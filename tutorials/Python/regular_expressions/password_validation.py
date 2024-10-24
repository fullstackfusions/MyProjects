import re
# password validation
def is_valid_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    return re.match(pattern, password) is not None

# Test the function
print(is_valid_password("Passw0rd!"))  # True
print(is_valid_password("password"))   # False