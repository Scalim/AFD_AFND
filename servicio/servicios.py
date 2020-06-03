from flask import jsonify


def parsear_automata(automata):
    E = automata['E']  # (Σ) Alfabeto
    K = automata['K']  # (K) Nodos
    S = automata['S']  # (S) Iniciales
    F = automata['F']  # (F) Finales
    s = []             # (δ) Conexiones

    for conexion in automata['s']:
        tupla = (conexion['inicio'], arista['letra'], arista['final'])
        s.append(tupla)
    return AutomataFinito(K, E, S, F, conexiones)


def operar(json):
    automata = parsear_automata(json['automatas'])
    return jsonify(["uwu"])


def simplificar(json):
    automata = parsear_automata(json['automata'])
    return jsonify(["uwu"])
