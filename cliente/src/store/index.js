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

var conexionesUno =
    localStorage.getItem("conexionesUno") &&
    localStorage.getItem("conexionesUno") != "undefined" ?
    JSON.parse(localStorage.getItem("conexionesUno") || "null") : [];

var alfabetoUno =
    localStorage.getItem("alfabetoUno") &&
    localStorage.getItem("alfabetoUno") != "undefined" ?
    JSON.parse(localStorage.getItem("alfabetoUno") || "null") : [];

var inicialesUno =
    localStorage.getItem("inicialesUno") &&
    localStorage.getItem("inicialesUno") != "undefined" ?
    JSON.parse(localStorage.getItem("inicialesUno") || "null") : [];

var finalesUno =
    localStorage.getItem("finalesUno") &&
    localStorage.getItem("finalesUno") != "undefined" ?
    JSON.parse(localStorage.getItem("finalesUno") || "null") : [];

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

var conexionesDos =
    localStorage.getItem("conexionesDos") &&
    localStorage.getItem("conexionesDos") != "undefined" ?
    JSON.parse(localStorage.getItem("conexionesDos") || "null") : [];

var alfabetoDos =
    localStorage.getItem("alfabetoDos") &&
    localStorage.getItem("alfabetoDos") != "undefined" ?
    JSON.parse(localStorage.getItem("alfabetoDos") || "null") : [];

var inicialesDos =
    localStorage.getItem("inicialesDos") &&
    localStorage.getItem("inicialesDos") != "undefined" ?
    JSON.parse(localStorage.getItem("inicialesDos") || "null") : [];

var finalesDos =
    localStorage.getItem("finalesDos") &&
    localStorage.getItem("finalesDos") != "undefined" ?
    JSON.parse(localStorage.getItem("finalesDos") || "null") : [];

const store = new Vuex.Store({
    state: {
        nodosUno,
        origenesUno,
        destinosUno,
        conexionesUno,
        alfabetoUno,
        inicialesUno,
        finalesUno,
        nodosDos,
        origenesDos,
        destinosDos,
        conexionesDos,
        alfabetoDos,
        inicialesDos,
        finalesDos
    },
    mutations: {
        crearAutomataUno(state, payload) {
            state.nodosUno = payload.nodos;
            state.origenesUno = payload.origenes;
            state.destinosUno = payload.destinos;
            state.conexionesUno = payload.conexiones;
            state.alfabetoUno = payload.alfabeto;
            state.inicialesUno = payload.iniciales;
            state.finalesUno = payload.finales;

            localStorage.setItem("nodosUno", JSON.stringify(payload.nodos));
            localStorage.setItem("origenesUno", JSON.stringify(payload.origenes));
            localStorage.setItem("destinosUno", JSON.stringify(payload.destinos));
            localStorage.setItem("conexionesUno", JSON.stringify(payload.conexiones));
            localStorage.setItem("alfabetoUno", JSON.stringify(payload.alfabeto));
            localStorage.setItem("inicialesUno", JSON.stringify(payload.iniciales));
            localStorage.setItem("finalesUno", JSON.stringify(payload.finales));

        },
        crearAutomataDos(state, payload) {
            state.nodosDos = payload.nodos;
            state.origenesDos = payload.origenes;
            state.destinosDos = payload.destinos;
            state.conexionesDos = payload.conexiones;
            state.alfabetoDos = payload.alfabeto;
            state.inicialesDos = payload.iniciales;
            state.finalesDos = payload.finales;

            localStorage.setItem("nodosDos", JSON.stringify(payload.nodos));
            localStorage.setItem("origenesDos", JSON.stringify(payload.origenes));
            localStorage.setItem("destinosDos", JSON.stringify(payload.destinos));
            localStorage.setItem("conexionesDos", JSON.stringify(payload.conexiones));
            localStorage.setItem("alfabetoDos", JSON.stringify(payload.alfabeto));
            localStorage.setItem("inicialesDos", JSON.stringify(payload.iniciales));
            localStorage.setItem("finalesDos", JSON.stringify(payload.finales));
        },
    },
    getters: {
        automataUno: state => {
            const alfabeto = state.alfabetoUno;
            var aristas = [];
            var vertices = [];

            for (let i = 0; i < state.nodosUno.length; i++){
                const inicial = state.inicialesUno[i];
                const final = state.finalesUno[i];
                const nodo = nodosUno[i].etiqueta;
                
                //NO SÉ SI AGREGAR EL ESTADO DE INICIAL Y FINAL
                vertices.push(nodo);
            }

            for (let i = 0; i < state.origenesUno.length; i++) {
                const origen = state.origenesUno[i];
                const destino = state.destinosUno[i];
                const peso = state.conexionesUno[i];

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
        automataDos: state => {
            const alfabeto = state.alfabetoDos;
            var aristas = [];
            var vertices = [];

            for (let i = 0; i < state.nodosDos.length; i++){
                const inicial = state.inicialesDos[i];
                const final = state.finalesDos[i];
                const nodo = nodosDos[i].etiqueta;
                
                //NO SÉ SI AGREGAR EL ESTADO DE INICIAL Y FINAL
                vertices.push(nodo);
            }

            for (let i = 0; i < state.origenesDos.length; i++) {
                const origen = state.origenesDos[i];
                const destino = state.destinosDos[i];
                const peso = state.conexionesDos[i];

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