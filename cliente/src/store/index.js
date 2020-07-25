import Vue from "vue";
import Vuex from 'vuex';

Vue.use(Vuex);

// Datos primer autómata
var nodosUno =
    localStorage.getItem("nodosUno") &&
    localStorage.getItem("nodosUno") != "undefined" ?
    JSON.parse(localStorage.getItem("nodosUno") || "null") : [];
var origenesUno =
    localStorage.getItem("origenesUno") &&
    localStorage.getItem("origenesUno") != "undefined" ?
    JSON.parse(localStorage.getItem("origenesUno") || "null") : [];

var destinosUno =
    localStorage.getItem("destinosUno") &&
    localStorage.getItem("destinosUno") != "undefined" ?
    JSON.parse(localStorage.getItem("destinosUno") || "null") : [];

var pesosUno =
    localStorage.getItem("pesosUno") &&
    localStorage.getItem("pesosUno") != "undefined" ?
    JSON.parse(localStorage.getItem("pesosUno") || "null") : [];

var alfabetoUno =
    localStorage.getItem("alfabetoUno") &&
    localStorage.getItem("alfabetoUno") != "undefined" ?
    JSON.parse(localStorage.getItem("alfabetoUno") || "null") : [];

// Datos segundo autómata
var nodosDos =
    localStorage.getItem("nodosDos") &&
    localStorage.getItem("nodosDos") != "undefined" ?
    JSON.parse(localStorage.getItem("nodosDos") || "null") : [];
var origenesDos =
    localStorage.getItem("origenesDos") &&
    localStorage.getItem("origenesDos") != "undefined" ?
    JSON.parse(localStorage.getItem("origenesDos") || "null") : [];

var destinosDos =
    localStorage.getItem("destinosDos") &&
    localStorage.getItem("destinosDos") != "undefined" ?
    JSON.parse(localStorage.getItem("destinosDos") || "null") : [];

var pesosDos =
    localStorage.getItem("pesosDos") &&
    localStorage.getItem("pesosDos") != "undefined" ?
    JSON.parse(localStorage.getItem("pesosDos") || "null") : [];

var alfabetoDos =
    localStorage.getItem("alfabetoDos") &&
    localStorage.getItem("alfabetoDos") != "undefined" ?
    JSON.parse(localStorage.getItem("alfabetoDos") || "null") : [];

const store = new Vuex.Store({
    state: {
        nodosUno,
        origenesUno,
        destinosUno,
        pesosUno,
        alfabetoUno, 
        nodosDos,
        origenesDos,
        destinosDos,
        pesosDos,
        alfabetoDos
    },
    mutations: {
        crearAutomataUno(state, payload) {
            state.nodosUno = payload.nodos;
            state.origenesUno = payload.origenes;
            state.destinosUno = payload.destinos;
            state.pesosUno = payload.pesos;
            state.alfabetoUno = payload.alfabeto;

            localStorage.setItem("nodosUno", JSON.stringify(payload.nodos));
            localStorage.setItem("origenesUno", JSON.stringify(payload.origenes));
            localStorage.setItem("destinosUno", JSON.stringify(payload.destinos));
            localStorage.setItem("pesosUno", JSON.stringify(payload.pesos));
            localStorage.setItem("alfabetoUno", JSON.stringify(payload.alfabeto));
        },
        crearAutomataDos(state, payload) {
            state.nodosDos = payload.nodos;
            state.origenesDos = payload.origenes;
            state.destinosDos = payload.destinos;
            state.pesosDos = payload.pesos;
            state.alfabetoDos = payload.alfabeto;

            localStorage.setItem("nodosDos", JSON.stringify(payload.nodos));
            localStorage.setItem("origenesDos", JSON.stringify(payload.origenes));
            localStorage.setItem("destinosDos", JSON.stringify(payload.destinos));
            localStorage.setItem("pesosDos", JSON.stringify(payload.pesos));
            localStorage.setItem("alfabetoDos", JSON.stringify(payload.alfabeto));
        },
    },
    getters: {
        grafoUno: state => {
            const alfabeto = state.alfabetoUno;
            var aristas = [];
            var vertices = [];

            for (const nodo of state.nodosUno) {
                vertices.push(nodo.etiqueta);
            }

            for (let i = 0; i < state.origenesUno.length; i++) {
                const origen = state.origenesUno[i];
                const destino = state.destinosUno[i];
                const peso = state.pesosUno[i];

                aristas.push({
                    inicio: origen,
                    final: destino,
                    peso: peso,
                });
            }
            return {
                aristas,
                vertices,
                alfabeto
            };
        },
        grafoDos: state => {
            const alfabeto = state.alfabetoDos;
            var aristas = [];
            var vertices = [];

            for (const nodo of state.nodosDos) {
                vertices.push(nodo.etiqueta);
            }

            for (let i = 0; i < state.origenesDos.length; i++) {
                const origen = state.origenesDos[i];
                const destino = state.destinosDos[i];
                const peso = state.pesosDos[i];

                aristas.push({
                    inicio: origen,
                    final: destino,
                    peso: peso,
                });
            }
            return {
                aristas,
                vertices,
                alfabeto
            };
        }
    }
});

export default store;