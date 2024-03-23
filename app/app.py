from flask import Flask, send_file, jsonify, json, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yaml')

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/data', methods=['GET'])
def obtener_datos():
    with open('data.json') as json_file:
        datos = json.load(json_file)
    return jsonify(datos)

@app.route('/data', methods=['POST'])
def cargar_datos():
    nuevos_datos = request.json
    try:
        with open('data.json', 'w') as json_file:
            json.dump(nuevos_datos, json_file)
        return 'Datos cargados exitosamente', 200
    except Exception as e:
        return f'Error al cargar los datos: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
