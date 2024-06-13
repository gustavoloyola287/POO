#Creación de la clase Producto y sus atributos

class Producto():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_informacion(self):
        print("El producto se llama: ",self.nombre)
        print("cuesta: ",self.precio)
        print("stock: ",self.cantidad)

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion
       
        
    def mostrar_expiracion(self):
        print("vence: ",self.fecha_expiracion)  
        
  
alimento = Alimento("harina","70","12","12-12-24")     
alimento.mostrar_informacion()
alimento.mostrar_expiracion()     