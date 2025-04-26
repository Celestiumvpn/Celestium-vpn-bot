import requests
from flask import Flask, request, jsonify

app = Flask(_name_)

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

    payload = {
        "phone": phone,
        "message": message
    }

    response = requests.post(BASE_URL, json=payload)

    if response.status_code == 200:
        return jsonify({"success": True, "response": response.json()})
    else:
        return jsonify({"success": False, "response": response.text}), response.status_code

@app.route('/')
def home():
    return "Celestium VPN Bot Online! Comando para enviar: /send"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=10000)
