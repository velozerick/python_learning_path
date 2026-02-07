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