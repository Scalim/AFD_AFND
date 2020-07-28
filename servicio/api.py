from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from servicios import fecha_y_hora, simplificar, operar, transformar
from automatafinito import fecha_y_hora

application = Flask(__name__)
cors = CORS(application, resources={r"/foo": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'
application.config.update(
    WTF_CSRF_ENABLED=True,
    SECRET_KEY='amo-los-grafos'
)


@application.route('/', methods=['GET'])
@cross_origin(origin='*')
def conectar():
    print(fecha_y_hora()+"[api.py] conectar()")
    return jsonify(mensaje='Conectado a servicio')


@application.route('/simplificar', methods=['POST'])
@cross_origin(origin='*')
def simplificar_automata():
    print(fecha_y_hora()+"[api.py] simplificar_automata()")
    content = request.get_json(silent=True)
    return simplificar(content)


@application.route('/operar', methods=['POST'])
@cross_origin(origin='*')
def operar_automata():
    print(fecha_y_hora()+"[api.py] operar_automata()")
    content = request.get_json(silent=True)
    return operar(content)


@application.route('/transformar', methods=['POST'])
@cross_origin(origin='*')
def transformar_automata():
    print(fecha_y_hora()+"[api.py] transformar_automata()")
    content = request.get_json(silent=True)
    return transformar(content)


if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)
