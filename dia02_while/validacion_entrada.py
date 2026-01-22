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
