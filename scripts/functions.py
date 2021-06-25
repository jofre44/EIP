print("Actividad 3. Programacion Avanzada en Python")
print("Alumno: Jose Sepulveda \n")

print("Ejercicio 1: Crear función para sumar o restar valores")

def suma_resta(num_1, num_2):
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except:
        print("Error!! Datos introducidos no son números")
        return()
    
    print(f"Suma de los números: {num_1+num_2}\n")
    print(f"Resta de los números: {num_1-num_2}\n")

# Pedir número por pantalla
numero_1 = input("Introducir numero 1:\n")
numero_2 = input("Introducir numero 2:\n")

suma_resta(numero_1, numero_2)

print("\nEjercicio 2: Función recursiva suma de numero")

def suma_recursiva(numero=10, num_sum=0):
    if numero == 0:
        print(f"Suma de funcion recursiva: {num_sum}")
    else:
        num_sum = num_sum + numero 
        numero -= 1
        suma_recursiva(numero, num_sum)

#Solicitar numero inicial por pantalla
numero_inicial = input("Introducir numero entero:\n")

try:
    numero_inicial = int(numero_inicial)
    suma_recursiva(numero_inicial)
except:
    print("El numero introducido es incorrecto. Se calcula suma del 0 al 10")
    suma_recursiva()
