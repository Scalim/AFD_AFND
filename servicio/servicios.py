from flask import jsonify
from automatafinito import AutomataFinito, fecha_y_hora


def parsear_automata(automata):
    K = automata['K']  # (K) Nodos
    E = automata['E']  # (Σ) Alfabeto
    S = automata['S']  # (S) Iniciales
    F = automata['F']  # (F) Finales
    s = []             # (δ) Conexiones

    for conexion in automata['s']:
        tupla = (conexion[0], conexion[1], conexion[2])
        s.append(tupla)
    return AutomataFinito(E, K, S, F, s)


def simplificar(json):
    print(fecha_y_hora()+"[servicios.py] simplificar()")
    automata = parsear_automata(json)
    print("Autómata:")
    automata.mostrar_quintupla()
    simplificado = automata.simplificar_afd()
    simplificado.mostrar_quintupla()
    if (isinstance(simplificado, str)):
        return jsonify({
            "eraAfd": False,
            "error": simplificado
        })
    else:
        return jsonify({
            "eraAfd": True,
            "simplificado": simplificado.convertir_diccionario()
        })


def transformar(json):
    print(fecha_y_hora()+"[servicios.py] transformar()")
    automata = parsear_automata(json)
    print("Autómata:")
    automata.mostrar_quintupla()
    transformado = automata.obtener_afd()
    transformado.mostrar_quintupla()
    if (isinstance(transformado, str)):
        return jsonify({
            "eraAfd": True,
            "transformado": automata.convertir_diccionario()
        })
    else:
        return jsonify({
            "eraAfd": False,
            "transformado": transformado.convertir_diccionario()
        })


def operar(json):
    print(fecha_y_hora()+"[servicios.py] operar()")
    operacion = json['operacion']
    print("Operación: " + str(operacion))

    automata1 = parsear_automata(json['automatas'][0])
    automata2 = parsear_automata(json['automatas'][1]) if len(
        json['automatas']) > 1 else None
    if (operacion == "complemento"):
        print("Autómata 1:")
        automata1.mostrar_quintupla()
    else:
        print("Autómata 1:")
        automata1.mostrar_quintupla()
        print("Autómata 2:")
        automata2.mostrar_quintupla()

    operado = automata1.operar(operacion, automata2)
    if (isinstance(operado, str)):
        return jsonify({
            "eraAfd": False,
            "error": operado
        })
    else:
        return jsonify({
            "automata": operado.convertir_diccionario(),
            "eraAfd": True,
        })
