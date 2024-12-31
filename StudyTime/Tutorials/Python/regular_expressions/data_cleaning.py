import re

# data cleaning
def clean_text(text):
    # Removes anything that is not a letter, number, or space
    pattern = r'[^\w\s]'
    return re.sub(pattern, '', text)

# Example usage
dirty_text = "Hello! This text, has: punctuation... #unwanted"
print(clean_text(dirty_text))  # 'Hello This text has punctuation unwanted'