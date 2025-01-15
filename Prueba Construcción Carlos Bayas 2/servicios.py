import mysql
from db import get_connection


#función para consultar productos en la base de datos
def consultar_producto(id_producto):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un entero positivo."} # Programación Defensiva  

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT nombre, cantidad FROM productos WHERE id = %s", (id_producto,))
    producto = cursor.fetchone()
    connection.close()

    if producto:
        return producto
    else:
        return {"error": "Producto no encontrado."}


#función para agregar productos a la base de datos
def agregar_producto(id_producto, cantidad):
    if not isinstance(cantidad, int) or cantidad <= 0:
        return {"error": "La cantidad debe ser un número entero positivo."} # Programación Defensiva

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO productos (id, nombre, cantidad) VALUES (%s, %s, %s)",
                       (id_producto, f"Producto {id_producto}", cantidad))
        connection.commit()
        return {"mensaje": f"Producto {id_producto} agregado con éxito."}
    except mysql.connector.errors.IntegrityError:
        return {"error": "El producto ya existe. Use otro ID."}
    finally:
        connection.close()


#función para actualizar el stock de un producto
def actualizar_stock(id_producto, nueva_cantidad):
    assert isinstance(id_producto, int) and id_producto > 0, "ID del producto debe ser un entero positivo." #aserción 
    assert isinstance(nueva_cantidad, int) and nueva_cantidad >= 0, "La nueva cantidad debe ser un entero no negativo."#aserción

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM productos WHERE id = %s", (id_producto,))
    if cursor.fetchone()[0] == 0:
        connection.close()
        return {"error": "Producto no encontrado."}

    cursor.execute("UPDATE productos SET cantidad = %s WHERE id = %s", (nueva_cantidad, id_producto))
    connection.commit()
    connection.close()

    return {"mensaje": f"Stock de Producto {id_producto} actualizado a {nueva_cantidad}."}
