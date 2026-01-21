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
	


"""
La identacion o el tab, tabulado, es fundamental en python  , son los espacios al inicio de la linea
se usa para saber que lineas pertenecen a un bloque (if,whle,etc)

"""


#En py los dos puntos : indican que empieza un bloque de codigo 


edad = 20

if edad >= 18:
	#Estas lineas estan indentadas
	#Por lo tanto pertnecen al if
	print("Eres mayor de edad")
	print("puedes continuar")


#Aqui ya no hay indentacion 
# Esto significa que esta linea no pertenece al if
print("Fin del programa") 
