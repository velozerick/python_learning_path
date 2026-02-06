# SET , es una coleccion que no repite, no tiene orden fijo


#tenemos la lista

cultivos = ['jitomate','pepino','rabano','lechuga','pepino','pepino','rabano'] #crear lista cultivos
permitidos = {'jitomate','pepino','lechuga'} #crear lista permitidos

cultivos_set = set(cultivos)
print(cultivos_set) #imprime los cultivos sin ser duplicados

# ALGO COMO ESTO PERO DE FORMA SENCILLA
'''

# Eliminar duplicados
cultivos_set = set(cultivos)
'pepino' in cultivos_set
print(cultivos_set)
print('rabano aparece',cultivos.count('rabano'), 'veces') # Buscar cuantas veces se repite rabano

#si rabano aparece mas de 1 vez eliminar las resatntes 
print(cultivos) #imprimir lista antes de ordenar
sin_duplicados = [] #Creamos una lista vacia

for cultivo in cultivos: #iniciar for
    if cultivo not in sin_duplicados: # si el cultivo no esta en la lista nueva lo agrega, 
                                      #pero a la siguente vuelta si encuentra un duplicado no lo agrega porque ya existe la lista nueva
        sin_duplicados.append(cultivo) #Agrega el cultivo en la lista nueva 
print(sin_duplicados)'''



st = {'item1','item2','item3'} #esto es un set


nuevo_cultivo = 'lechuga'

if nuevo_cultivo in permitidos:
    print('se puede sembrar')
else:
    print('no permitido')
