#Control de acceso a sistema

intentos = 3
password_correcta = "velozer"

usuario = input("Ingrese usuario ")
while intentos > 0:
    
    password_ingresada = input("ingrese password    ")

    if password_ingresada == "":
        print("vacio, porfavor intenta de nuevo")
     
    elif password_ingresada != password_correcta:
        intentos = intentos - 1
        print("wrong, bad password",intentos,"attemps remianing")


    else:
        print("bienvenid@ ",usuario)
        print("Lograste salir de la matrix")
        break
