import requests

# Define los datos que deseas cargar
nuevos_datos = {
    "nombre": "Lucas Damian Piorelle",
    "edad": 39
}

# Realiza una solicitud POST para enviar los datos a la API
respuesta = requests.post('http://localhost:5000/datos', json=nuevos_datos)

# Verifica la respuesta de la API
if respuesta.status_code == 200:
    print("Datos cargados exitosamente")
else:
    print("Error al cargar los datos:", respuesta.text)
