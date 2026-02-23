#mostrar resumen de acuerdo a entrada de datos

import cotizacion
import validacion


servicio = validacion.seleccion_servicio(cotizacion.servicios)

unidades = validacion.pedir_unidades()

urgente = validacion.pedir_sn("Desea cotizacion urgente? s/n: ")

empresa = validacion.pedir_sn("Desea cotizacion empresarial? s/n: ")

resultado = cotizacion.cotizador(servicio, unidades, urgente, empresa)

print(resultado)
