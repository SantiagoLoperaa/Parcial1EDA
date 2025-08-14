# Por cuestiones de orden y por el regaño de Juanpa, acá van a estar las clases del programa, mejor dicho, los agentes que actúan en el proyecto.
#Ví que en POO se usa más la nomenclatura con guiones bajos que la camelCase que es la que me gusta, yo me adapto para que Juanpa no me regañe
from enum import Enum #https://docs.python.org/es/3/library/enum.html Estudiando me gustó esta opción para mejorar la legibilidad representando las constantes con más claridad.

class TipoOperacion(Enum):
    COMPRA = "COMPRA"
    VENTA = "VENTA"


class Transaccion:
    """Representa una transacción de compra o venta de criptomonedas. Todo al Bitcoin Vietnamita"""
    def __init__(self, id_usuario, simbolo_cripto, cantidad_cripto, precio_en_usd, tipo_operacion: TipoOperacion):
        self.id_usuario = int(id_usuario)
        self.simbolo_cripto = str(simbolo_cripto)
        self.cantidad_cripto = float(cantidad_cripto)
        self.precio_en_usd = float(precio_en_usd)
        self.tipo_operacion = tipo_operacion

    def __repr__(self):
        return (f"Transaccion(usuario={self.id_usuario}, "
                f"{self.tipo_operacion.value}, {self.cantidad_cripto:.6f} {self.simbolo_cripto} @ {self.precio_en_usd:.2f} USD)")


class Usuario:
    """Representa a un usuario del mercado de criptomonedas, gente con plata, básicamente"""
    def __init__(self, id_usuario, nombre_usuario, saldo_inicial_cop, clase_bolsa, clase_pila):
        self.id_usuario = int(id_usuario)
        self.nombre_usuario = str(nombre_usuario)
        self.billetera_cop = clase_bolsa()
        self.billetera_cop.agregar_activo("COP", float(saldo_inicial_cop))
        self.portafolio_cripto = clase_bolsa()
        self.historial_transacciones = clase_pila()

    def __repr__(self):
        return f"Usuario({self.id_usuario}, {self.nombre_usuario})"
