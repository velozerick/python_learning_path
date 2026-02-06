'''
For sirve para recorrer una coleccion de datos , uno por uno, 
no repite x veces , es iterar sobre algo que y existe 

una lista
tupla 
diccionario
set
string

el while yo controlo el esado, decido cuadno termina
y el for python controla el avance y yo solo decido que recorrer


usaremos range()

es algo que genera numeros uno por uno 

range(5)  genera 0 1 2 3 4
range (1, 4) genera 1 2 3

'''

'''
for variable in algo:
bloque 




for i in range(5):
    if i ==3:
        print('llegue al 3')
    else:
        print('valor:', i)



for numero in range(10):
    if numero % 2 == 0:
        print(numero, 'par')
    else:
        print(numero, 'impar')
'''

# for con rango controlado

for control in range(1, 11):
    if control > 5:
        print(control)


print('ejercicio for continue')

# for continue

for cont in range(1, 11):
    if cont % 2 == 0:
        continue
    else:
        print(cont, 'es impar')



#for break

print('ejercicio for break')

for bre in range(1 ,11):
    if bre == 7:
        print('llegue al 7, paro')
        break



#for contador
print('Ejercicio contador')
contador = 0

for i in range(1, 11):
    if i % 2 ==0:
        contador = contador + 1
print(contador)



# for control de acceso

# En un sistema , los usuarios tienen IDs del 1 al 15, los usuarios con ID multiplo de 3 tienen acceso permitido, cuantos usuarios tienen acceso

print('ejercicio acceso')

usuarios = 0

for uid in range(1, 16):
    if uid % 3 == 0:
        usuarios = usuarios + 1
print(usuarios)