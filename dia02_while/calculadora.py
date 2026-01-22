print("Calculadora el VELOZ")

opcion = "si"

while opcion == 'si':

	num1 = int(input('Escribe un numero ')) 
	num2 = int(input('Escribe otro numero '))
	
	operacion = input('¿Que operacion deseas realizar? ')
	
	if operacion == "suma":
		print("El resultado es ", num1 + num2)
	elif operacion == "resta":
		print("El resultado es ", num1 - num2)
	elif operacion == "multiplicacion":
		print("El resultado es ", num1 * num2)
	elif operacion == "division":
		print("El resultado es ",num1 / num2)
	else:
		print("Elige suma, resta, multiplicacion o division")
	
	opcion = input('Deseas continuar? (si/no)')
print('Hasta luego')
