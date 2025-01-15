import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         
        password="P@ssw0rd",  
        database="inventario_db"
    )

#Conexión a la base de datos, las creación de la base de datos se encuentra en el archvio creacion_db.sql
