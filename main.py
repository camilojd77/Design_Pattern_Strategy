""" 
Se necesita desarrollar un programa que calcula el costo de envío de paquetes y el total a pagar para una 
tienda en línea. Los costos de envío varían según el destino del paquete y el método de envío elegido 
(envío estándar, envío express y envío premium). Además, es posible que en el futuro se agreguen nuevos 
métodos de envío o destinos. Queremos asegurarnos de que nuestro programa sea fácilmente extensible y 
que se pueda agregar nuevos cálculos de costo sin tener que cambiar el código existente.  """

from envio import CalculoEnvio, EnvioEstandar, EnvioExpress, EnvioPremium
from pedido import Pedido

continuar = True
while (continuar):
    print("Ingrese el destino del pedido: ")
    destinoSleccionado = input()
    print("Ingrese valor compra: ")
    valorCompraIngresado = input()
    print("Ingrese el número del método de envío: 1-Estandar, 2-Express, 3-Premium")
    metodoEnvio = input()

    if metodoEnvio == "1":
        metodoEnvio = EnvioEstandar()
    elif metodoEnvio == "2":
        metodoEnvio = EnvioExpress()
    elif metodoEnvio == "3":
        metodoEnvio = EnvioPremium()
    else:
        print("Método de envío no válido")
    
    valorCompraIngresado = float(valorCompraIngresado)

    print(f"Destino: {destinoSleccionado}")
    print(f"Método de envío: {metodoEnvio.__class__.__name__.replace('Envio','Envío ').replace('()','')}")
    print(f"Valor Compra: {valorCompraIngresado} dólares")

    pedido = Pedido(destino=destinoSleccionado, valorCompra=valorCompraIngresado)
    envio = metodoEnvio
    costo = envio.calcular_envio(pedido)
    totalPago = costo + pedido.valorCompra
    print(f"Costo de envío: {costo} dólares")
    print(f"Total a pagar: {totalPago} dólares")
    
    print("¿Desea Continuar (SI/NO)? ")
    deseaContinuar = input()
    if (deseaContinuar.lower() != "si"):
        break
