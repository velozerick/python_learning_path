# Generar un reporte de gastos de mi negocio
nombre = input('Inserta tu Nombre: ')
dinero_inicial = int(input('Cual es tu capital inicial: '))
gasto_en_comida = int(input('ingresa tu cantidad gastada en comida: '))
gasto_en_trasporte = int(input('Ingresa la cantidad gastada en trasporte: '))
gastos_varios = float(input('Ingresa tus demas gastos sueltos: '))

total_de_gastos = gasto_en_comida + gasto_en_trasporte + gastos_varios
print("Tu gran total gastado es: ", total_de_gastos)
print(f"Tu total es: {total_de_gastos}")

dinero_restante = dinero_inicial - total_de_gastos
print('Tu restante despues de tus gastos es: ', dinero_restante)
print(f"Te queda solo esto pobre: {dinero_restante}")
print(f"hola {nombre} total gastado {total_de_gastos} tu dinero restante es {dinero_restante}")