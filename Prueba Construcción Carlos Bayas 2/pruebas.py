import unittest
from servicios import agregar_producto, consultar_producto, actualizar_stock
from db import get_connection

class TestInventario(unittest.TestCase):
    
    def setUp(self):
        """
        Se ejecuta antes de cada prueba para reiniciar el estado de la base de datos.
        """
        connection = get_connection()
        cursor = connection.cursor()
        # Limpiar tabla antes de cada prueba
        cursor.execute("DELETE FROM productos")
        # Insertar datos iniciales
        cursor.execute("INSERT INTO productos (id, nombre, cantidad) VALUES (1, 'Leche', 10), (2, 'Pan', 20)")
        connection.commit()
        connection.close()

    def test_consultar_producto_valido(self):
        producto = consultar_producto(1)
        self.assertEqual(producto, {"nombre": "Leche", "cantidad": 10})

    def test_consultar_producto_invalido(self):
        producto = consultar_producto(99)  # Producto inexistente
        self.assertIn("error", producto)

    def test_agregar_producto_valido(self):
        respuesta = agregar_producto(4, 30)
        self.assertIn("mensaje", respuesta)
        producto = consultar_producto(4)  # ID auto-incremental
        self.assertEqual(producto, {"nombre": "Producto 4", "cantidad": 30})

    def test_agregar_producto_cantidad_invalida(self):
        respuesta = agregar_producto(5, -5)
        self.assertIn("error", respuesta)

    def test_actualizar_stock_valido(self):
        respuesta = actualizar_stock(1, 50)
        self.assertIn("mensaje", respuesta)
        producto = consultar_producto(1)
        self.assertEqual(producto, {"nombre": "Leche", "cantidad": 50})

    def test_actualizar_stock_invalido(self):
        with self.assertRaises(AssertionError):
            actualizar_stock(1, -10)  # Cantidad inválida

    def test_actualizar_stock_producto_inexistente(self):
        respuesta = actualizar_stock(99, 10)  # Producto inexistente
        self.assertIn("error", respuesta)

if __name__ == '__main__':
    unittest.main()
