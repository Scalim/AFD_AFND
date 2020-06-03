# Crear funciones acá 
from automatafinito import AutomataFinito

automata = {
  "E": ["Q1", "Q2", "Q3"],
  "K": ["a", "b"],
  "S": "Q3",
  "F": ["Q3"],
  "s": [
    {
      "inicio": "Q1",
      "letra": null,
      "final": "Q2"
    },
    {
      "inicio": "Q2",
      "letra": "a",
      "final": "Q2"
    },
    {
      "inicio": "Q2",
      "letra": "b",
      "final": "Q3"
    }
  ]
}

# Parsear autómata
def parsear_automata(automata):
    return AutomataFinito(automata['K'], automata['S'], automata['s'], automata['F'], )