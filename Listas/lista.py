#Listas

lst = []

#posicion      0          1         2        3
cultivos = ['jitomate','pepino','rabano','lechuga']

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