nombre = input('Como te llamas? ' )
edad = int(input('Que edad tienes? '))
licencia = input('Tienes licencia de conducir? (si/no) ')

print('Bienvendi@ ',nombre )



if edad >= 18 and licencia == 'si':
	print('Genial, puedes manejar legalmente')

elif   licencia == 'no' and edad >= 18:
		print('Puedes sacar una licencia')

else:
	print('Uy, aun no tienes la edad suficiente , regresa cuando seas mayor')
