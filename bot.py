import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Credenciais da Z-API
ID_INSTANCE = '3E04E0E5568A20BC7EA3A622FD8B21DA'
TOKEN_INSTANCE = 'E02980FF2B6A3D74CB2021B2'

# Endpoint da Z-API
BASE_URL = f"https://api.z-api.io/instances/{ID_INSTANCE}/token/{TOKEN_INSTANCE}/send-text"

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    phone = data.get('phone')
    message = data.get('message')

    # Pega o Client-Token vindo do cabeçalho
    client_token = request.headers.get('Client-Token')

    payload = {
        "phone": phone,
        "message": message
    }

    headers = {
        "Client-Token": client_token,
        "Content-Type": "application/json"
    }

    response = requests.post(BASE_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify({"success": True, "response": response.json()})
    else:
        return jsonify({"success": False, "response": response.text}), response.status_code
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
