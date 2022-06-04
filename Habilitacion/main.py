from Usuario import Usuario
from Cliente import Cliente
from ConsultarOferta import ConsultarOferta
from Inventario import Inventario
from Trabajador import Trabajador
from OrdenDeCompra import OrdenDeCompra

def main(Cliente, ConsultarOferta, Inventario, OrdenDeCompra, Trabajador, Usuario):
    objetoUsuario = Usuario("benjamin", 380232, 32, "xioma@23.com")
    objetoInventario = Inventario("desarrollar", 101792)
    objetoConsultarOferta = ConsultarOferta("peperoni", 3128672, "23 abril 2025", objetoInventario)
    objetoCliente = Cliente("benjamin", 380232, 32, "xioma@23.com", objetoConsultarOferta)
    objetoTrabajador = Trabajador("benjamin", 380232, 32, "xioma@23.com", 3124254232, objetoCliente)
    objetoOrdenDeCompra = OrdenDeCompra("23 mayo", "servicio web", 1, objetoCliente)


objetoUsuario = Usuario("benjamin", 380232, 32, "xioma@23.com")
objetoInventario = Inventario("desarrollar", 101792)
objetoConsultarOferta = ConsultarOferta("peperoni", 3128672, "23 abril 2025", objetoInventario)
objetoCliente = Cliente("benjamin", 380232, 32, "xioma@23.com", objetoConsultarOferta)
objetoTrabajador = Trabajador("benjamin", 380232, 32, "xioma@23.com", 3124254232, objetoCliente)
objetoOrdenDeCompra = OrdenDeCompra("23 mayo", "servicio web", 1, objetoCliente)

funcionmain = main(Cliente, ConsultarOferta, Inventario, OrdenDeCompra, Trabajador, Usuario)