from calculador_de_costo_de_envio import CalculadorDeCostoDeEnvio

class CalculadorDeCostoDeEnvioLocal(CalculadorDeCostoDeEnvio):
    def calcular_costo_de_envio(self, destino: str, detalles_envio: dict) -> float:
        # Realizar el cálculo de costo de envío para envíos locales
        # y devolver el costo de envío correspondiente.
        return 5.0
