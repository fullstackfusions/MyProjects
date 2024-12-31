"""

Twilio Setup for Sending OTP
- Sign up for a Twilio account.
- Get the following credentials from your Twilio dashboard:
    - TWILIO_ACCOUNT_SID
    - TWILIO_AUTH_TOKEN
    - TWILIO_PHONE_NUMBER (the Twilio phone number that will send SMS).


Explanation of the Flow:

Request OTP (/request-otp):
- The user submits their phone number to request an OTP.
- A 6-digit OTP is generated using generate_otp().
- The OTP is sent via SMS to the user's phone using Twilio (send_otp()).
- The OTP is temporarily stored in otp_db with a timestamp to handle expiration (set for 5 minutes).

Verify OTP (/verify-otp):
- The user submits the phone number and the OTP they received.
- The server checks if the OTP matches what was sent to that phone number.
- If the OTP is correct and not expired, the user is authenticated.
- If the OTP is incorrect or expired, the server responds with an error message.

"""

# pip install Flask twilio

import random
import time
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Simulated database for users and OTP storage
users_db = {}
otp_db = {}

# Twilio client setup
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def generate_otp():
    """Generate a random 6-digit OTP."""
    return random.randint(100000, 999999)

def send_otp(phone_number, otp):
    """Send OTP to the user via SMS using Twilio."""
    message = client.messages.create(
        body=f"Your verification code is {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    return message.sid

@app.route('/request-otp', methods=['POST'])
def request_otp():
    """User requests OTP by providing their phone number."""
    phone_number = request.json.get('phone_number')

    if not phone_number:
        return jsonify({"message": "Phone number is required"}), 400

    otp = generate_otp()
    send_otp(phone_number, otp)

    # Store the OTP along with a timestamp for expiry
    otp_db[phone_number] = {
        "otp": otp,
        "timestamp": time.time()  # Store the time to expire OTP later
    }

    return jsonify({"message": f"OTP sent to {phone_number}"}), 200

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    """User verifies the OTP."""
    phone_number = request.json.get('phone_number')
    otp_provided = request.json.get('otp')

    if not phone_number or not otp_provided:
        return jsonify({"message": "Phone number and OTP are required"}), 400

    # Check if the OTP exists and hasn't expired (expiry time: 5 minutes)
    otp_record = otp_db.get(phone_number)
    if otp_record:
        otp_stored = otp_record["otp"]
        timestamp = otp_record["timestamp"]

        # Check if OTP is still valid (expires after 300 seconds/5 minutes)
        if time.time() - timestamp > 300:
            return jsonify({"message": "OTP has expired!"}), 401

        if otp_provided == str(otp_stored):
            return jsonify({"message": "OTP is valid! User authenticated."}), 200
        else:
            return jsonify({"message": "Invalid OTP!"}), 401
    else:
        return jsonify({"message": "OTP not found for this phone number!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
