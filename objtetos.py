class Usuario:

    nombre = ''
    apellido = ''
    cedula = ''
    edad = 0

    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad


class Cuenta(Usuario):
    cantdinero = 0
    
    def __init__(self, cantdinero, nombre, apellido, cedula, edad):
        super().__init__(nombre, apellido, cedula, edad)
        self.cantdinero = cantdinero

    
    def __getcantdinero__(self):
        return self.cantdinero 

    def __setcantdinero__(self):
        return 


class Beneficio(Cuenta):
    interes = 0

    def __init__(self, cantdinero, nombre, apellido, cedula, edad):
        super().__init__(cantdinero, nombre, apellido, cedula, edad)
