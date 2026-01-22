print("Calculadora el VELOZ")

opcion = "si"

while opcion == 'si':

	num1 = int(input('Escribe un numero ')) 
	num2 = int(input('Escribe otro numero '))
	
	operacion = input('¿Que operacion deseas realizar? ')
	
	if operacion == "suma":
		print("El resultado es ", num1 + num2)
	else:
		print('prueba lista')
	
	opcion = input('Deseas continuar? (si/no)')
print('Hasta luego')
