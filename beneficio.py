from cuenta import Cuenta
class Beneficio(Cuenta):

    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad, dineroAhorrado)
        self.porcentaje = 0.05

    def validarUsuarioJoven(self):
        x=int(self.edad)
        return lambda x: True if x>=18 and x<28  else False
       
    def mostrar(self):
        if self.validarUsuarioJoven()==False:
            return "SubTotal: "+ self.formatoDinero(self.dineroAhorrado)+"\nInterese generados: $0.0\nTotal: "+ self.formatoDinero(self.dineroAhorrado)

        intereses = int(self.dineroAhorrado) * self.porcentaje
        total = int(self.dineroAhorrado) + intereses
        return "SubTotal: "+ self.formatoDinero(self.dineroAhorrado)+"\nInterese generados: "+ self.formatoDinero(intereses) +"\nTotal: "+ self.formatoDinero(total)
       