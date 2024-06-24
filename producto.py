#Creación de la clase Producto y sus atributos

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_informacion(self):
        print("El producto se llama: ",self.nombre)
        print("cuesta: ",self.precio)
        print("stock: ",self.cantidad)
        
# class Electronico(Producto):
#     def __init__(self, nombre, precio, cantidad, marca, modelo):
#         super().__init__(nombre, precio, cantidad)
#         self.marca = marca
#         self.modelo = modelo
        
#     def mostrar_electronico(self):
#         print("marca: ",self.marca,"\nmodelo: ",self.modelo)         

# electronico = Electronico("televisor","1000","11","noblex","ytz")
# electronico.mostrar_informacion()
# electronico.mostrar_electronico()
      