import numpy as np

print("Actividad 4. Buenas Practicas Python")
print("Alumno: Jose Sepulveda \n")


def max_of_list(list_of_list):
    """
    Funcion que devuelve el valor maximo de una lista
    Parametros:
        list_of_list: una lista de listas
    Output:
        max_of: diccionario que indica el valor maximo de cada una de las listas dentro de la lista
    """
    max_of = {f'Max of list {idx}': np.max(list_of_list[idx]) for idx in range(0,len(list_of_list))}

    return max_of

def is_prime(value):
    """
    Funcion para filtrar numero primos
    Parametros:
        value: numero int
    Output:
        True si el numero es primo, False caso contrario
    """
    # Evaluamos si es igual a 1
    if value == 1:
        return True
    # Evaluamos si es negativo
    elif value <= 0:
        return False
    else:
        # Evaluamos si es par
        if value%2 == 0:
            return False
        # Evaluamos si es divisible por algun otro numero
        for n in range(2,int((value+3)/2)):
            if value%n == 0:
                return False
        return True

list_of = [[2,3],[3,6],[7,6]]

print(max_of_list(list_of))

odd_list = list(filter(is_prime, range(1,1000)))

print(f'\nPrime number on the list:\n {odd_list}')
