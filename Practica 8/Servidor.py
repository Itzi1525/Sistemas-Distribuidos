from flask import Flask, request, jsonify

app = Flask(__name__)

# -----------------------------
# RUTA PARA NAVEGADOR (GET)
# -----------------------------
@app.route('/')
def inicio():
    return "<h1>SERVIDOR ACTIVO</h1>"

# 👉 NUEVO: PAGAR DESDE NAVEGADOR
@app.route('/pagar_view')
def pagar_view():
    return "<h1>TRANSACCIÓN EXITOSA</h1>"

# 👉 NUEVO: CLIENTE SIMULADO
@app.route('/cliente')
def cliente_view():
    return "<h1>PAGO EXITOSO</h1>"


# -----------------------------
# API REAL (POST + JSON)
# -----------------------------

@app.route('/pagar', methods=['POST'])
def pagar():
    data = request.get_json()

    monto = data.get("monto")

    if monto <= 1000:
        return jsonify({
            "success": True,
            "mensaje": "TRANSACCIÓN EXITOSA"
        })
    else:
        return jsonify({
            "success": False,
            "mensaje": "FALLÓ LA TRANSACCIÓN"
        })


@app.route('/comprar', methods=['POST'])
def comprar():
    data = request.get_json()

    precio = data.get("precio")
    numero_productos = data.get("numero_productos")
    total = data.get("total")

    if precio * numero_productos == total:
        return jsonify({
            "success": True,
            "mensaje": "COMPRA EXITOSA"
        })
    else:
        return jsonify({
            "success": False,
            "mensaje": "FALLÓ LA COMPRA"
        })


if __name__ == '__main__':
    app.run(debug=True)