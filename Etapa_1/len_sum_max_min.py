# Son funciones incorporadas  y sirven para operar rapidamente sobre estructuras de datos como : 
# listas, tuplas, strings o diccionarios

#Contar registros, calcular totales , obtener valores extremos, estadistica basica , validar longitudes

#----------
# LEN()
#----------

#Devuelve cantidad de elementos

len([1,2,3]) #3
len("hola") #4


#----------
# SUM()
#----------

sum([10,20,30]) # 60


#----------
# MAX()
#----------

max([5,10,30]) #30


#----------
# MIN()
#----------

min([10,20,5])#5



#----------
# *args
#----------

#Recibe una cantidad variable de argumentos posicionales 
#(Es una forma flexible de  crear funciones cuando no sabes cuantos vaores recibiras)

def calcular_total(*precios):
    return sum(precios)



#----------
# **kwargs
#----------

#Recibe una cantidad variable de argumentos nombrados

def crear_usuario(**datos):
    return datos
