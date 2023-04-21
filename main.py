""" 
Se necesita desarrollar un programa que calcula el costo de envío de paquetes y el total a pagar para una 
tienda en línea. Los costos de envío varían según el destino del paquete y el método de envío elegido 
(envío estándar, envío express y envío premium). Además, es posible que en el futuro se agreguen nuevos 
métodos de envío o destinos. Queremos asegurarnos de que nuestro programa sea fácilmente extensible y 
que se pueda agregar nuevos cálculos de costo sin tener que cambiar el código existente.  """

from envio import CalculoEnvio, EnvioEstandar, EnvioExpress, EnvioPremium
from pedido import Pedido

pedido = Pedido(destino="Colombia", valorCompra=100.00)
envio = EnvioPremium()
costo = envio.calcular_envio(pedido)
totalPago = costo + pedido.valorCompra
print(f"Costo de envío: {costo}")
print(f"Total a pagar: {totalPago}")