# Se validan datos



def seleccion_servicio (servicios):
    while True:
        servicio = input("Escriba que servicio desea: 1-soporte, 2-CCTV, 3-Redes: ").strip()
        if servicio in servicios:
            return servicio
        print("Error, solo se puede seleccionar 1, 2 , 3")


def pedir_unidades():
        unidades = int(input("Escriba la cantidad de unidades que desea: "))
        return unidades


def pedir_sn(mensaje):
    while True:
        resp = input(mensaje).strip().lower()
        if resp == "s" or resp == "n":
             return resp
        print("Error, solo se puede seleccionar 's' o 'n' ")


