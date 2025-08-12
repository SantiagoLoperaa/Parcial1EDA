import requests
import random
from historialtransacciones import Historial
from bolsa import Cartera


url = "https://api.coinlore.net/api/tickers/"

    # Hacer la solicitud GET
response = requests.get(url)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    data = response.json()  # Convertir respuesta a diccionario de Python
    monedas = data.get("data", [])  # Lista de criptomonedas
    
class Accion:
    def __init__(self, descripcion, monto, cantidad, criptomoneda):
        self.descripcion = descripcion
        self.monto = monto
        self.cantidad = cantidad
        self.criptomoneda = criptomoneda
    
class Transaccion(Accion):
    def __init__(self, descripcion, monto, cantidad, criptomoneda):
        super().__init__(descripcion, monto, cantidad, criptomoneda):
        

class Usuario(Historial, Cartera, Transaccion):
  def __init__(self, id, nombre, saldo, historial, cartera):
    super().__init__(historial, cartera)
    self.id = id
    self.nombre = nombre
    self.saldo = saldo
    self.historial = historial 
    self.cartera = cartera
    
    def Movimiento(self, descripcion, monto, cantidad):
        descripcion = random.choice(["Compra", "Venta"])
        monto = random.randint(monedas['price_usd'])
        cantidad = random.randint(1, 5)

    transaccion = Transaccion(descripcion, monto, cantidad, self.criptomoneda)
    return transaccion
    



    
    
usuario1 = Usuario(1, "Juan", 1000, [], {})
transaccion = Movimiento()
print(transaccion)



