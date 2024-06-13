#Clase hija Electrónico

from producto import Producto

class Electronico(Producto):
    
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo
        
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    
    def mostrar_electronico(self):
        super().mostrar_producto()
        print(self.get_marca())

marca = input("Ingrese marca: ")
modelo = input("Ingrese modelo: ") 

mi_electronico = Electronico( marca, modelo)

mi_electronico.mostrar_electronico()


