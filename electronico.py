#Clase hija Electrónico

from producto import Producto

class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo
        
    def mostrar_electronico(self):
        super().mostrar_informacion
        print("marca: ",self.marca,"\nmodelo: ",self.modelo)   
