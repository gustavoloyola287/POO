#Creación de la clase Producto y sus atributos

class Producto():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar_producto(self):
        print("El producto se llama: ",self.get_nombre(),"y cuesta: ",self.get_precio(),"pesos")
    
nombre = input("Ingrese nombre del producto: ")
precio = input("Ingrese precio del producto: ")
cantidad = input("Ingrese cantidad del producto: ")

mi_producto = Producto(nombre, precio, cantidad)
mi_producto.mostrar_producto()

#print(mi_producto.mostrar_producto())
    