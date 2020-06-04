from datetime import datetime
from flask import jsonify
from automatafinito import AutomataFinito

def fecha_y_hora():
    return '--> '+str(datetime.now(tz=None).replace(microsecond=0))+': '

def parsear_automata(automata):
    K = automata['K']  # (K) Nodos
    E = automata['E']  # (Σ) Alfabeto
    S = automata['S']  # (S) Iniciales
    F = automata['F']  # (F) Finales
    s = []             # (δ) Conexiones

    for conexion in automata['s']:
        tupla = (conexion['inicio'], arista['letra'], arista['final'])
        s.append(tupla)
    return AutomataFinito(E, K, S, F, s)

def operar(json):
    automata1 = parsear_automata(json['automatas'][0])
    automata2 = parsear_automata(json['automatas'][1])
    operacion = json['operacion']

    return jsonify(["uwu"])


def simplificar(json):
    automata = parsear_automata(json['automata'])
    return jsonify(["uwu"])