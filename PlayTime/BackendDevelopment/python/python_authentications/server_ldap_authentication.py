"""

Use Case: Used in enterprise environments for authentication against a centralized directory of users, such as Active Directory or OpenLDAP.

Common in: Corporate environments, internal applications, enterprise networks.

Security: Secure if used with encrypted connections (e.g., LDAPS). It integrates well with internal user management systems.

"""

from ldap3 import Server, Connection, ALL
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the LDAP server and base DN (Distinguished Name)
LDAP_SERVER = "ldap://your-ldap-server.com"
BASE_DN = "dc=example,dc=com"

@app.route('/ldap-login', methods=['POST'])
def ldap_login():
    """Authenticate user against an LDAP server."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Construct the full distinguished name (DN) for the user
    user_dn = f"cn={username},{BASE_DN}"

    # Connect to the LDAP server
    try:
        server = Server(LDAP_SERVER, get_info=ALL)
        conn = Connection(server, user=user_dn, password=password)
        # Perform the bind operation (authenticate)
        if conn.bind():
            return jsonify({"message": f"LDAP authentication successful for user: {username}"}), 200
        else:
            return jsonify({"message": "LDAP authentication failed"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        conn.unbind()

if __name__ == "__main__":
    app.run(debug=True)
