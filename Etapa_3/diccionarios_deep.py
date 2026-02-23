"""
-Diccionarios con mas campos
-Diccionarios con otros dicionarios dentro     diccionarios anidados
-Acceso a multiples niveles
"""

##########  Diccionario dentro de diccionario (DICCIONARIOS ANIDADOS)

empresa = {
    "nombre_empresa": "SYREI",
    "ubicacion": {
        "ciudad": "Guadalajara",
        "pais": "México"
                },
    "contacto": {
        "telefono": 5511223344,
        "email": "syrei@mail.com"
    }
}


print(empresa["ubicacion"]["ciudad"]) #Imprimir ciudad
print(empresa["contacto"]["email"]) #imprimir email

empresa ["ubicacion"]["pais"] = "Canada" #cambiar el pais a canada
print(empresa["ubicacion"]["pais"]) 

empresa ["contacto"]["activo"] = True #agregar en contaco la clave activo

print(empresa) #imprimir todo el diccionario


print("\n -----LISTA DE DICCIONARIOS----- \n")
##########  LISTA DE DICCIONARIOS

# lista -> indice -> diccionario -> clave


servicios = [
    {"id":1, "nombre":"soporte","precio": 250 },
    {"id":2, "nombre": "CCTV", "precio":400},
    {"id": 3, "nombre": "redes", "precio":560}
             ]

print(servicios[1]["nombre"]) # el nombre del segundo servicio
print(servicios[2]["precio"]) # el precio del tercer servicio

names = [n ["nombre"] for n in servicios   ]
print(names)

precios = [n ["precio"] for n in servicios if n ["precio"] > 400]
print(precios)







print("\n -----DICCIONARIO QUE CONTIENE LISTA DE DICCIONARIOS----- \n")
##########  DICCIONARIO QUE CONTIENE LISTA DE DICCIONARIOS

# diccionario -> clave -> lista -> indice -> clave

empresa_data = {
    "nombre_empresa": "SYREI",
    "ubicacion": {
        "ciudad": "Guadalajara",
        "pais": "México"
    },
    "servicios":[
        {"id": 1, "nombre": "soporte", "precio": 250},
        {"id": 2, "nombre": "CCTV", "precio": 890},
        {"id": 3, "nombre": "redes", "precio": 430}
    ]

    }

print(empresa_data["servicios"][2]["nombre"]) # el nombre del tercer servicio
print(empresa_data["ubicacion"]["ciudad"]) # imprimir la ciudad

high_price = [n["precio"] for n in empresa_data["servicios"] if n["precio"] > 300]
print(high_price)





for i in empresa_data["servicios"]:
    print(i["nombre"], i["precio"])

