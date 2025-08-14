#Estructuras de Datos pa usar ahorita

class ColaOrdenes: #Voy a ponerle todas las funcinalidades que aprendí por si me llegan a ser útiles.
    """Cola que almacena órdenes de compra/venta (FIFO: primero en entrar, primero en salir). Gracias a Youtube aprendí esto"""
    def __init__(self):
        self._ordenes = []

    def encolar_orden(self, orden):
        """Agrega una orden al final de la cola. Ahorita creo que será útil"""
        self._ordenes.append(orden)

    def desencolar_orden(self):
        """Elimina y devuelve la primera orden en la cola. De pronto si necesito hacer alguna validación ahorita pa ver como va la cosa"""
        if self.esta_vacia():
            raise IndexError("La cola de órdenes está vacía")
        return self._ordenes.pop(0)

    def ver_primera_orden(self):
        """Devuelve la primera orden sin eliminarla. Pa lo mismo, validaciones"""
        if self.esta_vacia():
            raise IndexError("La cola de órdenes está vacía")
        return self._ordenes[0]

    def esta_vacia(self):
        """Indica si la cola no contiene órdenes. No debería pasar, pero por si las"""
        return len(self._ordenes) == 0

    def obtener_tamano(self):
        """Cantidad de órdenes en la cola."""
        return len(self._ordenes)


class PilaHistorial:
    """Pila que almacena el historial de transacciones de un usuario (LIFO: último en entrar, primero en salir)."""
    def __init__(self):
        self._transacciones = []

    def apilar_transaccion(self, transaccion):
        """Agrega una transacción al historial."""
        self._transacciones.append(transaccion)

    def desapilar_transaccion(self):
        """Elimina y devuelve la transacción más reciente."""
        if self.esta_vacia():
            raise IndexError("El historial de transacciones está vacío")
        return self._transacciones.pop()

    def ver_transaccion_reciente(self):
        """Devuelve la transacción más reciente sin eliminarla."""
        if self.esta_vacia():
            raise IndexError("El historial de transacciones está vacío")
        return self._transacciones[-1]

    def esta_vacia(self):
        """Indica si el historial está vacío."""
        return len(self._transacciones) == 0

    def obtener_tamano(self):
        """Cantidad de transacciones en el historial."""
        return len(self._transacciones)

    def obtener_transacciones_mas_recientes(self):
        """Devuelve las transacciones con la más reciente primero."""
        return list(reversed(self._transacciones))


class BolsaActivos: #"activos" me pareció un nombre más pro para el saldo del usuario
    """Bolsa que almacena los activos (criptomonedas o saldo en COP) de un usuario."""
    def __init__(self):
        self._activos = {}

    def agregar_activo(self, nombre_activo, cantidad_activo):
        """Agrega una cantidad de un activo."""
        if cantidad_activo < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._activos[nombre_activo] = self._activos.get(nombre_activo, 0) + cantidad_activo

    def quitar_activo(self, nombre_activo, cantidad_activo):
        """Quita una cantidad de un activo."""
        if cantidad_activo < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if self._activos.get(nombre_activo, 0) < cantidad_activo:
            raise ValueError(f"No hay suficiente {nombre_activo} en la bolsa")
        self._activos[nombre_activo] -= cantidad_activo
        if self._activos[nombre_activo] <= 0:
            del self._activos[nombre_activo]

    def obtener_cantidad_activo(self, nombre_activo):
        """Devuelve la cantidad disponible de un activo."""
        return self._activos.get(nombre_activo, 0)

    def obtener_todos_los_activos(self):
        """Devuelve todos los activos y cantidades."""
        return dict(self._activos)
