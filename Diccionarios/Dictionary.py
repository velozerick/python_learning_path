''' Un diccionario es una estructura de datos que guarda informacion en pares:
clave -- valor

por ejemplo:

nombre -- Erick

edad -- 22

activo -- True

Eso es un diccionario
'''


#Crear diccionario junto con datos
persona = {
    "nombre" : "Erick",
    'edad': 22,
    'activo': True
}

#Acceder al diccionario a su clave y su valor
print(persona["nombre"])
print(persona["edad"])

#Modificar
persona["edad"] = 23
print(persona)


#Agregar
persona['pais'] = 'México'
print(persona)