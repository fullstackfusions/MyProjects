responses = ["some email response"]

EmailResponse = "email response schema"

def send_email(response):
    print("email sent")

# Using filter and lambda
filtered_responses = filter(lambda response: isinstance(response, EmailResponse), responses)
for response in filtered_responses:
    send_email(response)
