from Usuario import Usuario
from Cliente import Cliente
from ConsultarOferta import ConsultarOferta
from Inventario import Inventario

class Trabajador(Usuario):
    def __init__(self,  nombre:str, id:int, edad:int, correo:str, celular:int, datosCliente:Cliente):
        super(). __init__(nombre, id, edad, correo)
        self.celular = celular
        self.datosCliente = datosCliente

    def UsuarioConAcceso():
        usu = "El usuario con acceso es david"
        return usu
    def EnviarOferta():
        envi = "oferta enviada con exito"
        return envi

objetoInventario = Inventario("desarrollar", 101792)
objetoConsultarOferta = ConsultarOferta("peperoni", 3128672, "23 abril 2025", objetoInventario)
objetoCliente = Cliente("benjamin", 380232, 32, "xioma@23.com", objetoConsultarOferta)
objetoTrabajador = Trabajador("benjamin", 380232, 32, "xioma@23.com", 3124254232, objetoCliente)