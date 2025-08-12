class MiClaseConPila:
    def __init__(self):
        self.pila = []  # Inicializa la pila como una lista vacía

    def apilar(self, elemento):
        """Agrega un elemento a la pila."""
        self.pila.append(elemento)

    def desapilar(self):
        """Elimina y devuelve el elemento superior de la pila."""
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return None  # O lanzar una excepción si la pila está vacía

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.pila) == 0

    def cima(self):
        """Devuelve el elemento superior de la pila sin eliminarlo."""
        if not self.esta_vacia():
            return self.pila[-1]
        else:
            return None  # O lanzar una excepción si la pila está vacía

# Ejemplo de uso
mi_objeto = MiClaseConPila()
mi_objeto.apilar(10)
mi_objeto.apilar(20)
mi_objeto.apilar(30)

print(f"Cima de la pila: {mi_objeto.cima()}")  # Output: Cima de la pila: 30
print(f"Elemento desapilado: {mi_objeto.desapilar()}")  # Output: Elemento desapilado: 30
print(f"¿La pila está vacía? {mi_objeto.esta_vacia()}")  # Output: ¿La pila está vacía? False



def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

def obtener_historial(self):
        return self.transacciones