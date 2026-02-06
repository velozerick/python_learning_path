#Listas



#posicion      0          1         2        3
cultivos = ['jitomate','pepino','rabano','lechuga']
'''
print(cultivos[3])
print(cultivos[0])
print(cultivos[2])

#Agregar elementos a la lista

cultivos.append('camote')
cultivos.append('cebolla')
print(cultivos)


#Modificar elementos en una lista
cultivos[1] = 'pepino_chico'
print(cultivos)

#Saber cuantos elementos hay 

cantidad =len(cultivos)
print(cantidad)

#Eliminar datos de un alista
del cultivos[5]
print(cultivos)





# for en listas
for cultivos in cultivos:
    print(cultivos)

    

#Recorrer listas
# Significa ver un elemento por elemento, en orden de inicio a fin 

for cultivos in cultivos:
    print(cultivos)


'''
#Buscar elementos en una lista

buscando = 'pepino'
encontrado = False

for cultivo in cultivos:
    if cultivo == buscando:
        encontrado = True
print(encontrado)


#Otra forma mas clara

find = 'camote'

for cultivo in cultivos:
    if cultivo == find:
        print('existe el elemento',find)
        break
else:
        print('no existe el elemento',find)


cultivos.append('camote')
print(cultivos)

find = 'camote'

for cultivo in cultivos:
    if cultivo == find:
        print('existe el elemento',find)
        break
else:
        print('no existe el elemento',find)