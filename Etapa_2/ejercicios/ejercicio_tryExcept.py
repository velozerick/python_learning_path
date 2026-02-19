# verificar si existe o no el archivo

def leer_misiones(path):
    lista_misiones =[]
    error = None
    
    #leer el archivo
    try:
        with open(path, "r") as archivo:
            contenido = archivo.read()
            lineas = contenido.split("\n")
            lista_misiones = lineas
            for i in lista_misiones:
                i_limpio = i.strip()
                if i_limpio:
                    lista_misiones.append(i_limpio)
    #except
    except FileNotFoundError:
        error = "\n--- ¡Archivo no encontrado ¡ ---\n"
    
    return lista_misiones , error

lista_misiones, error = leer_misiones("mission.txt")

if not error:
    print(lista_misiones)
else:
    print("Error: " ,error)




#############################

def dividir(a ,b):
    error = None
    opn = None
    try:
        opn = a / b
    except ZeroDivisionError:
        error = "No se puede dividir entre cero "
    return opn, error

opn ,error = dividir(5, 0)

if not error:
    print(opn)
else:
    print("Error, esta mal en algo ", error)

