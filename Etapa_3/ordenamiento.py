#ORDENAMIENTO

"""
sorted()

es una funcion integrada de python que sirve para ordenar un iterable y devolver una nueva lista ordenada 
"""
# sorted(iterable, key=None, reverse=False)
#iterable es lo que quieres ordenar  (lista, tupla, diccionario(ordenara las claves) cualquier estructura iterable)
# key  que valor debo usar como criterio de comparacion 



personas = [
    {"nombre": "Ana", "edad":30},
    {"nombre": "Ignacio", "edad":20}
]

ordenados = sorted(personas, key=lambda p: p["edad"])
print(ordenados)




servicios = [
        {"id": 1, "nombre": "soporte", "precio": 250},
        {"id": 2, "nombre": "CCTV", "precio": 890},
        {"id": 3, "nombre": "redes", "precio": 430}
    ]


servicios_ordenados = sorted(servicios, key = lambda s: s["precio"], reverse = True)
print(servicios_ordenados)

servicios_nombre = sorted(servicios, key = lambda n: n["nombre"])

order_name = []