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

    def getNombre(self):
        return self.nombre 

    def setDineroAhorrado(self, DineroAhorrado):
        self.DineroAhorrado = DineroAhorrado

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

class Cuenta(Usuario):

    dineroAhorrado = 0
    
    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad)
        self.dineroAhorrado = dineroAhorrado

    
    def getDineroAhorrado(self):
        return self.dineroAhorrado 

    def setDineroAhorrado(self, dineroAhorrado):
        self.dineroAhorrado = dineroAhorrado

    def detalle(self):
        return super().detalle() + "\ncantidad dinero ahorrado: "+ str(self.dineroAhorrado)
    
    def ingresar(self, cantidad):
        if cantidad>0:
            self.dineroAhorrado += cantidad
            return "Consignación exitosa\nSu nuevo saldo es de: $"+ str(self.dineroAhorrado)
        else:
            return "La cantidad ingresada no es valida" 
    
    def retirar(self, cantidad):
        if cantidad>0:
            self.dineroAhorrado -= cantidad
            return "Retiro exitoso\nSu nuevo saldo es de: $"+ str(self.dineroAhorrado)
        else:
            return "La cantidad ingresada no es valida" 
            
        
class Beneficio(Cuenta):

    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad, dineroAhorrado)
        self.porcentaje = 0.05

    def validarUsuarioJoven(self):
        if int(self.edad)>=18 & int(self.edad)<28:
            return True
        else:
            return False
    
    def mostrar(self):
        ban = self.validarUsuarioJoven()
        if ban == True:
            intereses = int(self.dineroAhorrado) * self.porcentaje
            total = int(self.dineroAhorrado) + intereses
            return "SubTotal: $"+ str(self.dineroAhorrado)+"\nInterese generados: $"+ str(intereses) +"\nTotal: $"+ str(total)
        else:
            return "SubTotal: $"+ str(self.dineroAhorrado)+"\nInterese generados: $0.0\nTotal: $"+ str(self.dineroAhorrado)

persona = Beneficio("andres", "mafla","1193570753", 23, 1000000) 
print("-----------------------------------")
print(persona.detalle())
print("-----------------------------------")
print(persona.ingresar(100000))
print("-----------------------------------")
print(persona.retirar(50000))
print("-----------------------------------")
print(persona.retirar(-8))
print("-----------------------------------")
print(persona.ingresar(-10000))
print("-----------------------------------")
print(persona.mostrar())

