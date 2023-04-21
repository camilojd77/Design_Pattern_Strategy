from calculador_de_costo_de_envio import CalculadorDeCostoDeEnvio

class CalculadorDeCostoDeEnvioNacional(CalculadorDeCostoDeEnvio):
    def calcular_costo_de_envio(self, destino: str, detalles_envio: dict) -> float:
        # Realizar el cálculo de costo de envío para envíos nacionales
        # y devolver el costo de envío correspondiente.
        return 10.0
