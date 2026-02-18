#Crea una funcion qu edevuelva solo las misiones activas

def mission_active ():
    list_active = []
    with open("misiones.txt", "r") as archivo: 
        content = archivo.readlines()
        for line in content:
            partes = line.strip().split(":")
            if partes[0] == "Mision":
                nombre = partes[1]
            if partes[0] == "Estado" and partes[1] == " activa":
                list_active.append(nombre)
    return list_active


misiones_activas = mission_active()
print("Las misiones activas son : ",misiones_activas)




# devolver un diccionario solo con las misiones activas y su destino

def mission_info ():
    list_mission = []
    with open("misiones.txt", "r") as archivo: 
        content = archivo.readlines()
        for line in content:
            partes = line.strip().split(":")
            if partes[0] == "Mision":
                nombre = partes[1]
            if partes[0] == "Destino":
                destino = partes[1]
            if partes[0] == "Estado" and partes[1] == " activa":
                estado = partes[1]
                info = {
                        "nombre": nombre,
                        "destino": destino,
                        "estado": estado
                       }
                list_mission.append(info)
    return list_mission


info_mision = mission_info()
print("Informacion de las misiones : ",info_mision , "\n")