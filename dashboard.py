import requests

API_URL = "http://127.0.0.1:5000/api/temperature"  # Endereço do servidor

def get_data():
    """Obtém os dados da API"""
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def display_dashboard(data):
    """Exibe os dados de temperatura em um formato simples"""
    print("Temperatura | Timestamp")
    print("-------------------------")
    for entry in data:
        print(f"{entry['temperature']}°C   | {entry['timestamp']}")

if __name__ == "__main__":
    data = get_data()
    display_dashboard(data)
