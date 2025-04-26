from flask import Flask, request
import requests

app = Flask(__name__)

# Troque pelos seus dados da API do Zap'n
ZAPN_TOKEN = "SEU_TOKEN_AQUI"
ZAPN_INSTANCE_ID = "SEU_ID_AQUI"

@app.route("/", methods=["GET"])
def home():
    return "Celestium VPN - Online", 200

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    # Extrai informações básicas
    phone_number = data['message']['from']
    message_text = data['message']['body'].lower()

    # Lógica de resposta simples
    if "teste" in message_text:
        send_message(phone_number, "Olá! Aqui é a CELESTIUM VPN. Seu teste gratuito foi iniciado. Aproveite!")
    elif "comprar" in message_text:
        send_message(phone_number, "Ótimo! Para comprar seu plano CELESTIUM VPN, envie seu comprovante para este número.")
    else:
        send_message(phone_number, "Olá, seja bem-vindo à CELESTIUM VPN! Para iniciar um teste, digite 'Teste'. Para comprar, digite 'Comprar'.")

    return "Success", 200

def send_message(phone, message):
    url = f"https://api.z-api.io/instances/{ZAPN_INSTANCE_ID}/token/{ZAPN_TOKEN}/send-text"
    payload = {
        "phone": phone,
        "message": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    requests.post(url, json=payload, headers=headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
