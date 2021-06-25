import sqlite3
from sqlite3 import Error

print("Actividad 7. Programacion Avanzada en Python")
print("Alumno: Jose Sepulveda \n")


def create_connection(db_file):

    """ Funcion para crear conexion con la base de datos
        param:
            df_file: nombre de la base de datos
        output:
            conn: conexion a la base de datos
    """
    conn =  None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Conexión con la base de datos {db_file} correcta')
    except Error as e:
        print('No se pudo conectar a la base de datos.\n')
        print(e)

    return conn

def create_table(conn, query, table_name):

    """Funcion para crear tabla
        params:
            conn: conexion con base de datos
            query: query para crear tabla
            table_name: nombre de la tabla a crear
    """"
    if conn is None:
        print('No hay conexión a base de datos')
        return None
    try:
        c = conn.cursor()
        c.execute(query)
        print(f'Se creo table {table_name} de forma correcta')
    except Error as e:
        print(f'No se pudo crear tabla {table_name}.\n')
        print(e)

 
def col_info(conn, mod_type, table_name):

    """ Funcion para crear diccionario clave (nombre de as columnas de la tabla) valor (valor de las columnas)
        params:
        conn: conexion con base de datos
        mod_type: tipo de modificacion a realizar
        table_name: nombre de la tabla de datos
    """
    query_col = f"""PRAGMA table_info({table_name});"""
    c = conn.cursor()
    c.execute(query_col)
    col_list = c.fetchall()
    values_dic = {}
    for i in range(len(col_list)):
        if col_list[i][1] == 'id' and mod_type == 'u':
            value = input(f"Ingrese valor para campo {col_list[i][1]} ({col_list[i][2]}) que se va a actualizar: ")
        else:
            value = input(f"Ingrese valor para campo {col_list[i][1]} ({col_list[i][2]}): ")
        values_dic[col_list[i][1]] = value
    return values_dic

def modify_table(conn, mod_type, table_name):

    """ Funcion para modificar tabla de datos
        params:
        conn: conexion con base de datos
        mod_type: tipo de modificacion a realizar
        table_name: nombre de la tabla de datos
    """

    if mod_type == 'i': 
        
        # Consulta tipo INSERT
        values_dic = col_info(conn, mod_type, table_name)

        col_str = ''
        val_str = ''
        for col, val in values_dic.items():
            if col_str == '':
                col_str = col_str + col
                val_str = val_str + '?'
            else:
                col_str = col_str + ',' + col
                val_str = val_str + ',?'

        query = f"""INSERT INTO {table_name} ({col_str})
                    VALUES({val_str})"""
        data_list = tuple(values_dic.values())
        try:
            c = conn.cursor()
            c.execute(query, data_list)
            conn.commit()
            print(f'Se ingresaron los valores de forma correcta')
        except Error as e:
            print(f'No se pudo ingresar valores.\n')
            print(e)


    elif mod_type == 'u':

        # Consulta tipo UPDATE
        values_dic = col_info(conn, mod_type, table_name)

        col_str = ''
        aux_list = []
        for col, val in values_dic.items():

            if col != 'id':
                if col_str == '':
                    col_str = col_str + col + '= ?'
                    aux_list.append(val)
                else:
                    col_str = col_str + ',\n' + col + '= ?'
            else:
                id_field = val

        query = f"""UPDATE {table_name} 
                    SET {col_str}
                    WHERE id = ?"""
        print(query)
        aux_list.append(id_field)
        data_list = tuple(aux_list)
        print(data_list)
        try:
            c = conn.cursor()
            c.execute(query, data_list)
            conn.commit()
            print(f'Se actualizaron los valores de forma correcta')
        except Error as e:
            print(f'No se pudo actualizar valores.\n')
            print(e)

    elif mod_type == 's':

        # Consulta tipo SELECT
        query = f"""SELECT * FROM {table_name}"""

        try:
            c = conn.cursor()
            c.execute(query)
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f'Error al hacer el select.\n')
            print(e)

    elif mod_type == 'd':

        #Consulta tipo DELETE
        query = f"""DELETE FROM {table_name}"""

        try:
            c = conn.cursor()
            c.execute(query)
            conn.commit()
            print(f'Se han eliminado todos los registros de la tabla.\n')
        except Error as e:
            print(f'Error el borrar datos en tabla.\n')
            print(e)

    else:
        print('Dato incorrecto')


print('Actividad 1: Crear base de datos.\n')
db_name = input("Ingrese nombre de Base de datos (dejar en blanco para usar nombre predeterminado 'ejemplo'):\n")

if db_name == '':
    db_name = 'ejemplo'

db_file = db_name + '.db'

conn = create_connection(db_file)


print('\nActividad 2: crear tablas')

crear_table_str = input('¿Desea crear tabla (t: si; f: no):\n')
if crear_table_str == 'f':
    crear_tabla = False
elif crear_table_str == 't':
    crear_tabla = True
else:
    print('Dato in correcto, no se van a crear tabla')
    crear_tabla = False
i = 1
while crear_tabla:
    table_name = input(f"Ingrese nombre de tabla (dejar en blanco para usar nombre predeterminado 'tabla{i}'):\n")
    if table_name == '':
        table_name = 'tabla'+str(i)
    
    numero_campos = int(input(f'Ingrese numero de campos en la tabla {table_name}:\n'))
    
    print('Primer campo de la tabla es id siendo un integer y Primary key')

    fields_query = 'id integer PRIMARY KEY'

    for j in range(2,numero_campos+1):
        col_name = input(f"Ingrese nombre de columna {j} (dejar en blanco para usar nombre predeterminado 'columna{j}'):\n")
        if col_name == '':
            col_name = 'columna'+str(j)

        col_type = input(f"Ingrese tipo de dato de la columna (1 para integer; 2 para text'):\n")
        if col_type == '1':
            col_type = 'integer'
        elif col_type == '2':
            col_type = 'text'
        else:
            print('Dato erroneo. Se crea columna tipo integer')
            col_type = 'integer'
        
        col_null = input(f"Ingrese si se permite valor nulo para columna (1 es permitido; 2 no es permitido'):\n")
        if col_null == '1':
            col_null = ''
        elif col_null == '2':
            col_null = ' NOT NULL'
        else:
            print('Dato erroneo. Se permite valores nulos en la columna')
            col_null = ''

        fields_query = fields_query + ',\n' + col_name + ' ' + col_type + col_null

    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                {fields_query}
                );"""
    
    create_table(conn, query, table_name)

    crear_table_str = input('¿Desea crear otra tabla (t: si; f: no):\n')
    if crear_table_str == 'f':
        crear_tabla = False
    elif crear_table_str == 't':
        crear_tabla = True
        i += 1
    else:
        print('Dato in correcto, no se van a crear tabla')
        crear_tabla = False



print('\nActividad 3: modificar tablas')
modificar_str = input('¿Desea modificar alguna tabla (t: si; f: no):\n')
if modificar_str == 'f':
    modificar = False
elif modificar_str == 't':
    modificar = True
else:
    print('Dato in correcto, no se van a modificar ninguna tabla')
    modificar = False
while modificar:
    c = conn.cursor()
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
    tables_list = c.fetchall()

    tables_dic = {i: tables_list[i][0] for i in range(len(tables_list))}
    table_ind = int(input(f'Seleccione tabla a modificar {tables_dic}:\n'))
    table_select = None
    try:
        table_select = tables_dic[table_ind]
    except:
        print('Valor equivocado para seleccion de tabla')
        
    if table_select is not None:
        mod_type = input("Ingrese tipo de modificacion a realizar (i: insertar; u: actualizar; s: listar; d: borrar):\n")
        modify_table(conn, mod_type, table_select)

    modificar_str = input('¿Desea realizar otra modificacion (t: si; f: no):\n')
    if modificar_str == 'f':
        modificar = False
    elif modificar_str == 't':
        modificar = True
    else:
        print('Dato in correcto, no se van a realizar modificaciones')
        modificar = False