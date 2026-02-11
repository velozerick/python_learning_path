# Se divide en varias etapas para llegar a flask por lo tanto iniciamos con esto 

# un parametro opcional es un parametro que tiene valor por defecto

#ejemplo

def saludar(nombre="invitado"):
    print('hola',nombre)
saludar()
saludar('erick')
#si no le paso el argumento , usa el valor por defecto
#si le pasas el argumento , usa el que tu envies

# ejercicio area

def calcular_area(base, altura=10):
    area = base * altura
    return area

resultado = calcular_area(3,20)
print(resultado)


#crea una funcion que calcule el precio final, parametros precio, impuesto por defecto 16%, debe regresar el precio con impuesto aplicado

def calculo(precio, iva=0.16):
    precio_final = precio * (1 + iva)
    return precio_final
precio_iva = calculo(50)
print('el precio final con iva:',round(precio_iva))



#crear la funcion calcular_precio_seguro
def calcular_precio_seguro(precio, iva = 0.16):
    #si el precio es (-) mandar un mensaje , de lo contrario hacer el calculo del precio final
    if precio < 0:
        return 'precio invalido'
    else:
        precio_final = precio * (1 + iva)
    return precio_final
resultado = calcular_precio_seguro(20)

print(resultado)