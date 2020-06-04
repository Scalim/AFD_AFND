from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from servicios import fecha_y_hora, simplificar, operar

application = Flask(__name__)
cors = CORS(application, resources={r"/foo": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route('/', methods=['GET'])
@cross_origin(origin='*')
def conectar():
    print(fecha_y_hora()+'El servicio funciona correctamente')
    return jsonify(mensaje='Conectado a servicio')

@application.route('/simplificar', methods=['POST'])
@cross_origin(origin='*')
def simplificarAutomata():
    print(fecha_y_hora()+'Mensaje con info')
    content = request.get_json(silent=True)
    return simplificar(content)

@application.route('/operar', methods=['POST'])
@cross_origin(origin='*')
def operarAutomata():
    print(fecha_y_hora()+'Mensaje con info')
    content = request.get_json(silent=True)
    return operar(content)

if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)