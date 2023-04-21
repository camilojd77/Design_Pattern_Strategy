#Implementación del patro de diseño Strategy

from abc import ABC, abstractmethod

class CalculoEnvio(ABC):
    #La clase CalculoEnvio es la estrategia abstracta.

    @abstractmethod
    def calcular_envio(self, pedido):
        pass

class EnvioEstandar(CalculoEnvio):
    #La clase EnvioEstandar es una estrategia concreta.

    def calcular_envio(self, pedido):
        if pedido.destino == "Colombia":
            return 5.00
        elif pedido.destino == "México":
            return 20.00
        elif pedido.destino == "Perú":
            return 10.00
        elif pedido.destino == "Chile":
            return 15.00
        else:
            raise ValueError("Destino no válido")

class EnvioExpress(CalculoEnvio):
    #La clase EnvioExpress es otra estrategia concreta.

    def calcular_envio(self, pedido):
        if pedido.destino == "Colombia":
            return 15.00
        elif pedido.destino == "México":
            return 30.00
        elif pedido.destino == "Perú":
            return 20.00
        elif pedido.destino == "Chile":
            return 25.00
        else:
            raise ValueError("Destino no válido")

class EnvioPremium(CalculoEnvio):
    #La clase EnvioPremium es otra estrategia concreta.

    def calcular_envio(self, pedido):
        if pedido.destino == "Colombia":
            return 25.00
        elif pedido.destino == "México":
            return 40.00
        elif pedido.destino == "Perú":
            return 30.00
        elif pedido.destino == "Chile":
            return 35.00
        else:
            raise ValueError("Destino no válido")
