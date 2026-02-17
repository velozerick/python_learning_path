with open("logs.txt", "a") as archivo:
    archivo.write("usuario 2 creado correctamente\n")

"""
Desglose--

with open -> esto abre el archivo
"logs.txt" -> nombre del archivo (si no existe  lo crea)
"a" -> modo append agrega sin borrar
as archivo -> le damos un nombre temporal al archivo
archivo.write(...) -> escribimos dentro 

syntaxis

with open("archivo.txt", "modo") as variable:
    hacer_algo()
"""


#"a"

def guardar_log(mensaje):
    with open("sistema_logs.txt", "a") as archivo:
        archivo.write(mensaje + "\n")
guardar_log("usuario creado")
guardar_log("password invalido")
guardar_log("usuario 2 creado")

'''

#"w"
def crear_archivo(clientes):
    with open("clientes.txt", "w") as archivo_clientes:
      archivo_clientes.write(clientes + " \n")

crear_archivo("Cliente : SYREI\n"
              "Ciudad: Guadalajara")
'''


#Crea una funcion donde reciba un diccionario de cliente y lo guarde en un archivo llamado clientes.txt

#diccionario
datos_cliente = {
    "nombre" : "SYREI",
    "ciudad": "Guadalajara",
    "preioridad": "alta"
}


def crear_archivo_cliente(datos_cliente):
    with open("clientes.txt", "w") as archivo:
        for clave, valor in datos_cliente.items():
            archivo.write(clave + ": " + valor + "\n")


    
crear_archivo_cliente(datos_cliente)







#"r"
