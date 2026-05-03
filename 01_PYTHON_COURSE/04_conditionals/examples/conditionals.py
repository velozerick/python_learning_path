#---------------------------------------------------------#
#                IF STATEMENTS (CONDICIONALES)            #
#---------------------------------------------------------#

"""
Las sentencias IF te permiten examinar el estado actual de un programa 
y responder apropiadamente a ese estado.
"""

###---PRUEBAS CONDICIONALES---###

# El corazón de cada sentencia if es una expresión que puede ser True o False.
# Esto se llama prueba condicional.

car = 'bmw'
print(car == 'bmw')  # True: El operador == pregunta si los valores son iguales.
print(car == 'audi') # False

# La comparación ignora mayúsculas si usamos métodos:
user = 'Admin'
print(user.lower() == 'admin') # True


###---OPERADORES DE COMPARACIÓN---###

"""
Igual que:            ==
No es igual a:        !=
Mayor que:            >
Menor que:            <
Mayor o igual que:    >=
Menor o igual que:    <=
"""

age = 18
if age >= 18:
    print("Ya puedes votar.")


###---COMPROBAR MÚLTIPLES CONDICIONES---###

# AND: Ambas deben ser True
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False

# OR: Al menos una debe ser True
print(age_0 >= 21 or age_1 >= 21)  # True


###---LA ESTRUCTURA IF-ELIF-ELSE---###

"""
Se usa cuando necesitas manejar más de dos situaciones posibles.
Python ejecuta solo un bloque en la cadena.
"""

edad = 12

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 25
elif edad < 65:
    precio = 40
else:
    precio = 20

print(f"Tu entrada cuesta ${precio}.")


###---COMPROBAR SI UN VALOR ESTÁ EN UNA LISTA---###

# Aunque veremos listas a fondo luego, es común usar 'in' para verificar:
usuarios_baneados = ['andrew', 'carolina', 'david']
usuario = 'marie'

if usuario not in usuarios_baneados:
    print(f"{usuario.title()}, puedes publicar si deseas.")


#---------------------------------------------------------#
#                EJERCICIOS PARA PRACTICAR                #
#---------------------------------------------------------#

#--- EJERCICIO 1: Prueba de Color de Alien ---
# Crea una variable 'alien_color' y asígnale 'verde', 'amarillo' o 'rojo'.
# Escribe un if para comprobar si el color es verde. Si lo es, imprime 
# que el jugador ganó 5 puntos.

alien_color = None
# Tu código aquí:


#--- EJERCICIO 2: Etapas de la vida ---
# Escribe una cadena if-elif-else que determine la etapa de la vida de una persona.
# Pide la edad con un input() y conviértela a int().
# Si la edad es menor de 2, es un bebé.
# Si tiene entre 2 y 4 (sin incluirlo), es un infante.
# Si tiene entre 4 y 13 (sin incluirlo), es un niño.
# Si tiene entre 13 y 20 (sin incluirlo), es un adolescente.
# Si tiene 20 o más, es un adulto.

# edad_persona = 
# Tu código aquí:


#--- EJERCICIO 3: Login de Usuario ---
# Crea una variable 'username' usando input().
# Si el nombre es 'admin', imprime "Hola admin, ¿quieres ver el reporte de hoy?"
# Si es cualquier otro nombre, imprime "Hola [nombre], gracias por entrar de nuevo."

# username = 
# Tu código aquí: