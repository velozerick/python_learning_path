########## Gestion de Huerto ##########


#importar librerias
import datetime
hoy = datetime.date.today() #datetime es el modulo, .date es una clase dentro de datetime, today() es un metodo que devuelve la fecha actual  
print(hoy)

#crear fecha manual

fecha_siembra = datetime.date(2026,2,18)
print(fecha_siembra)

dias = hoy - fecha_siembra
print(dias)