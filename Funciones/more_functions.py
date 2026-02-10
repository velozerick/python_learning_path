# Intentamos encapsular una logica completa , ademas de evitar errorres ya que estara en un unico lugar y organizado

def my_function():
    #aqui va el codigo
    print("Esto es una funcion")

my_function() # llamar a la funcion


def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(2, 254)
sum_two_values(2523, 2)
sum_two_values(2, 21056)


def sum_values_r(f_val,s_val):
    return f_val + s_val
my_result = sum_values_r(10,6)

print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Erick", "veloz")

