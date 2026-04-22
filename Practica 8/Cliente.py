import requests

# ---- PAGAR ----
url = "http://127.0.0.1:5000/pagar"

datos_pago = {
    "numero_tarjeta": "123456789",
    "monto": 1000,
    "nombre": "Juan Perez",
    "codigo_CVV": "456"
}

respuesta = requests.post(url, json=datos_pago)
data = respuesta.json()

print(data["mensaje"])


# ---- COMPRAR ----
url2 = "http://127.0.0.1:5000/comprar"

datos_compra = {
    "id_producto": 101,
    "precio": 250,
    "numero_productos": 4,
    "total": 1000
}

respuesta2 = requests.post(url2, json=datos_compra)
data2 = respuesta2.json()

print(data2["mensaje"])