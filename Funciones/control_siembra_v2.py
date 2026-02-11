
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




#clasificar solicitudes
def clasificar_solicitudes(lista_normalizada,permitidos): #Crear la funcion con los parametros de la lista ya filtrada y la permitidos que es con la que vamos a sacar aprobados y rechazados
    lista_permitidos=[]#crear lista permitidos
    lista_rechazados=[]#crear lista rechazados
    for c in lista_normalizada:#crear for, para lista_ normalizada en permitidos
        if c in permitidos: #si los elementos de lista normalizada esta en la lista permitidos
            lista_permitidos.append(c)
        else:
            lista_rechazados.append(c)
    return lista_permitidos, lista_rechazados

lista_permitidos,lista_rechazados = clasificar_solicitudes(lista_normalizada,permitidos) #variable creada para el resultado


#Resumen

def resumen (lista_permitidos,lista_rechazados):#crear funcion donde las entradas son las listas creadas
    #crear contadores, contador1 , contador2 uno para permitidos y otro para rechazados
    contador_p = len(lista_permitidos)
    contador_r = len(lista_rechazados)
    total = contador_p + contador_r
    #calcular el porcentaje parte/total * 100 de permitidos y de rechazados
    porcentaje_p = len(lista_permitidos)/total * 100
    porcentaje_r = len(lista_rechazados)/total * 100
    #enviar con return
    return porcentaje_p,porcentaje_r,contador_p,contador_r,total

porcentaje_p,porcentaje_r,contador_p,contador_r,total = resumen(lista_permitidos,lista_rechazados)




print('Los cultivos permitidos son:',lista_permitidos,'\n')
print('Los cultivos rechazados son:',lista_rechazados,'\n')

print('La cantidad de cultivos permitidos son:',contador_p,'\n')
print('La cantidad de cultivos rechazados son:',contador_r,'\n')
print('el total de cultivos son:',total)

print('EL porcentaje de permitidos:',round(porcentaje_p,2),'%')
print('El porcentaje de rechazados:',round(porcentaje_r,2),'%')