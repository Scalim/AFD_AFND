import Vue from "vue";
import Vuex from 'vuex';

Vue.use(Vuex);

var nodos =
    localStorage.getItem("nodos") &&
    localStorage.getItem("nodos") != "undefined" ?
    JSON.parse(localStorage.getItem("nodos") || "null") : [];
var origenes =
    localStorage.getItem("origenes") &&
    localStorage.getItem("origenes") != "undefined" ?
    JSON.parse(localStorage.getItem("origenes") || "null") : [];

var destinos =
    localStorage.getItem("destinos") &&
    localStorage.getItem("destinos") != "undefined" ?
    JSON.parse(localStorage.getItem("destinos") || "null") : [];

var pesos =
    localStorage.getItem("pesos") &&
    localStorage.getItem("pesos") != "undefined" ?
    JSON.parse(localStorage.getItem("pesos") || "null") : [];


const store = new Vuex.Store({
    state: {
        nodos,
        origenes,
        destinos,
        pesos
    },
    mutations: {
        crearGrafo(state, payload) {
            state.nodos = payload.nodos;
            state.origenes = payload.origenes;
            state.destinos = payload.destinos;
            state.pesos = payload.pesos;

            localStorage.setItem("nodos", JSON.stringify(payload.nodos));
            localStorage.setItem("origenes", JSON.stringify(payload.origenes));
            localStorage.setItem("destinos", JSON.stringify(payload.destinos));
            localStorage.setItem("pesos", JSON.stringify(payload.pesos));
        },
    },
    getters: {
        grafo: state => {
            var aristas = [];
            var vertices = [];

            for (const nodo of state.nodos) {
                vertices.push(nodo.etiqueta);
            }

            for (let i = 0; i < state.origenes.length; i++) {
                const origen = state.origenes[i];
                const destino = state.destinos[i];
                const peso = state.pesos[i];

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