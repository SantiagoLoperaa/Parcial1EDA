# Acá ocurre la magia baby. Definitivamente nada fue más difícil que el hp motor de simulación, este parcial ha sido una hemorroides definitivamente.

import logging
from estructuras_datos import BolsaActivos, PilaHistorial
from modelos import Usuario
from motor_simulacion import MotorSimulacion

def configurar_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def crear_usuarios_iniciales():
    return [
        Usuario(1, "Ana", 1_000_000, BolsaActivos, PilaHistorial),
        Usuario(2, "Luis", 1_000_000, BolsaActivos, PilaHistorial),
        Usuario(3, "Maya", 1_000_000, BolsaActivos, PilaHistorial),
    ]

def main():
    configurar_logging()
    tasa_cambio_usd_a_cop = 4200
    usuarios = crear_usuarios_iniciales()

    # Inicializar motor con lista vacía (se llenará desde la API, que hp gallo)
    motor = MotorSimulacion(usuarios, [], tasa_cambio_usd_a_cop)

    # Cargar precios y lista completa de criptos desde API
    motor.mercado.cargar_precios_desde_api()
    motor.lista_simbolos_cripto = motor.mercado.lista_simbolos_cripto

    # Simulación de 10 turnos
    for turno in range(10):
        logging.info(f"--- Turno {turno+1} ---")
        motor.ejecutar_turno()

        # =========================
        #  De acá pa abajo es FASE 2, procesamiento de órdenes primero
        # =========================
        motor.procesar_una_orden()
        motor.procesar_una_orden()

    # =========================
    #  Reporte final, también de fase 2
    # =========================
    motor.generar_reporte_final()

if __name__ == "__main__":
    main()
