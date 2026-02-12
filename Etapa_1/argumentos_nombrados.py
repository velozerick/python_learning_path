# Argumentos nombrados 

#crear usuario en un sistema
#Queremos que la funcionreciba , username, email,role, active y devuelva un diccionario con esos datos

def crear_usuario(*,username,email,role,active = True): # crear funcion, (*) significa a partir de aqui todos los parametros deben ser enviados por nombre
    #crear dicionario
    usuario = {
        "username": username,
        "email": email,
        'role': role,
        'active': active
    }
    return usuario

#llamada correcta con argumentos nombrados
usuario1 = crear_usuario(
    email = "erick@vulcan.com",
    username  = 'Erick',
    role = "admin"   
)
print(usuario1)





################################################################3


print("Ejercicio regisro de usuario \n")
#Registrar usuario
def registrar_usuario(*,username,email,age,activo = True):
    user = {
        "username": username,
        "email": email,
        "age":age,
        "activo": activo
    }
    if username == "":
        return "El usuario no puede estar vacio"
    elif age < 13:
        return "Debes tener mayor de 13 para registrarte"
    elif email == "":
        return "email no puede estar vacio"
    else:
        return user

user1 = registrar_usuario(
    username = 'Erick',
    email = 'erick@vulcan.com',
    age = 15
)

print(user1)
print("fin del ejercicio \n\n")

###############################################################


#Registro con validacion

def crear_cuenta(*,username,email,edad,activo = True):

    #validar datos
    if username == "":
        return {"ok":False, "error": "El usuario no puede estar vacio"}
    if email == "":
        return {"ok":False, "error": "El email no puede estar vacio"}
    if "@"not in email:
        return {"ok":False, "error": "El email debe tener @"}
    if edad < 18:
        return {"ok":False, "error": "No tienes la edad suficicente para el registro"}
    
    #crear dicionario
    user = {
        "username": username,
        "email": email,
        "edad": edad
    }

    return{"ok":True , "user":user}

#crear variable con arguemntos nombrados
resp = crear_cuenta(
    username = "Erick",
    email = "erick@vulcano.com",
    edad = 1
    )

if resp ["ok"]:
    print("usuario creado",resp["user"])

else:
    print("error:", resp["error"])

