# Una funcion es un bloque de codigo con nombre, que permite hacer UNA cosa 

#Syntaxis de la funcion

def nombre_de_la_funcion():
    #aqui va el codigo 
    nombre_de_la_funcion()


def saludar(): #definir la funcion  mas el nombre de la funcion
    print('hello there')
saludar() # ejecutar la funcion

'''
def mostrar_mensaje():
    mensaje = input('Quien eres? ')
    print('hola ',mensaje)
mostrar_mensaje()
'''

def saludar_usuario(nombre): # dentro del paraentesis declaramos una variable local "se le llama parametro"
    print('hola', nombre)

saludar_usuario('Erick')
saludar_usuario('General Kenobi')
saludar_usuario('mundo')






# EJERCICIO 1 RETORNO + PARAMETROS
def fahrenheit_to_celsius (f): # creamos la funcion fahrenheit_to_celsius y le asignamos el paametro f 
    return (f -32) * 5 / 9 # return sirve para terminar la funcion y enviar el valor hacia afuera
   

c1=(fahrenheit_to_celsius(77)) # guardar el resultado con el valor asignado en una variable 
c2=(fahrenheit_to_celsius(95))
c3=(fahrenheit_to_celsius(50))

print('77 grados fahrenhait a celsius es:',c1,'° grados celsius ') # imprimir el resultado
print('95 grados fahrenhait a celsius es:',c2,'° grados celsius ') # imprimir el resultado
print('50 grados fahrenhait a celsius es:',c3,'° grados celsius ') # imprimir el resultado