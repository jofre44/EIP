import threading
print("Actividad 9. Programacion Avanzada en Python")
print("Alumno: Jose Sepulveda \n")

print('Actividad: Crear funcion y ejecutar en diferentes hilos.\n')

def print_function(max_number):
    for number in range(1,max_number+1):
        print(f'Ejecucion del for loop numero {number} en hilo {max_number}')


try:
    final_num = int(input('Introducir numeros de hilos a crear (default 10):\n'))
except:
    print('Valor incorrecto, se crean 10 hilos')
    final_num = 10

for i in range(1, final_num + 1):
    trhead = threading.Thread(target=print_function, args=(i,))
    trhead.start()