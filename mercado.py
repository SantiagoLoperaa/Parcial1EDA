# Acá quiero gestionar los comportamientos de las criptos baby, ojalá funcione todo bien.
#Gracias a ChatGPT por ayudarme a traducir el código de Java de Juanpa y resolverme duditas lógicas.
import urllib.request #https://docs.python.org/es/3.13/library/urllib.html Fue la que ví easy pa manejar URLs, si veo otra que me guste, tal vez la cambie.
import json
import logging
import random

class MercadoCriptomonedas:
    """Gestiona los precios de criptomonedas y su actualización."""
    def __init__(self, lista_simbolos_cripto, tasa_cambio_usd_a_cop):
        self.lista_simbolos_cripto = list(lista_simbolos_cripto)
        self.tasa_cambio_usd_a_cop = float(tasa_cambio_usd_a_cop)
        self.precios_en_usd = {}

    def cargar_precios_desde_api(self):
        """Carga TODOS los precios actuales desde Coinlore API."""
        url = "https://api.coinlore.net/api/tickers/"
        try:
            with urllib.request.urlopen(url, timeout=10) as respuesta:
                contenido = respuesta.read().decode("utf-8")
                datos = json.loads(contenido).get("data", [])
                # Guardar todos los símbolos y precios de la API
                self.precios_en_usd = {
                    item["symbol"]: float(item["price_usd"])
                    for item in datos if "symbol" in item and "price_usd" in item
                }
                # Actualizar lista de símbolos con todos los disponibles
                self.lista_simbolos_cripto = list(self.precios_en_usd.keys())
                logging.info(f"Precios iniciales cargados ({len(self.precios_en_usd)} criptos): {self.lista_simbolos_cripto}")
        except Exception as e:
            logging.error(f"No se pudieron cargar precios desde API: {e}")
            # Valor de respaldo si la API falla
            self.precios_en_usd = {"BTC": 100.0}
            self.lista_simbolos_cripto = ["BTC"]

    def fluctuar_precios(self, max_porcentaje=0.05):
        """Aplica una fluctuación aleatoria a los precios."""
        for simbolo, precio in self.precios_en_usd.items():
            variacion = random.uniform(-max_porcentaje, max_porcentaje)
            self.precios_en_usd[simbolo] = max(0.0, precio * (1 + variacion))
