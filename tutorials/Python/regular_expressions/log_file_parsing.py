import re

# log file parsing
def extract_error_logs(log_data):
    pattern = r'ERROR: (\d+): ([\w\s]+)'
    return re.findall(pattern, log_data)

# Example usage
log = "INFO: 200: Success\nERROR: 404: Not Found\nERROR: 500: Server Error"
print(extract_error_logs(log))  # [('404', 'Not Found'), ('500', 'Server Error')]