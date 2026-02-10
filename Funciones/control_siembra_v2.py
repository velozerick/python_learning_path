
solicitudes = [
    "Jitomate", " pepino", "Rábano", "LECHUGA", "Camote",
    "Perejil", "cilantro", "JITOMATE", "Pepino ", "  lechuga  ",
    "Zanahoria", "CALABACITA", "PAPA", "papa", "Chíle serrano",
    "Cebolla", "CEBOLLA ", "Epazote", "ALBAHACA", "ESPINACA",
    "brócoli", "Coliflor", "Acelga", "Tomate", "Jitomate ",
    "pepino", "RABANO", "rabano", "  perejil", "cilantro ",
    "Fresa", "Sandía", "Melón", "Nopal", "  chile serrano  ",
    "HIERBABUENA", "hierbabuena", "Orégano", "oregano", "Manzanilla",
    "Lavanda", "Caléndula", "calendula", "Zinnia", "zinnia ",
    "Espinaca", "LECHUGA", "Pepino", "JITOMATE", "CILANTRO"
]

permitidos = {
    "jitomate", "pepino", "lechuga", "espinaca", "cilantro", "perejil",
    "albahaca", "epazote", "zanahoria", "rabano", "cebolla", "chile serrano",
    "calabacita", "papa"
}


#normalizar solicitudes 

def normalizar_solicitudes(solicitudes): #crear la funcion con el parametro solicitudes que es la lista que vamos a manejar
    normalizada = [] #cear nueva lista normalizada
    for solicitud in solicitudes:#para solicitud en solicitudes 
        c =solicitud.strip().lower()# crear variable para guardar solicitudes en minusculas
        normalizada.append(c)#llenar la nueva lista 
    return normalizada#funcion termina y la manda al exterior
lista_normalizada = normalizar_solicitudes(solicitudes)# guardar en una variable el resultado

print(lista_normalizada)


#clasificar solicitudes
def clasificar_solicitudes(lista_normalizada,permitidos): #Crear la funcion con los parametros de la lista ya filtrada y la permitidos que es con la que vamos a sacar aprobados y rechazados
    lista_permitidos=[]#crear lista permitidos
    for c in lista_normalizada:#crear for, para lista_ normalizada en permitidos
        if c in permitidos: #si los elementos de lista normalizada esta en la lista permitidos
            lista_permitidos.append(c)
    return lista_permitidos

lpermitidos = clasificar_solicitudes(lista_normalizada,permitidos)
print(lpermitidos)


