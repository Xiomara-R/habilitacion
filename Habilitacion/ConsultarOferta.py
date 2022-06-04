from Inventario import Inventario


class ConsultarOferta():
    def __init__(self, nombre:str, precio:int, fechas:str, inventario: Inventario):
        self.nombre = nombre
        self.precio = precio
        self.fechas = fechas
        self.inventario = inventario
    
    def ConsultarSolicitud():
        con = "Solicitud consultada"
        return con

    def ConsultarOferta():
        s = "oferta consultada"
        return s

    def Validacion():
        val = "validado"
        return val
    
    def EnviarOferta():
        en = "oferta enviada"
        return en

objetoInventario = Inventario("desarrollar", 101792)
objetoConsultarOferta = ConsultarOferta("peperoni", 3128672, "23 abril 2025", objetoInventario)

    