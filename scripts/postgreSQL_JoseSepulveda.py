import psycopg2 
from psycopg2 import sql 
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# Connect to an existing database 
conn = psycopg2.connect(user='postgres', password='postgres', host='localhost', port=5438) 
# Open a cursor to perform database operations 
cur = conn.cursor()

#######
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# creamos base de datos
cur.execute(sql.SQL('CREATE DATABASE {};').format( sql.Identifier('actividad'))) 

cur.close() 
conn.close()

# conectamos con la base de datos
conn = psycopg2.connect(database="actividad", user='postgres', password='postgres', host='localhost', port=5438)
cur = conn.cursor()

# creamos tabla edicion
try: 
    cur.execute("""
    CREATE TABLE edicion (
        ID_edic SERIAL  PRIMARY KEY, 
        Numero varchar(80));""") 
except psycopg2.Error as e: 
    print('Error Crear tabla: %s', str(e))

# creamos tabla notas
try: 
    cur.execute("""
    CREATE TABLE notas (
        ID_notas SERIAL PRIMARY KEY, 
        Name varchar(80),
        Edad INT,
        Notas NUMERIC, 
        ID_edic INT REFERENCES edicion(ID_edic));""") 
except psycopg2.Error as e: 
    print('Error Crear tabla: %s', str(e))

# insertamos datos en tabla edicion
try: 
    cur.execute(f"""INSERT INTO edicion (Numero) VALUES 
    ('Uno'),
    ('Dos'),
    ('Tres');""") 
except psycopg2.Error as e: 
    print('Error Insertar dato: %s', str(e))

# insertamos datos en tabla notas
try: 
    cur.execute(f"""INSERT INTO notas (Name, Edad, Notas, ID_edic) VALUES 
    ('Isabel Maniega', 30, 5.6, 1),
    ('José Manuel Peña', 30, 7.8, 1),
    ('Pedro López', 25, 5.2, 2),
    ('Julia García', 22, 7.3, 1),
    ('Amparo Mayora', 28, 8.4, 3),
    ('Juan Martínez', 30, 6.8, 3),
    ('Fernando López', 35, 6.1, 2),
    ('María Castro', 41, 5.9, 3);""") 
except psycopg2.Error as e: 
    print('Error Insertar dato: %s', str(e))

# actualizamos datos de Pedro Lopez
try: 
    cur.execute("UPDATE notas SET notas=6.4 WHERE name='Pedro López'") 
except psycopg2.Error as e: 
    print('Error Actualizar dato: %s', str(e))

# actualizamos datos de María Castro
try: 
    cur.execute("UPDATE notas SET notas=5.2 WHERE name='María Castro'") 
except psycopg2.Error as e: 
    print('Error Actualizar dato: %s', str(e))

# lectura de datos de tabla edicion
cur.execute("SELECT * FROM edicion;") 
rows = cur.fetchall()
print("\n---- Datos en tabla edicion---\n") 
for row in rows: 
    print(row)

# lectura de datos de tabla notas
cur.execute("SELECT * FROM notas;") 
rows = cur.fetchall() 
print("\n---- Datos en tabla notas---\n") 
for row in rows: 
    print(row)

# lectura de datos con nota entre 5 y 6.5
cur.execute("SELECT * FROM notas WHERE notas BETWEEN 5 AND 6.5;") 
rows = cur.fetchall() 
print("\n---- Datos en tabla notas con notas entre 5 y 6.5---\n") 
for row in rows: 
    print(row)

# lectura de datos de la edicion 2
cur.execute("""SELECT * 
               FROM notas n
               INNER JOIN edicion e
               ON n.ID_edic = e.ID_edic
               WHERE numero = 'Dos';""") 
rows = cur.fetchall() 
print("\n---- Datos en de personas en la edicion DOS---\n") 
for row in rows: 
    print(row)

# eliminar datos de Pedro Lopez
try: 
    cur.execute("DELETE FROM notas WHERE name='Pedro López';")
except psycopg2.Error as e: 
    print('Error eliminar dato: %s', str(e))

# Close communication with the database
conn.commit() 
cur.close() 
conn.close()