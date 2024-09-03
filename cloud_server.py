from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulação de banco de dados em memória
temperature_data = []

@app.route('/api/temperature', methods=['POST'])
def receive_temperature():
    data = request.json
    temperature = data.get("temperature")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if temperature is not None:
        temperature_data.append({"temperature": temperature, "timestamp": timestamp})
        return jsonify({"message": "Dados recebidos"}), 200
    else:
        return jsonify({"message": "Sem dados"}), 400

@app.route('/api/temperature', methods=['GET'])
def get_temperature_data():
    return jsonify(temperature_data), 200

if __name__ == "__main__":
    app.run(debug=True)
