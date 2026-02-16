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
nombres = ["Erick","Alejandra","Luis","Ignacio"] #Crear la lista de nombres 
result = [name.lower() for name in nombres ] # crear lista result , por cada name quiero generar su version en minusculas, la expresion es = que quiero contruir con cada elemento
print(result)
# de cierta manera se puede leer asi , primero se lee for despues condiciones y al final la expresion 







print("\n ------Ejercicio 2------ \n")
#Ejercicio 2 


usuarios = [
    {"username": "erick", "email": "erick@mail.com", "activo": True},
    {"username": "ana", "email": "ana@mail.com", "activo": False},
    {"username": "luis", "email": "luis@mail.com", "activo": True},
    {"username": "maria", "email": "maria@mail.com", "activo": False},
]


def obtener_usuarios_activos(usuarios):
    '''
    user_act = [user for user in usuarios if user["activo"] == True ]
    return user_act
    '''
    return [user["username"].upper() for user in usuarios if user["activo"]]
user_lis = obtener_usuarios_activos(usuarios)
print("Los usuarios activos son:",user_lis)


def obtener_email(usuarios):
    return [user["email"].lower() for user in usuarios if not user["activo"]]
email_list = obtener_email(usuarios)
print ("Email de los usuarios no activos: ", email_list)

