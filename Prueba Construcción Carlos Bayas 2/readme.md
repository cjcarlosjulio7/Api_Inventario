# API de Inventario

## Descripción
Esta API permite consultar, agregar y actualizar productos en un inventario.

## Requisitos
- Python 3.8 o superior
- MySql Workbench
- Flask ('pip install flask')
- mySql ('pip install mysql-connector-python')

## Instrucciones
1. Clonar este repositorio.
2. Instalar las dependencias de pyton.
3. Crear una base de datos en MySql con el nombre 'inventario_db' con el Script dado
4. Configurar el archivo 'config.py' con los datos de la base de datos, según su usuario y contraseña
5. Ejecutar 'python app.py'.
6. Acceder a la API en `http://127.0.0.1:5000`.


## Prueba los siguientes endpoints con el uso de Postman
### `GET /producto/<id_producto>`
Consulta un producto por ID.

### `POST /producto`
Agrega un producto al inventario otrogandole un id y un stock.

### `PUT /producto/<id_producto>`
Actualiza el stock de un producto existente.
