solicitudes = ['Pepino', 'Rabano', 'LECHUGA', 'camote', 'pepino', 'Jitomate', 'pepino']

permitidos = {'jitomate', 'pepino', 'lechuga'}


c_aprobados = 0
c_rechazados = 0



aprobados_unicos = []
rechazados_unicos = []


for solicitud in solicitudes:
    c = solicitud.lower()
    if c in permitidos:
        aprobados_unicos.append(c)
        c_aprobados = c_aprobados + 1

        
    else:
        rechazados_unicos.append(c)
        c_rechazados = c_rechazados + 1


        
ac = set(aprobados_unicos)
print(ac)
print(rechazados_unicos)
        

print(c_aprobados)
print(c_rechazados)


# Calcular pocentaje de aprobados y rechazados 

porcentaje_a = (c_aprobados / len(solicitudes) ) * 100 # crear variable de porcentaje, = al contador de aprobados entre el total de elementos , multiplicando por cien 
print('EL porcentaje de aprobados es: ',porcentaje_a, '%') 

# Calcular el procentaje de rechazados , ceando la variable del porcenaje de rechazados = al contador de rechazados entre el total de elementos , multiplicando por cien 
porcentaje_r = (c_rechazados / len(solicitudes)) * 100
print('EL porcentaje de rehazados es: ',porcentaje_r, '%')