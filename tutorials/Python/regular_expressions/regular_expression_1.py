import re

def extract_email_phone(text):
    # Regex pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Regex pattern for matching phone numbers (simple pattern for demonstration)
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

    # Find all matches in the text
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    return emails, phones

# Example usage
sample_text = """
    Hello, my email address is example.email@example.com and my friend's is friend_email123@example.co.uk.
    You can call me at 123-456-7890 or reach my office at 123.456.7890.
"""

emails, phones = extract_email_phone(sample_text)
print("Emails found:", emails)
print("Phone numbers found:", phones)