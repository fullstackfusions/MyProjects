"""

This script is performing data intensive task. In this script, we are understanding how we can use the multiprocessing on chunks of lot of data. 

Note: This example is tested on millions of records and hence proven pretty efficient solution.

Example overview,

(Assume following source objects are fetched from some api call or from s3 bucket or any other source)
- source1_dir has 225 json files, each file is holding 10000 json objects in a list
- source2_dir has 205 json files, each file is holding 10000 json objects in a list
- source3_dir has 220 json files, each file is holding 10000 json objects in a list

Now we need to find the match and update the object or find some relation between each record, 
- for that suppose source1 object are reference data, 
- source2 files' each objects' has to check relation with reference data and update if there's any match or add as a new object in reference data if there's no match, 
- similarly for source3 files' each objects' has to check relation with new reference data

Limitations:
- we cannot open and close files everytime, it will reduce the speed
- we cannot use single process to check each relation for each objects, that will be time consuming
- we cannot store data in instance object while there's parallel processes are being run, this will not hold any data. for example, final result of `update_or_add_output_data` cannot be store in instance variable, you will get empty result at the end of whole process.

Possible Solutions:
- we can use multiprocessing that will solve the time issue, processes will be running in parallel so total time will be divided by number of workers
- we can create a hash of the something that can help us check relation very quickly, instead of checking each object's -> each keys' -> each values'. 
- we can create an instance variable which can be accessible anywhere in the instance during the code, just make sure you don't use them inside the parallel processes.


"""


import os
import json
from collections import defaultdict
from multiprocessing import Pool
from datetime import datetime

class Mapping:

    def __init__(self):

        # `today` is used to keep latest data separate from previous records, assuming we have a requirement to keep fresh data separate
        today = datetime.now().strftime("%Y%m%d")

        # Output directory is holding final result
        self.output_dir = f"{today}/output"
        self.source1_dir = f"{today}/source1"
        self.source2_dir = f"{today}/source2"
        self.source3_dir = f"{today}/source3"

        # Checklist is the name of all columns we are expecting in each object of response
        self.check_list = ["DeviceIP", "DeviceMAC", "DeviceName", "DeviceInterface", "DeviceType", "RemoteDeviceName", "RemoteDeviceInterface", "RemoteDeviceIP", "ConnectionType", "Label"]
        
        # Matchlist is the unique key names of columns that we can create their hash
        self.match_list = ["DeviceIP", "DeviceMAC", "DeviceName"]

        # Extralist is the extra column names which cannot be unique, we are required to update them or find a relation
        self.extra_list = ["DeviceInterface", "DeviceType", "RemoteDeviceName", "RemoteDeviceInterface", "RemoteDeviceIP", "ConnectionType", "Label"]

        # This is an instance variable we are using to speed up the access during any running instance
        self.main_data_map = defaultdict(list)  # Use defaultdict to simplify appending

    # Load json from local
    def load_json_from_local(self, file):
        with open(file, "r") as f:
            return json.load(f)
    
    # Save output entries in json in specific chunks
    def save_output_entries(self, output_entries, batch_size=10000):
        # Flattened entries are extracting out sublists from output entries and create a list of objects
        flattened_entries = [item for sublist in output_entries for item in sublist]
        
        for i in range(0, len(flattened_entries), batch_size):
            # Slicing the list with their batch size
            batch = flattened_entries[i:i+batch_size]
            file_name = f"{self.output_dir}/output_entries_{i//batch_size + 1}.json"
            with open(f"result/{file_name}", "w") as f:
                json.dump(batch, f, indent=4)
    
    # Create a first reference entry in instance object
    def keys_for_output_entries(self, source1_list):
        for entry in source1_list:
            for obj in entry:
                key = self.get_match_list(obj)

                # The primary advantage of defaultdict is that it provides a default value for non-existent keys, so you don't need to check if a key exists before assigning a value.
                if key not in self.main_data_map:
                    self.main_data_map[key].append(obj)

    # Generate a partial hash
    def get_match_list(self, item):
        return tuple(item[key] for key in self.match_list if item.get(key))

    
    # This function is used by parallel process so make sure you don't store anythin in instance variable inside this function
    def update_or_add_output_data(self, new_data):
        
        # As we cannot use instance object so we use local defaultdict in each worker
        shared_data = defaultdict(list)
        
        for new_item in new_data:

            # Filtering out unnecessary values from object
            if any(new_item[key] == "unknown" for key in self.check_list):
                continue
            
            # Getting hash
            new_key = self.get_match_list(new_item)

            # Checking hash, also consider we are not required to use shared_data.items() as it is holding list of keys and list of values
            if new_key in shared_data:
                updated = False
                for existing_obj in shared_data[new_key]:
                    if all(existing_obj[extra_key] == new_item[extra_key] or new_item[extra_key] == "unknown"
                           for extra_key in self.extra_list):
                        # Update missing fields
                        for check_key in self.check_list:
                            if not existing_obj[check_key] and new_item[check_key]:
                                existing_obj[check_key] = new_item[check_key]
                        updated = True
                        break

                if not updated:
                    shared_data[new_key].append(new_item)
            else:
                shared_data[new_key].append(new_item)
        return shared_data

    # Parallel processes to speed up the relation mapping process
    def parallel_process_output_data(self, data_list, num_workers=8):
        # Flatten the data_list to make sure we're working with a list of items
        flat_data_list = []
        for sublist in data_list:
            flat_data_list.extend(sublist)

        # Split the flat_data_list evenly across workers
        chunk_size = len(flat_data_list) // num_workers
        data_chunks = [flat_data_list[i:i + chunk_size] for i in range(0, len(flat_data_list), chunk_size)]
        
        # If there are any remainder items that don't fit evenly, add them to the last chunk
        if len(flat_data_list) % num_workers != 0:
            data_chunks[-1].extend(flat_data_list[chunk_size * num_workers:])

        with Pool(processes=num_workers) as pool:
            # Result is a list of defaultdict objects
            result = pool.map(self.update_or_add_output_data, data_chunks)

        # Merge the results from all workers into self.main_data_map
        self.merge_results(result)

    def merge_results(self, result_list):
        for result in result_list:
            for key, items in result.items():
                existing_items = {json.dumps(i, sort_keys=True) for i in self.main_data_map[key]}  # Avoid duplicates
                for item in items:
                    item_json = json.dumps(item, sort_keys=True)  # Convert item to JSON string for comparison
                    if item_json not in existing_items:
                        self.main_data_map[key].append(item)
                        existing_items.add(item_json)  # Track new additions


    def local_map_files_in_parallel(self):
        
        def load_files(directory):
            files = [os.path.join(f"result/{directory}", f) for f in sorted(os.listdir(f"result/{directory}"))]
            return [self.load_json_from_local(file) for file in files]

        source2_list = load_files(self.source2_dir)
        source1_list = load_files(self.source1_dir)
        source3_list = load_files(self.source3_dir)

        self.keys_for_output_entries(source1_list)

        # Combine lists for parallel processing
        combined_list = source2_list + source3_list

        self.parallel_process_output_data(combined_list)

        # Save the processed entries
        self.save_output_entries(list(self.main_data_map.values()))

if __name__ == "__main__":
    mapping = Mapping()
    mapping.local_map_files_in_parallel()


