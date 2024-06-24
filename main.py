import alimento, electronico, producto

electronico = electronico.Electronico("televisor","1000","11","noblex","ytz")
electronico.mostrar_informacion()
electronico.mostrar_electronico()

producto = producto.Producto("mesa","99", "2")
producto.mostrar_informacion()

alimento = alimento.Alimento("harina","70","12","12-12-24")     
alimento.mostrar_informacion()
alimento.mostrar_fecha_expiracion()