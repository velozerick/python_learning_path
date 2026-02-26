# clase servicio
# atributos:  nombre, precio
# Metodos:  descripcion(), , aplicar_descuento
#objetos: s1= soporte, s2=CCTV, s3=redes

class Servicio:
    # __init__ se ejecuta cuando creas un objeto
    def __init__ (self,nombre,precio):
        #Atributos datos que tiene el objeto
        self.nombre = nombre
        self.precio = precio

    #Metodo: accion que el objeto puede hacer
    def descripcion(self):
        return f"{self.nombre} - {self.precio}"
    
    #metodo con parametro extra
    def aplicar_descuento(self,porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento

#Objetos, creados desde la clase
s1 = Servicio("soporte",250)
s2 = Servicio("CCTV", 890)
s3 = Servicio("redes", 430)

#Uso de metodos
print(s1.descripcion())
print(s2.descripcion())
print(s3.descripcion())


#descuento a cctv
s2.aplicar_descuento(10)

print("despues del descuento: ")
print(s2.descripcion())












