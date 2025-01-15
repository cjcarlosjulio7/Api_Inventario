CREATE DATABASE inventario_db;

USE inventario_db;

CREATE TABLE productos (
    id INT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL
);
-- Inserta algunos datos iniciales
INSERT INTO productos (id, nombre, cantidad) VALUES (1, 'Leche', 10), (2, 'Pan', 20);
