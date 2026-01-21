opcion = "s"

while opcion == "s":
	nombre = input('escribe tu nombre ')
	edad = int(input('Escribe tu edad '))
	licencia = input('tienes licencia (si/no) ')

	print('Bienvenid@', nombre)

	if edad >= 18 and licencia == "si":
		print('Genial puedes manejar')
	elif edad >= 18 and licenica == "no":
		print('Puedes sacar una licencia')
	else:
		print('no tienes la edad suficiente')
	
	opcion = input('quieres intentar de nuevo? (s/n)')
	
