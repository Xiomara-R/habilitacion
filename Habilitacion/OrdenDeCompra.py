from Trabajador import Trabajador
from Cliente import Cliente
from ConsultarOferta import ConsultarOferta
from Inventario import Inventario

class OrdenDeCompra:
    def __init__(self, fechaLimite:str, producto:str, cantidadProducto:int, cliente: Cliente):
        self.fechaLimite = fechaLimite
        self.producto = producto
        self.cantidadProducto = cantidadProducto
        self.cliente = cliente
    
    def VerificarOferta():
        ofertaVerificada = "oferta verificada"
        return ofertaVerificada
    def EnviarOrdenCompra():
        orden = "Orden enviada compra"
        return orden


objetoInventario = Inventario("desarrollar", 101792)
objetoConsultarOferta = ConsultarOferta("peperoni", 3128672, "23 abril 2025", objetoInventario)
objetoCliente = Cliente("benjamin", 380232, 32, "xioma@23.com", objetoConsultarOferta)
objetoTrabajador = Trabajador("benjamin", 380232, 32, "xioma@23.com", 3124254232, objetoCliente)
objetoOrdenDeCompra = OrdenDeCompra("23 mayo", "servicio web", 1, objetoCliente)
