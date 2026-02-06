# Permitidos no permitidos

cultivos = ['jitomate','pepino','rabano','lechuga','camote','pepino'] #crear lista cultivos

permitidos = ['jitomate','pepino','lechuga'] #crear lista permitidos


#crear listas vacias donde se guardaran los datos validos y no_validos
validos = []
no_validos = []

#si el cultivo esta permitido se guardara en la lista validos si no en la lista no_validos
cont_validos = 0
cont_no_validos = 0

for cultivo in cultivos:  #para cultivo en cultivos , va recorriendo la lista cultivos 
    if cultivo in permitidos:  #si cultivo esta en la lista permitido despues de revisar la lista cultivos
        if cultivo not in validos: # si cultivo no esta en la lista validos
            validos.append(cultivo) # agregamos cultivo en la lista validos 
            cont_validos = cont_validos + 1 # contamos cuantas veces se repite validos
       
            
        
    else: # entonces agegamos cultivo a los no validos , los que no estan en la lista permitidos despues de comparar
        no_validos.append(cultivo)  
        cont_no_validos = cont_no_validos + 1 # contar cuantos no validas hay 
        



print('Cultivos validos',validos)
print('Cultivos no validos',no_validos)

print('Total validos:',cont_validos)
print('Total no validos:',cont_no_validos)



