# Son funciones incorporadas  y sirven para operar rapidamente sobre estructuras de datos como : 
# listas, tuplas, strings o diccionarios

#Contar registros, calcular totales , obtener valores extremos, estadistica basica , validar longitudes

#----------
# LEN()
#----------

#Devuelve cantidad de elementos

len([1,2,3]) #3
len("hola") #4


#----------
# SUM()
#----------

sum([10,20,30]) # 60


#----------
# MAX()
#----------

max([5,10,30]) #30


#----------
# MIN()
#----------

min([10,20,5])#5



#----------
# *args
#----------

#Recibe una cantidad variable de argumentos posicionales 
#(Es una forma flexible de  crear funciones cuando no sabes cuantos vaores recibiras)

def calcular_total(*precios):
    return sum(precios)



#----------
# **kwargs
#----------

#Recibe una cantidad variable de argumentos nombrados

def crear_usuario(**datos):
    return datos







#--------------------
#Sistema basico de pedidos 

def pedidos(*precio,**datos_cliente):
    #si no hay datos
    if not precio:
        return False ,"No se enviarion servicios", None
    
    #Calcular

    total = sum(precio)
    cantidad_servicios = len(precio)
    servicio_caro = max(precio)
    servicio_barato =min(precio)

    #devolver estructurado

    resumen = {
        "total" : total,
        "cantidad de servicios" : cantidad_servicios,
        "servicio mas caro" : servicio_caro,
        "servicio mas barato" : servicio_barato
    }

    return True, "resumen creado correctamente",resumen


ok,mensaje,pedido = pedidos(
    15500,3529,452,20,6529,
    nombre = "SYREI",
    ciudad="Guadalajara",
    prioridad="alta"

)

if ok:
    print(mensaje)
    print(pedido)
else:
    print("error:", mensaje)