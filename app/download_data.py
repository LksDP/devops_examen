import requests

# Realiza una solicitud GET para obtener los datos desde la API
respuesta = requests.get('http://localhost:5000/datos')

# Verifica la respuesta de la API
if respuesta.status_code == 200:
    datos_obtenidos = respuesta.json()
    print("Datos obtenidos correctamente:", datos_obtenidos)
else:
    print("Error al obtener los datos:", respuesta.text)
