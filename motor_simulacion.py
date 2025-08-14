# Acá voy a gestionar la lógica de simulación de mercado (Fase 1). Gracias Copilot y ChatGPT por ayudarme con el orden lógico, eso me tenía loco. Especiales agradecimientos a ellos en esta sección porque me desenredaron, ya que si le pregunto a Juanpa, me pega

import logging
import random
import json
from estructuras_datos import ColaOrdenes
from modelos import TipoOperacion, Transaccion
from mercado import MercadoCriptomonedas

class MotorSimulacion:
    """Motor para simular un mercado de criptomonedas (Fase 1)."""
    def __init__(self, lista_usuarios, lista_simbolos_cripto, tasa_cambio_usd_a_cop):
        self.usuarios = {usuario.id_usuario: usuario for usuario in lista_usuarios}
        self.lista_simbolos_cripto = list(lista_simbolos_cripto)
        self.cola_ordenes = ColaOrdenes()
        self.mercado = MercadoCriptomonedas(self.lista_simbolos_cripto, tasa_cambio_usd_a_cop)
        self.tasa_cambio_usd_a_cop = float(tasa_cambio_usd_a_cop)

    def generar_orden_aleatoria(self, usuario):
        """Genera una orden aleatoria de compra o venta para un usuario."""
        if not self.lista_simbolos_cripto:
            logging.warning("No hay criptomonedas disponibles para generar órdenes.")
            return

        if random.random() < 0.6:  # 60% de probabilidad de operar
            tipo_operacion = TipoOperacion.COMPRA if random.random() < 0.5 else TipoOperacion.VENTA
            simbolo_cripto = random.choice(self.lista_simbolos_cripto)
            precio_usd = self.mercado.precios_en_usd.get(simbolo_cripto, 0)

            if tipo_operacion == TipoOperacion.COMPRA:
                presupuesto_usd = random.uniform(10, 200)
                cantidad_cripto = presupuesto_usd / precio_usd if precio_usd > 0 else 0
            else:
                disponible = usuario.portafolio_cripto.obtener_cantidad_activo(simbolo_cripto)
                cantidad_cripto = random.uniform(0, disponible) if disponible > 0 else 0

            if cantidad_cripto > 0:
                transaccion = Transaccion(usuario.id_usuario, simbolo_cripto, cantidad_cripto, precio_usd, tipo_operacion)
                self.cola_ordenes.encolar_orden(transaccion)
                logging.info(f"Orden generada: {transaccion}")

    def ejecutar_turno(self):
        """Ejecuta un turno de la simulación (solo generación de órdenes)."""
        self.mercado.fluctuar_precios()

        # Si la lista está vacía, usar todos los símbolos cargados en el mercado
        if not self.lista_simbolos_cripto:
            self.lista_simbolos_cripto = list(self.mercado.precios_en_usd.keys())

        for usuario in self.usuarios.values():
            self.generar_orden_aleatoria(usuario)

    # ================================
    #  Acá estará el procesamiento de órdenes. Fase 2 se viene muchachos.
    # ================================
    def procesar_una_orden(self):
        """Procesa una orden del libro, validando y actualizando datos."""
        if self.cola_ordenes.esta_vacia():
            logging.info("No hay órdenes para procesar.")
            return

        orden = self.cola_ordenes.desencolar_orden()
        usuario = self.usuarios.get(orden.id_usuario)
        if not usuario:
            logging.error(f"Usuario {orden.id_usuario} no encontrado, orden descartada.")
            return

        precio_en_cop = orden.precio_en_usd * self.tasa_cambio_usd_a_cop

        try:
            if orden.tipo_operacion == TipoOperacion.COMPRA:
                costo_cop = orden.cantidad_cripto * precio_en_cop
                saldo_cop = usuario.billetera_cop.obtener_cantidad_activo("COP")

                if saldo_cop < costo_cop:
                    logging.warning(f"Compra inválida: saldo insuficiente para {usuario.nombre_usuario}")
                    return

                usuario.billetera_cop.quitar_activo("COP", costo_cop)
                usuario.portafolio_cripto.agregar_activo(orden.simbolo_cripto, orden.cantidad_cripto)
                usuario.historial_transacciones.apilar_transaccion(orden)
                logging.info(f"{usuario.nombre_usuario} compra {orden.cantidad_cripto:.6f} {orden.simbolo_cripto}")

            else:  # VENTA
                disponible = usuario.portafolio_cripto.obtener_cantidad_activo(orden.simbolo_cripto)
                if disponible < orden.cantidad_cripto:
                    logging.warning(f"Venta inválida: no hay suficiente {orden.simbolo_cripto} para {usuario.nombre_usuario}")
                    return

                usuario.portafolio_cripto.quitar_activo(orden.simbolo_cripto, orden.cantidad_cripto)
                recibido_cop = orden.cantidad_cripto * precio_en_cop
                usuario.billetera_cop.agregar_activo("COP", recibido_cop)
                usuario.historial_transacciones.apilar_transaccion(orden)
                logging.info(f"{usuario.nombre_usuario} vende {orden.cantidad_cripto:.6f} {orden.simbolo_cripto}")

        except Exception as e:
            logging.error(f"Error procesando la orden {orden}: {e}")

    def generar_reporte_final(self, nombre_archivo="reporte_final.json"):
        """Genera y guarda un reporte final con el estado de todos los usuarios."""
        precios_finales = self.mercado.precios_en_usd
        reporte = {
            "tasa_cambio_usd_a_cop": self.tasa_cambio_usd_a_cop,
            "precios_finales_usd": precios_finales,
            "usuarios": []
        }

        for usuario in self.usuarios.values():
            saldo_cop = usuario.billetera_cop.obtener_cantidad_activo("COP")
            activos = []
            valor_portafolio_cop = 0

            for simbolo, cantidad in usuario.portafolio_cripto.obtener_todos_los_activos().items():
                precio_usd = precios_finales.get(simbolo, 0)
                valor_cop = cantidad * precio_usd * self.tasa_cambio_usd_a_cop
                valor_portafolio_cop += valor_cop
                activos.append({
                    "simbolo": simbolo,
                    "cantidad": cantidad,
                    "precio_usd": precio_usd,
                    "valor_cop": valor_cop
                })

            historial = []
            for transaccion in usuario.historial_transacciones.obtener_transacciones_mas_recientes():
                historial.append({
                    "tipo": transaccion.tipo_operacion.value,
                    "simbolo": transaccion.simbolo_cripto,
                    "cantidad": transaccion.cantidad_cripto,
                    "precio_usd": transaccion.precio_en_usd
                })

            reporte["usuarios"].append({
                "id_usuario": usuario.id_usuario,
                "nombre": usuario.nombre_usuario,
                "saldo_cop": saldo_cop,
                "valor_portafolio_cop": valor_portafolio_cop,
                "activos": activos,
                "historial": historial
            })

        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=4, ensure_ascii=False)

        logging.info(f"Reporte final guardado en {nombre_archivo}")
