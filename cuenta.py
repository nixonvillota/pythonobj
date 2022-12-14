from usuario import Usuario
class Cuenta(Usuario):
    
    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado=0):
        super().__init__(nombre, apellido, cedula, edad)
        self.dineroAhorrado = dineroAhorrado

    
    def getDineroAhorrado(self):
        return self.dineroAhorrado 

    def setDineroAhorrado(self, dineroAhorrado):
        self.dineroAhorrado = dineroAhorrado

    def detalle(self):
        return super().detalle() + "\ncantidad dinero ahorrado: "+ self.formatoDinero(self.dineroAhorrado)
    
    def ingresar(self, cantidad):
        if cantidad<0:
            return "La cantidad ingresada Debe ser mayor a cero"
        self.dineroAhorrado += cantidad
        return "Consignación exitosa\nSu nuevo saldo es de: "+ self.formatoDinero(self.dineroAhorrado)
         
    def retirar(self, cantidad):
        if cantidad<0:
            return "La cantidad a retirar debe ser mayor que cero"
        if self.dineroAhorrado < cantidad:
            return "La cantidad a retirar supera a la cantidad ahorrada"
        self.dineroAhorrado -= cantidad
        return "Retiro exitoso\nSu nuevo saldo es de: "+ self.formatoDinero(self.dineroAhorrado)
         
    
    def formatoDinero(self,numero):
        return ('$ {:,.2f}'.format(numero).replace(",", "@").replace(".", ",").replace("@", "."))
            