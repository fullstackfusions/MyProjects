# extract key value pairs
import re

def extract_key_value_pairs(text, keys):
    extracted_data = {}
    for key in keys:
        pattern = rf'{key}: (\S+)'
        match = re.search(pattern, text)
        if match:
            extracted_data[key] = match.group(1)
    return extracted_data

# Example usage
text_report = "Date: 2021-01-01, Status: Success, OrderID: 123456, Amount: $150.00"
keys_to_extract = ["Date", "OrderID", "Amount"]
extracted_info = extract_key_value_pairs(text_report, keys_to_extract)

print(extracted_info)
# Output: {'Date': '2021-01-01', 'OrderID': '123456', 'Amount': '$150.00'}