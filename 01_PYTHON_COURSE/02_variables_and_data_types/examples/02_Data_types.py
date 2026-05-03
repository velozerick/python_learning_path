#Data Types

#---------------STRING---------------#
"""
Un String es una serie de caracteres, todo dentro de "" o '', es considerado
un string 
"""
#Creamos la variable my_string

my_string = "Esto es un string"
my_other_string = 'Esto es otro string'


##MAYUSCULAS EN STRING

name = "un titulo"
print(name.title())
#Se usa para iniciar cada palabra con mayuscula
#al imprimir la variable se agrega el punto y lo que se desea haer en este caso on title(), upper(), lower(), etc.


en_mayus = "un titulo"
print(en_mayus.upper())

en_minus = "UN tiTulo"
print(en_minus.lower())



##OPERACIONES CON STRINGS

first_name = "Obi wan"
last_name = "Kenobi"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")


##ESPACIOS EN BLANCO

"""
cuando un usuario ingresa datos en una entrada puede cometer el error de dar algun espacio 
para limpiar datos con espacios usamos ".strip()"
"""

favorite_lenguaje = "  python "
print(favorite_lenguaje.strip())
print(favorite_lenguaje)

#Mas funciones como esta se veran mas adelante










###---NUMEROS---###

##ENTEROS

"""
los enteros o INT, son los numeros enteros, no decimal, no fraccion
haremos operaciones con ellos
"""

num1 = 5
num2 = 5

res = num1 + num2
print(res)


##FLOTANTES

#Tambien conocido como float

#Se les llama flotantes a los numeros con decimal

num_flt = 4.56
num_flt2 = 7.98

res = num_flt + num_flt2
print(res)


##BOOLEANOS

my_true = True
my_false = False

print(my_true)



##MULTIPLE ASSIGNMENT
x, y, z = 23, 0,21
print(y)