from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from servicios import fecha_y_hora, simplificar, operar, transformar
from automatafinito import fecha_y_hora


application = Flask(__name__)
cors = CORS(application, resources={r"/*": {"resources": ["http://localhost:8080", "http://localhost:8081"]}})
application.config['CORS_HEADERS'] = 'Content-Type'


@application.route('/', methods=['GET'])
def conectar():
    print(fecha_y_hora()+"[api.py] conectar()")
    return jsonify(mensaje='Conectado a servicio')


@application.route('/simplificar', methods=['POST'])
def simplificar_automata():
    print(fecha_y_hora()+"[api.py] simplificar_automata()")
    content = request.get_json(silent=True)
    return simplificar(content)


@application.route('/operar', methods=['POST'])
def operar_automata():
    print(fecha_y_hora()+"[api.py] operar_automata()")
    content = request.get_json(silent=True)
    return operar(content)


@application.route('/transformar', methods=['POST'])
def transformar_automata():
    print(fecha_y_hora()+"[api.py] transformar_automata()")
    content = request.get_json(silent=True)
    return transformar(content)


if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)