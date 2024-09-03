import requests  # Biblioteca para enviar requisições HTTP
import random    # Para gerar valores aleatórios
import time      # Para pausar o envio de dados

API_URL = "http://127.0.0.1:5000/api/temperature"  # Endereço do servidor

def get_temperature():
    """Simula a leitura da temperatura"""
    return round(random.uniform(20.0, 30.0), 2)

def send_data(temperature):
    """Envia os dados para a API na nuvem"""
    data = {"temperature": temperature}
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        print(f"Dado enviado com sucesso: {temperature}°C")
    else:
        print(f"Falha ao enviar dados: {response.status_code}")

if __name__ == "__main__":
    while True:
        temperature = get_temperature()
        send_data(temperature)
        time.sleep(5)  # Pausa de 5 segundos antes de enviar o próximo dado
