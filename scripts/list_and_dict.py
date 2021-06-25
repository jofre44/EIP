print("Actividad 5. Programacion Avanzada en Python")
print("Alumno: Jose Sepulveda \n")

print("""Ejercicio 1: Utiliza una lista para almacenar los números del 1 al 10 la cual debe 
         ser rellenada con el uso de un bucle while. Finalmente muestra la lista en orden 
         inverso.\n""")

print("Creando lista en bucle...")

num_list = []
num = 1
while (num <=10):
    num_list.append(num)
    num +=1

num_list.sort(reverse=True)
print(f"Imprimiendo lista creada en orden inverso:\n{num_list}")

print("""Ejercicio 2:\n- Crea un diccionario 4 valores.""")
dic_val = {1: 1, 2: 2, 3: 3, 4: 4}
print(dic_val)

print("\n- Muestra los valores del diccionario.")
print(dic_val.values())

print("\n- Modifica el 3º valor del diccionario")
dic_val[3] = 33
print(dic_val)

print("\n- Añade un nuevo valor al diccionario de tipo lista")
dic_val[5] = [5,10,15]
print(dic_val)

print("\n- Muestra nuevamente los valores")
print(dic_val.values())
