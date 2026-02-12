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