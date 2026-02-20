#mostrar resumen de acuerdo a entrada de datos

import cotizacion

#COTIZAR
while True:
    servicio = input("Escriba que servicio desea: 1-soporte, 2-CCTV, 3-Redes ").strip()
    if servicio in cotizacion.servicios:
        break
    print("Error, solo puedes seleccionar 1, 2 ,3")
        
unidades = int(input("Escriba la cantidad de unidades que desea:"))

urgente = input("Desea que la cotización sea urgente? escriba s para si o n para no: ")
empresa = input("Desea que la cotización sea para empresa? escriba s para si o n para no: ")

resultado = cotizacion.cotizador(servicio, unidades,urgente,empresa)
print(resultado)

