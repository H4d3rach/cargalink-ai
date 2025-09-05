from flask import Flask, jsonify, request
from chatbot import Chatbot
import pandas as pd
from sortEmpresas import sort_empresas
import logging

logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Formato del log
            handlers=[
                logging.FileHandler("files/logsAI-API.log"),
                logging.StreamHandler()
            ]
        )
app = Flask(__name__)
chatbot = Chatbot()

@app.route('/reordenar', methods=['POST'])
def reordenar():
    data = request.get_json()
    empresas = pd.json_normalize(data["empresas"])
    preferences = pd.json_normalize(data["preferencias"])
    empresas_sorted = sort_empresas(empresas, preferences)
    return jsonify(empresas_sorted)

@app.route('/chatbot', methods=['POST'])
def use_chatbot():
    data = request.get_json()
    response_chatbot = chatbot.get_response(data["pregunta"])
    response = {
            "pregunta": data["pregunta"], 
            "respuesta": response_chatbot[0],
            "excedeUmbral": response_chatbot[1]
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)