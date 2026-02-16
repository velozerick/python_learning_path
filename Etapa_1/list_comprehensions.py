#Es una forma correcta, compacta y elegante de crear listas 

#En lugar de hacer esto ;

numeros = [1,2,3,4]
dobles = []

for n in numeros :
    dobles.append(n * 2)

#Podemos hacer esto 
dobles = [n * 2 for n in numeros]
print(dobles)

#expresion for elemento in iterable

#Por cada elemento en esta coleccion, genera esto 





pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)

#Hacemos esto 
pares = [n for n in numeros if n % 2 == 0]
#expresion for elemento in iterable if condicion

print(pares)

########################################################

print("\n Ejercicio 1\n")
#Ejercicio 1
nombres = ["Erick","Alejandra","Luis","Ignacio"]
result = [name.lower() for name in nombres ]
print(result)