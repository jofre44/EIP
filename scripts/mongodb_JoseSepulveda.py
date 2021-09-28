import pymongo 
import datetime
# crearemos un cliente para conectarnos a la base de datos 
# añadimos el IP (localhost) y host (27017) 
client = pymongo.MongoClient("localhost", 27017) 

# creamos conexión a la base de datos en nuestro caso eip 
db = client.actividad

# insertamos datos
doc_list = [
    {"nombre": "Pedro López", "edad": 25, "email": "pedro@eip.com", "nota": 5.2, 
    "fecha": datetime.datetime.strptime("12-07-2021 12:45:26", "%d-%m-%Y %H:%M:%S")},
    {"nombre": "Julia García", "edad": 22, "email": "julia@eip.com", "nota": 7.3, 
    "fecha": datetime.datetime.strptime("12-07-2021 12:45:26", "%d-%m-%Y %H:%M:%S")},
    {"nombre": "Amparo Mayoral", "edad": 28, "email": "amparo@eip.com", "nota": 8.4, 
    "fecha": datetime.datetime.strptime("12-07-2021 12:45:26", "%d-%m-%Y %H:%M:%S")},
    {"nombre": "Juan Martínez", "edad": 30, "email": "juan@eip.com", "nota": 6.8, 
    "fecha": datetime.datetime.strptime("12-07-2021 12:45:26", "%d-%m-%Y %H:%M:%S")}
]

for doc in doc_list:
    db.user.insert_one(doc)

# actualizar datos de Amparo y Juan
datos = db.user.find({}) 
for dato in datos:
    # actualizacion de Amparo  
    if dato["nombre"] == "Amparo Mayoral": 
        id_Amparo = dato["_id"]
        db.user.update_one({"_id": id_Amparo}, 
                            {"$set": {"nombre": "Amparo Mayoral", "nota": 9.3}})
    # actualizacion de Juan
    if dato["nombre"] == "Juan Martínez": 
        id_Juan = dato["_id"]
        db.user.update_one({"_id": id_Juan}, 
                            {"$set": {"nombre": "Juan Martínez", "nota": 7.2}})

# impresion de datos en base de datos
print("\n-----------------------Impresion de datos en BBDD----------\n")
datos = db.user.find({}) 
for dato in datos:
    print(dato)

# impresion de datos con notas entre 7 y 7.5
print("\n-----------------------Impresion de datos con notas entre 7 y 7.5----------\n")
my_query = {'nota':{'$gte':7 ,'$lte':7.5}}
datos = db.user.find(my_query)

for dato in datos:
    print(dato)

# eliminar datos de Pedro
datos = db.user.find({}) 
for dato in datos: 
    if dato["nombre"] == "Pedro López": 
        idMongo = dato["_id"] 
        db.user.delete_one({"_id": idMongo})