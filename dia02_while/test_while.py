opcion = "si"

while opcion == "si":
	nombre = input('¿Como te llamas? ' )
	edad = int(input('¿Cual es tu edad? '))
	
	if edad  <= 13:
		print(nombre, "Eres un niño")
	
	elif edad <= 17:
		print(nombre, "Eres un adolescente")
	
	elif edad >= 18 and edad <= 64:
		print(nombre, "Eres adulto")

	else:
		print(nombre, "Eres adulto mayor")

	opcion = input("¿Quieres evauluar nuevamente? (si/no)")


print("Fin del programa")
