"""
Hasta ahora el codigo asume que todo siempre sale bien , pero en la vida real

el archivo puede no existir 
puede esatr vacio
puede venir mal formateado
fallar el acceso 
"""

#try:
    #codigo que podria fallar

#except TipoDeError:
    #que hacer si falla
#else:
    #se ejecuta cuando no hubo error

#finally:
    #ejecutar algo pase lo que pase


####################################

numero = input("Escribe un numero: ")
numero_entero = int(numero)

print("El doble es: ", numero_entero * 2)
#Si el usuario escribe por ejemplo 10 el resultado sera 20 pero si escribe algo mas como hola , dara un error entonces ...

try:
    number = input("Escribe un número: ")
    number_entero = int(number)
    print("El doble es: ", number_entero)

except ValueError:
    print("Eso no es un numero valido")

else:
    print("Deberias empezar a saber que es un numero")

finally:
    ("programa terminado")


