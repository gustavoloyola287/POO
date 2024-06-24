#Clase hija Alimento

from producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion
    
    def getFecha_expiracion(self):
        return self.fecha_expiracion
        
    def mostrar_fecha_expiracion(self):
        print("vence: ",self.fecha_expiracion)  
