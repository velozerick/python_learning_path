#Crear funcion 
#intentar abrir archivo
#si no existe -> regresa list vacia y error
#si existe -> devuelve lista SOLO con naves activas
#cada nave debe ser un diccionario diciendo nave falcon, capacidad , 5 , la capacidad debe ser entero , si la capacidad no es numero se manjea error 



def leer_naves(path):
    naves = [] #crear lista
    error = None #crear error

    #Intentar abrir y leer archivo
    try:
        with open(path , "r") as archivo:
          contenido = archivo.readlines()
          for lines in contenido:
              partes = lines.strip().split(": ", 1)
              if len(partes) != 2:
                  continue
              key = partes[0].strip()
              value = partes[1].strip()

              if partes[0] == "Nave":
                  nave = partes[1]
              if partes[0] == "Estado" and partes[1] == " activa":
                  estado = partes[1]
              if partes[0] == "Capacidad":
                  capacidad = partes[1]

                  dicc_naves = {
                  "Nave": nave ,
                  #"Estado": estado,
                  "Capacidad": capacidad
               }
                  naves.append(dicc_naves)


    except FileNotFoundError: 
            error = "No se encontró el archivo o está vacio"
    
    return naves, error

naves ,error = leer_naves("naves.txt")

if not error:
    print(naves)
else:
    print(naves)
    print(error)
