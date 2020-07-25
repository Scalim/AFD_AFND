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

const store = new Vuex.Store({
    state: {
        nodosUno,
        origenesUno,
        destinosUno,
        pesosUno, 
        nodosDos,
        origenesDos,
        destinosDos,
        pesosDos
    },
    mutations: {
        crearAutomataUno(state, payload) {
            state.nodosUno = payload.nodos;
            state.origenesUno = payload.origenes;
            state.destinosUno = payload.destinos;
            state.pesosUno = payload.pesos;

            localStorage.setItem("nodosUno", JSON.stringify(payload.nodos));
            localStorage.setItem("origenesUno", JSON.stringify(payload.origenes));
            localStorage.setItem("destinosUno", JSON.stringify(payload.destinos));
            localStorage.setItem("pesosUno", JSON.stringify(payload.pesos));
        },
        crearGrafo(state, payload) {
            state.nodosDos = payload.nodos;
            state.origenesDos = payload.origenes;
            state.destinosDos = payload.destinos;
            state.pesosDos = payload.pesos;

            localStorage.setItem("nodosDos", JSON.stringify(payload.nodos));
            localStorage.setItem("origenesDos", JSON.stringify(payload.origenes));
            localStorage.setItem("destinosDos", JSON.stringify(payload.destinos));
            localStorage.setItem("pesosDos", JSON.stringify(payload.pesos));
        },
    },
    getters: {
        grafoUno: state => {
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
                vertices
            };
        },
        grafoDos: state => {
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
                vertices
            };
        }
    }
});

export default store;