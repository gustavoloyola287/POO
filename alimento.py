#Clase hija Alimento

from producto import Producto

class Alimento(Producto):
    
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion
        
        
    def get_fecha_expiracion(self):
        return self.fecha_expiracion
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(self.get_fecha_expiracion())

fecha_expiracion = input("Ingrese fecha de expiracion:  : ") 

mi_alimento = Alimento(nombre, fecha_expiracion)

mi_alimento.mostrar_informacion()
