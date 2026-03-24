class Car:
    def __init__(self, marca,modelo, color):
        
        #Atributos
        self.brand = marca
        self.modelo = modelo
        self.color = color

    #Metodos
    def acelerar(self):
        print(f"El {self.marca} está acelerando")
    
    def frenar(self):
        print(f"El {self.marca} está frenando")

#Crear objeto

my_car = Car("Toyota","Corolla", "red")

my_car.acelerar

