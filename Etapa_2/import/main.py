# Aqui vamos a importar la logica de huerto.py

import huerto 
import datetime



fecha = datetime.date(2026,1,19) #fecha de la siembra
dias = huerto.dias_desde_siembra(fecha)
print("Han pasado",dias,"días desde la siembra del rábano")


