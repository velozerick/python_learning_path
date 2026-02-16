"""
Demostracion de funciones puras vs funciones con efectos secundarios
"""

#PURE    mismas entradas mismas salidas
#Sirve para transformar datos, calcular, validar y devolver resultados

#SIDE EFFECTS
# sirve para registrar, guardar, notificar, persisitir: por ejemplo guarda el email en una lista global o imprime un log

LOGS = [] # variable global , se modifica desde afuera 

#----------
#FUNCION PURA
#----------

def validar_usuario(username, email):
    #transformacion interna
    username_limpio = username.strip()
    email_limpio = email.strip().lower()

    errores = [] # lista local 

    #validaciones
    if len(username_limpio) < 3:
        errores.append("El username debe tener al menos 3 caracteres")

    if "@"not in email_limpio:
        errores.append("Email invalido")

    # si hay errores termina aqui
    if errores:
        return False, None, errores
    
    #si todo esat bien -> crear diccionario

    usuario = {
        "username": username_limpio,
        "email": email_limpio,
        "activo": True
    }

    return True, usuario,[]


#EFECTO SECUNDARIO

def registrar_errores(errores):
    for error in errores:
        LOGS.append(error) #esto modifica algo externo

ok,usuario,errores = validar_usuario("Erick","erickcorreo.com")

if not ok:
    registrar_errores(errores)
else:
    print("Usuario valido:" , usuario)
print("logs",LOGS)






##########################################################################3

#----------
#Ejercicio
#----------
print("\n Validacion de contraseña \n")
#Funcion pura

#Crear lista Logs[]
Logs = []

#fucion validar_password

def validar_password(password):
    #filtrar entradas
    clean_password = password.strip()

    #crear lista errores
    errores =[]

    #validaciones
    if len(clean_password) < 8:
        errores.append("La contraseña debe tener minimo 8 caracteres")
    
    if not any(n.isdigit()for n in clean_password):
            errores.append("La contraseña debe tener al menos un número")
        #si hay errores termina aqui
    if errores:
            return False, None, errores

#si todo esta bien 
    return True, clean_password, errores


#EFECTOS

def registro_errores(errores):
    for error in errores:
        Logs.append(error)


ok,clean_password,errores = validar_password(" hola1234")

if not ok:
    registro_errores(errores)
else:
    print(clean_password,"Contraseña correcta")
print("LOGS",Logs)
        
    
        
    
    





