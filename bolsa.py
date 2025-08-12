class Cartera:
    Billetera = {}  

    def __init__(self, saldo):
        self.saldo = saldo

    def agregar_al_diccionario(self, clave, saldo):
        Cartera.Billetera[clave] = saldo
