from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

application = Flask(__name__)
cors = CORS(application, resources={r"/foo": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route('/', methods=['GET'])
@cross_origin(origin='*')
def conectar():
    print('Conectado a servicio')
    return jsonify(mensaje='Conectado a servicio')

if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)