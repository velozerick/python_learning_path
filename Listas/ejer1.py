# contar cuantas veces aparece un elemento

cultivos = ['jitomate','pepino','rabano','lechuga','pepino','pepino','rabano'] #crear lista cultivos

#buscar cunatas veces en la lista se repite pepino

buscar = 'pepino' #crear variable buscar 

contador = 0 #crear la variable contador inciando en 0

for cultivo in cultivos: #inicio de for
    if cultivo == buscar: # si la variable cultivo es igual a la variable buscar 'pepino'
        contador = contador + 1 # ir aumentando las veces que bucar se repite 
        
print(buscar, 'aparece', contador, 'veces') #imprimir cuantas veces buscar se repite







# Eliminar duplicados

print('rabano aparece',cultivos.count('rabano'), 'veces') # Buscar cuantas veces se repite rabano

#si rabano aparece mas de 1 vez eliminar las resatntes 
print(cultivos) #imprimir lista antes de ordenar
sin_duplicados = [] #Creamos una lista vacia

for cultivo in cultivos: #iniciar for
    if cultivo not in sin_duplicados: # si el cultivo no esta en la lista nueva lo agrega, 
                                      #pero a la siguente vuelta si encuentra un duplicado no lo agrega porque ya existe la lista nueva
        sin_duplicados.append(cultivo) #Agrega el cultivo en la lista nueva 
print(sin_duplicados)
