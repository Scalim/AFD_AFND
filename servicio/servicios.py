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


def simplificar(json):
    print(fecha_y_hora()+"[servicios.py] simplificar()")
    automata = parsear_automata(json['automata'])
    print("Autómata:")
    automata.mostrar_quintupla()
    return jsonify(["uwu"])


def operar(json):
    print(fecha_y_hora()+"[servicios.py] operar()")
    operacion = json['operacion']
    print("Operación: " + str(operacion))

    if (operacion == "complemento"):
        print("Autómata 1:")
        automata1.mostrar_quintupla()
        automata1 = parsear_automata(json['automatas'][0])
    else:
        automata1 = parsear_automata(json['automatas'][0])
        automata2 = parsear_automata(json['automatas'][1])
        print("Autómata 1:")
        automata1.mostrar_quintupla()
        print("Autómata 2:")
        automata2.mostrar_quintupla()

    return jsonify(["uwu"])