#Es una forma correcta, compacta y elegante de crear listas 

#En lugar de hacer esto ;

numeros = [1,2,3,4]
dobles = []

for n in numeros :
    dobles.append(n * 2)

#Podemos hacer esto 
dobles = [n * 2 for n in numeros]
print(dobles)