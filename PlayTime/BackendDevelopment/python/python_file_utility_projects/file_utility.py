import os
import json
import yaml
import logging
import zipfile
from io import BytesIO
from typing import Dict, Any, List

# For s3 file operations I am considering we are leveraging StorageConfig
# from projects/python_boto3_operations/S3_Storage_Operations/s3_storage_config.py
from projects.python_boto3_operations.S3_Storage_Operations.s3_storage_config import StorageConfig


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FileUtility:

    def __init__(self):
        self.storage_config = StorageConfig.from_env()
        self.s3_client = self.storage_config.client
        self.bucket_name = self.storage_config.bucket_name

    def load_json_from_local(self, file: str):
        with open(file, "r") as f:
            return json.load(f)
    
    def load_json_from_s3(self, file: str):
        file_obj = self.s3_client.get(bucket_name=self.bucket_name, object_key=file)
        data = file_obj["Body"].read().decode("utf-8")
        return json.loads(data)

    def load_s3_files(self, s3_path=""):
        try:
            files_response = self.s3_client.list_objects(bucket_name=self.bucket_name, directory=s3_path)
            files = [{"Key": obj["Key"]} for obj in files_response["Contents"]]
            for file in files:
                json_data = self.load_json_from_s3(file["Key"])

                file_name = file["Key"].split("/")[-1]
                self.save_json_to_local(json_data, file_name)
        except:
            logger.exception("error")

    def create_directory(self, path: str):
        try:
            os.makedirs(path, exist_ok=True)
            logger.info(f"Directory '{path}' created successfully.")
        except:
            logger.exception("Error creating directory")
    
    def save_json_to_local(self, data: dict, file_path: str):
        # "a" is for appending purpose
        # "w" is for write only purpose
        with open(f"{file_path}", "a") as f:
            json.dump(data, f, indent=4)
    
    def save_json_to_s3(self, data: dict, file_path: str):
        json_data = json.dumps(data, indent=4)
        bytes_io = BytesIO(json_data.encode("utf-8"))
        self.s3_client.upload(bucket_name=self.bucket_name, object_key=file_path, object_data=bytes_io)
        logger.info(f"File uploaded to s3://{self.bucket_name}/{file_path}")
    
    def save_json_archive_to_s3(self, data:dict, key:str):
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            json_data = json.dumps(data, indent=4)
            zip_file.writestr(f"{key}", json_data)
        
        zip_buffer.seek(0)
        self.s3_client.upload(bucket_name=self.bucket_name, object_key=key, object_data=zip_buffer)
        logger.info(f"File uploaded to {self.bucket_name}/{key}")

    def upload_local_directory_to_s3(self, local_directory: str, s3_path=""):
        # local_directory will be a direcotry name
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_directory)
                s3_file_path = os.path.join(s3_path, relative_path).replace("\\", "/")

                data = self.s3_client.upload_file(bucket_name=self.bucket_name, file_name=local_file_path, object_name=s3_file_path)
                if data:
                    logger.info(f"{local_file_path} uploaded successfully to s3://{self.bucket_name}/{s3_file_path}")
                else:
                    logger.exception(f"{local_file_path} not uploaded successfully.")
    
    def upload_local_file_to_s3(self, local_file_name: str, s3_file_name=""):
        data = self.s3_client.upload_file(bucket_name=self.bucket_name, file_name=local_file_name, object_name=s3_file_name)
        if data:
            logger.info(f"{local_file_name} uploaded successfully to s3://{self.bucket_name}/{s3_file_name}")
        else:
            logger.exception(f"{local_file_name} not uploaded successfully.")
    
    def delete_local_files(self, path):
        try:
            delete_objects = [os.path.join(path, f) for f in sorted(os.listdir(path))]
            if delete_objects:
                for file in delete_objects:
                    os.remove(file)
                    logger.info(f"Directory '{file}' deleted successfully.")
        except:
            logger.exception("Error deleting directory")
    
    def delete_s3_files(self, directory: str = ""):
        # you can provide specific directory and pass that in directory param of list objects
        response = self.s3_client.list_objects(Bucket=self.bucket_name)
        files = response.get("Contents", [])
        if files:
            self.s3_client.delete_objects(
                bucket_name=self.bucket_name,
                object_list=files
            )
            logger.info(f"{directory if directory else 'All files'} deleted successfully.")
    
    def delete_3days_old_objects(self):
        self.s3_client.delete_3days_old_objects(self.bucket_name)

    def write_to_yml_file(self, file:str, data):
        # Writing to a YAML file
        with open(file, 'w') as file:
            yaml.dump(data, file)

    def read_from_yml_file(self, file:str):
        # Reading from a YAML file
        with open(file, 'r') as file:
            loaded_data = yaml.safe_load(file)
            logger.info(loaded_data)
    