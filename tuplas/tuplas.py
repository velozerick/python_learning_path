#Tuplas 

'''
Es una coleccion de valores como una lista pero se escribe con parentesis

'''

lista = []
tupla =()



registro = ('caja_1','camote','206-02-06') 

# Puedes leer una tupla pero no moificarla

l_equipo = ['laptop','pc','raspberry'] # esto es una lista 
equipo = ('laptop','pc','raspberry')# esto es una tupla

print(equipo[0]) #imprimir el lugar 0 de la tupla
print(equipo[-1]) # imprimir el ultimo elemento de la tupla
print(len(equipo)) # imprimir cuantos elementos hay en la tupla

l_equipo[0] = 'tablet'
print(l_equipo)

# equipo[0] = 'tablet' # esto marcara error ya que una tupla no se puede modificar

