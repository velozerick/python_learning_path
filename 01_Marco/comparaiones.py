# =========================================
# CLASE 06: COMPARACIONES EN PYTHON
# =========================================

# -----------------------------------------
# TEORÍA
# -----------------------------------------
# Comparar significa revisar si un valor es:
# - igual a otro
# - diferente de otro
# - mayor que otro
# - menor que otro
#
# El resultado de una comparación siempre será:
# True  -> verdadero
# False -> falso
#
# Esto es muy importante porque después se usa
# en condicionales como if, pero ahorita solo
# vamos a aprender a comparar.


# -----------------------------------------
# EJEMPLOS BÁSICOS
# -----------------------------------------

print(5 == 5)   # True  -> 5 es igual a 5
print(5 == 3)   # False -> 5 no es igual a 3

print(5 != 3)   # True  -> 5 es diferente de 3
print(5 != 5)   # False -> 5 no es diferente de 5

print(10 > 5)   # True  -> 10 es mayor que 5
print(5 > 10)   # False -> 5 no es mayor que 10

print(3 < 8)    # True  -> 3 es menor que 8
print(8 < 3)    # False -> 8 no es menor que 3

print(10 >= 10) # True  -> 10 es mayor o igual a 10
print(7 >= 5)   # True  -> 7 es mayor o igual a 5
print(4 >= 9)   # False -> 4 no es mayor o igual a 9

print(5 <= 5)   # True  -> 5 es menor o igual a 5
print(3 <= 8)   # True  -> 3 es menor o igual a 8
print(9 <= 2)   # False -> 9 no es menor o igual a 2


# -----------------------------------------
# IMPORTANTE
# -----------------------------------------
# No confundas:
#
# =   -> asignación
# ==  -> comparación
#
# Ejemplo:
numero = 10
print(numero == 10)  # True


# -----------------------------------------
# COMPARACIONES CON VARIABLES
# -----------------------------------------

a = 15
b = 20

print("Valor de a:", a)
print("Valor de b:", b)

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# -----------------------------------------
# COMPARACIONES CON INPUT
# -----------------------------------------
# Como input() devuelve texto, si queremos
# comparar números correctamente, debemos
# convertir con int().

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

print("¿Son iguales?", numero1 == numero2)
print("¿Son diferentes?", numero1 != numero2)
print("¿El primero es mayor?", numero1 > numero2)
print("¿El primero es menor?", numero1 < numero2)
print("¿El primero es mayor o igual?", numero1 >= numero2)
print("¿El primero es menor o igual?", numero1 <= numero2)


# -----------------------------------------
# PRÁCTICA GUIADA
# -----------------------------------------
# Cambia los valores de estas variables y
# observa cómo cambia el resultado.

edad_marco = 22
edad_erick = 22

print("¿Marco tiene la misma edad que Erick?", edad_marco == edad_erick)
print("¿Marco tiene diferente edad que Erick?", edad_marco != edad_erick)
print("¿Marco es mayor que Erick?", edad_marco > edad_erick)
print("¿Marco es menor que Erick?", edad_marco < edad_erick)


# -----------------------------------------
# EJERCICIO 1
# -----------------------------------------
# Instrucciones:
# 1. Crea dos variables llamadas numero_a y numero_b
# 2. Asígnales valores numéricos
# 3. Imprime:
#    - si son iguales
#    - si son diferentes
#    - si numero_a es mayor
#    - si numero_a es menor

# Escribe tu código aquí abajo:


# -----------------------------------------
# EJERCICIO 2
# -----------------------------------------
# Instrucciones:
# 1. Pide al usuario dos números con input()
# 2. Convierte ambos a int
# 3. Imprime:
#    - si el primer número es mayor
#    - si el segundo número es mayor
#    - si ambos son iguales

# Escribe tu código aquí abajo:


# -----------------------------------------
# EJERCICIO 3
# -----------------------------------------
# Instrucciones:
# 1. Crea dos variables:
#    precio_producto_1
#    precio_producto_2
# 2. Asígnales valores
# 3. Compara:
#    - si cuestan lo mismo
#    - si el primero cuesta más
#    - si el segundo cuesta más

# Escribe tu código aquí abajo:


# -----------------------------------------
# EJERCICIO 4
# -----------------------------------------
# Instrucciones:
# 1. Pide al usuario:
#    - su edad
#    - la edad de su hermano o amigo
# 2. Convierte ambas a int
# 3. Imprime:
#    - si tienen la misma edad
#    - si el usuario es mayor
#    - si el usuario es menor

# Escribe tu código aquí abajo:


# -----------------------------------------
# EJERCICIO 5
# -----------------------------------------
# Instrucciones:
# 1. Crea dos variables:
#    distancia_casa
#    distancia_trabajo
# 2. Asigna valores numéricos
# 3. Imprime comparaciones con:
#    ==, !=, >, <, >=, <=

# Escribe tu código aquí abajo: