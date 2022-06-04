
from Usuario import Usuario
from Inventario import Inventario
from ConsultarOferta import ConsultarOferta


class Cliente(Usuario):
    def __init__(self, nombre:str, id:int, edad:int, correo:str, consultarOfertas: ConsultarOferta):
        super(). __init__(nombre, id, edad, correo)
        self.consultarOfertas = consultarOfertas
    
    def ResivirOfertas():
        ser = "Oferta resivida"
        return ser

objetoUsuario = Usuario("benjamin", 380232, 32, "xioma@23.com")
objetoInventario = Inventario("desarrollar", 101792)
objetoConsultarOferta =ConsultarOferta("peperoni", 3128672, "23 abril 2025", objetoInventario)
objetoCliente = Cliente("benjamin", 380232, 32, "xioma@23.com", objetoConsultarOferta)