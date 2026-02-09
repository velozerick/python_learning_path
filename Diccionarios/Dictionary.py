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

#Como saber si una clave existe?
if "edad" in persona:
    print('la clave edad existe')
else:
    print('la clave edad no existe')

###########################################################


#Diccionario ejemplo

ejemplo = {
    "avion": 'airbus',
    'modelo': 320,
    'destinos': ['cancun','puerto vallarta','Ciudad de méxico']

}




#Reto 1 ,imprimir primer destino

print(ejemplo['destinos'][0])


#Reto 2 mostrar destinos 

for viaje in ejemplo['destinos']:
        print('Destino disponible', viaje )


#Reto 3 agregar una clave llamada "Internacional" imprimir si es verdadero imprime vuelo internacional , si es falso , vuelo nacional

ejemplo['Internacional'] = False # Agregar clave y valor

print(ejemplo)

# si es Internacional 
if ejemplo['Internacional'] == True:
     print('vuelo internacional')
     #si es nacional
else:
     print('Vuelo nacional')