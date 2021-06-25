import pandas as pd

print("Actividad 8. Programacion Avanzada en Python")
print("Alumno: Jose Sepulveda \n")

print('Actividad 1: Lectura y escritura de archivo .txt.\n')

file_name = input("Ingrese nombre de archivo .txt (dejar en blanco para usar nombre predeterminado 'ejemplo'):\n")

if file_name == '':
    file_name = 'ejemplo'

file_name = file_name + '.txt'

with open(file_name, 'a') as file:
    write_str = input('¿Desea agregar texto al archivo (t: si; f: no):\n')
    if write_str == 'f':
        write_in_txt = False
    elif write_str == 't':
        write_in_txt = True
        file.write('\n')
    else:
        print('Dato in correcto, no se agrega texto')
        write_in_txt = False
    while write_in_txt:
        text_to_add = input("Ingrese texto a agregar (dejar en blanco para agregar texto de Lorem Ipsum):\n")
        if text_to_add == '':
            text_to_add = 'Lorem ipsum dolor sit amet'
        file.write(f'{text_to_add}\n')

        write_str = input('¿Desea seguir agregando texto al archivo (t: si; f: no):\n')
        if write_str == 'f':
            write_in_txt = False
        elif write_str == 't':
            write_in_txt = True
        else:
            print('Dato in correcto, no se agrega texto')
            write_in_txt = False

print('------- Mostrando contenido del archivo elegido. --------\n')
file = open(file_name, 'r')
print(file.read())

print('Actividad 2: Lectura de archivo .csv y obtener valor medio, maximo y mimimo de cada columna.\n')
print('Se lee arcchivo cotizacion.csv')
sep_type = input("Indicar tipo de separador de columnas (dejar en blanco para usar ';' como seperador)")
if sep_type == '':
    sep_type = ';'
dec_type = input("Indicar tipo de separador decimal (dejar en blanco para usar '.' como seperador)")
if dec_type == '':
    dec_type = '.'
df = None
try :
    df = pd.read_csv('cotizacion.csv', sep= sep_type,index_col = 'Nombre', decimal = dec_type)
except:
    print("""Archivo cotizacion.csv no ha sido encontrado o separador de columnas utilizado incorrecto.""")
    print("""Verificar que el archivo se encuentre en la ruta correcta y de utilizar el seperador de columnas correcto""")

if df is not None:
    try:
        df = df.apply(pd.to_numeric)
        print('Se muestran a continuacion datos estadisticos de las columnas:\n')
        print(df.describe())
    except:
        print('Error al intentar convertir tipo de datos de las columnas. Verificar seperador de decimales y de miles')