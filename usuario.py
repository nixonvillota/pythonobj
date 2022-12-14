class Usuario:
    def __init__(self, nombre, apellido, cedula, edad=0):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad

    def getNombre(self):
        return self.nombre 

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getCedula(self):
        return self.cedula

    def setCedula(self, cedula):
        self.cedula = cedula

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def detalle(self):
        return "Usuario: \nnombre: "+self.nombre+" \napellido: "+self.apellido+" \ncedula: "+self.cedula+" \nedad: "+ str(self.edad)
