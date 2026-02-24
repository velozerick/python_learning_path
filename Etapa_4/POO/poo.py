"""
 CLASE

Una clase es un molde
un plano, una definicion , no es algo real todavia , es como el plano arquitectonico de una casa

OBJETO

Son las caracteristicas de un objeto

METODOS

son acciones que el objeto puede hacer 

ATRIBUTOS

Un atribuito es un dato que pertenece a cada objeto

"""


# Esto es una CLASE (el molde)

class Cultivo:
    
    #Este es el METODO CONSTRUCTOR
    #se ejecuta cuando creamos un objeto
    def __init__ (self, nombre, caja): # __init__ significa initialize , sirve para inicializar los atributos del objeto         simepre va primero el parametro self
        #

        #Estos son ATRIBUTOS
        #son datos que pertenecen a cada objeto
        self.nombre = nombre
        self.caja = caja
        self.riegos = 0

    #Esto es un METODO
    #Acciones que el objeto puede hacer    simepre lo que el objeto haga va en funciones

    def regar(self):
        self.riegos += 1
        print(f"Regaste {self.nombre}. Total riegos: {self.riegos}")


#Aqui estamos creando OBJETOS 

cultivo1 = Cultivo("jitomate", 2) #caja 2
cultivo2 = Cultivo("Cilantro",7) #caja 7

#Usamos el METODO del objeto
cultivo1.regar()
cultivo1.regar()







#crear clase jugador 
class Jugador:

    def __init__ (self, nombre, vida, poder_ataque):

        #ATRIBUTOS
        self.nombre = nombre
        self.vida = vida
        self.poder_ataque = poder_ataque
        

    #METODOS
    def recibir_golpe (self,cantidad):
        self.vida -= cantidad

        if self.vida < 0:
            self.vida = 0
            print(f"lo siento {self.nombre}. has muerto")
    
    def atacar(self, otro_jugador):
        otro_jugador.recibir_golpe(self.poder_ataque)
        print(f"{self.nombre} atacó a {otro_jugador.nombre}")


j1 = Jugador("Steve",10 ,5)
j2 = Jugador("Creeper",10,8)

j1.atacar(j2)
j1.atacar(j2)



