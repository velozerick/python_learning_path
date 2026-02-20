#tener precios base y aplicar formulas

#soporte se cobra por hora                              $250
#CCTV se cobra por camara instalada/configurada         $450
#Redes se cobra por punto de red salida/ponchado        $350

#Extras(recargos)
#Urgente + 15%
#Empresa + 10%

#crear diccionario con valores
servicios = {
    "1":250, #soporte
    "2": 450, #CCTV
    "3": 350 #Redes
}


def cotizador (servicio, unidades,urgente,empresa):
    
    '''
    print("DEBUG servicio:", servicio, type(servicio))
    print("SERVICIO", servicio)
    print("TIPO", type(servicio))
    print("LLAVES",servicios.keys())
    '''
    price = servicios[servicio]
    subtotal =  price * unidades
    urgente = urgente.strip().lower()
    empresa = empresa.strip().lower()

    if urgente == "s":
        total = subtotal * 1.15
    if empresa == "s":
        total = subtotal * 1.10
    else:
        return subtotal


    return total






