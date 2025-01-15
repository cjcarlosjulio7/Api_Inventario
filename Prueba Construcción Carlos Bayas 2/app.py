from flask import Flask, request, jsonify
from servicios import consultar_producto, agregar_producto, actualizar_stock

app = Flask(__name__)

# Ruta para consultar un producto
@app.route('/producto/<int:id_producto>', methods=['GET'])
def obtener_producto(id_producto):
    resultado = consultar_producto(id_producto)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200

# Ruta para agregar un producto
@app.route('/producto', methods=['POST'])
def agregar_producto_endpoint():
    datos = request.json
    id_producto = datos.get("id_producto")
    cantidad = datos.get("cantidad")

    if not id_producto or not cantidad:
        return jsonify({"error": "Se requieren 'id_producto' y 'cantidad'."}), 400

    resultado = agregar_producto(id_producto, cantidad)
    if "error" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado), 201


@app.route('/producto/<int:id_producto>', methods=['PUT'])
def actualizar_producto_endpoint(id_producto):
    datos = request.json
    nueva_cantidad = datos.get("cantidad")

    if nueva_cantidad is None:
        return jsonify({"error": "Se requiere la nueva cantidad."}), 400

    try:
        resultado = actualizar_stock(id_producto, nueva_cantidad)
        if "error" in resultado:
            return jsonify(resultado), 404
        return jsonify(resultado), 200
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

