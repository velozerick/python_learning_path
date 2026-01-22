"""
print('Ingrese contraseña para acceder')

cont = "si"

while cont == "si":
	data = input("Escriba la contraseña  ")
	
	if data == "veloz3r2505":
		print("Contraseña correcta puede acceder")
	else:
		print("Contraseña incorrecta")

	cont = input("Desea volver a intentar? (si/no)")

print("Fin del programa")
"""

# OPTIMIZACION DE CODIGO 

print ('Ingrese contraseña para acceder') 

password_correcta = "veloz3r2505" # declarar variable para contraseña correcta
continuar = "si" # declarar variable para while

while continuar == "si": # inincio de while
	password_ingresada = input("Escriba la contraseña: ") # pedir a ususario escribir contraseña
	
	if password_ingresada == password_correcta: # verificacion de contraseña
		print('Contraseña correcta puede continuar')
		continuar = "no" # Termina el while 
	else:
		print("Contraseña incorrecta")
	
		continuar = input("Desea volver a intentar? (si/no): ").strip().lower() # preguntar al ususario si desea volver a intentar con el uso de strip y lower sin importar mayusculas o minusculas en la entrada

print("Fin del programa")
