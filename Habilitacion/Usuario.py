class Usuario:
    def __init__(self, nombre:str, id:int, edad:int, correo:str):
        self.nombre = nombre 
        self.id = id
        self.edad = edad
        self.correo = correo


    def CreanUsuario():
        crea = "Usuario creado con exito"
        return crea
    
    def ActualizarUsuarios():
        act = "Usuario actualizado con exito"
        return act


objetoUsuario = Usuario("benjamin", 380232, 32, "xioma@23.com")