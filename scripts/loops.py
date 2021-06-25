import random as ran
print("Actividad 2. Programacion Avanzada en Python")
print("Alumno: Jose Sepulveda \n")

print("Ejercicio 1: Bucle que imprime numero desde 0 hasta numero introducido por pantalla")

numero = int(input("Introducir numero entero:"))
num_dict = {}
print("Inicio de bucle para imprimir numero por pantalla:")
for num in range(0, numero+1):
    print(num)
    
    # Se crea diccionario para ejercicio 2
    ran_num = ran.randint(0,100)
    num_dict[num] = num + ran_num

print("\nEjercicio 2: Imprimir valores de diccionario usando bucle for")
print("Inicio de bucle para imprimir valores de diccionario por pantalla:")
for num in num_dict.values():
    print(num)


