import requests

# URL de la API
url = "https://api.coinlore.net/api/tickers/"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    data = response.json()  # Convertir respuesta a diccionario de Python
    monedas = data.get("data", [])  # Lista de criptomonedas

    # Mostrar algunas monedas
    for moneda in monedas:  # Solo las primeras 5
        print(f"{moneda['symbol']} - {moneda['name']}: ${moneda['price_usd']}")
else:
    print(f"Error {response.status_code}: No se pudo obtener la información")
