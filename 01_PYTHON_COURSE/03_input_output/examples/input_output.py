#---------------------------------------------------------#
#               INPUT Y OUTPUT DE DATOS                  #
#---------------------------------------------------------#

###---SALIDA DE DATOS (OUTPUT)---###

"""
Ya hemos usado print(), que es la forma estándar de mostrar 
información en la consola.
"""

print("Hola Mundo") # Output directo de string
x = 10
print(x) # Output de una variable


###---ENTRADA DE DATOS (INPUT)---###

"""
La función input() permite que el usuario escriba algo.
IMPORTANTE: Todo lo que entra por input() Python lo lee como STRING.
"""

# 1. Entrada básica
usuario = input("Escribe tu nombre de usuario: ")
print(f"Bienvenido, {usuario}!")


# 2. Entrada de números (Casting)
"""
Si queremos hacer cálculos con un input, debemos convertirlo 
de string a int o float, de lo contrario dará error.
"""

# Ejemplo de suma fallida (sin convertir):
edad_str = input("Introduce tu edad: ")
# edad_futura = edad_str + 1  <-- Esto daría error: String + Int NO se puede.

# Ejemplo correcto (con conversión):
edad = int(input("¿Cuántos años tienes? ")) # Convertimos la entrada a Entero
print(f"El próximo año tendrás {edad + 1} años.")


###---EJERCICIOS PARA COMPLETAR---###

#--- EJERCICIO A: Entrada de Flotantes ---
# Instrucción: Pide al usuario el precio de un café y guárdalo como float.

precio_cafe = None # Usa float(input(...))
# print(f"El café cuesta ${precio_cafe}")


#--- EJERCICIO B: Calculadora de área simple ---
# Instrucción: Pide la base y la altura de un rectángulo y calcula su área.
# Recordatorio: Area = base * altura

# base = 
# altura = 
# area = 

# print(f"El área del rectángulo es: {area}")


#--- EJERCICIO C: El Limpiador de Datos ---
# Instrucción: Pide al usuario su ciudad, pero asegúrate de que se guarde 
# sin espacios extra al principio o al final y con la primera letra en mayúscula.

# ciudad_sucia = input("¿En qué ciudad vives? ")
# ciudad_limpia = None # Usa .strip() y .title()

# print(f"Vives en: {ciudad_limpia}")