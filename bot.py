import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Credenciais da Z-API
ID_INSTANCE = '3E040EE5568A20BC7EA3A622FD8821DA'
TOKEN_INSTANCE = 'E02980FF2B6A3D74CB2021B2'

# Endpoint da Z-API
BASE_URL = f"https://api.z-api.io/instances/{ID_INSTANCE}/token/{TOKEN_INSTANCE}/send-message"

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    phone = data.get('phone')
    message = data.get('message')

    payload = {
        "phone": phone,
        "message": {
            "text": message
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(BASE_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify({"success": True, "response": response.json()})
    else:
        return jsonify({"success": False, "response": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
