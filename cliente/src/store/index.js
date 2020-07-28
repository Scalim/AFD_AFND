import Vue from "vue";
import Vuex from 'vuex';

Vue.use(Vuex);

const vacio = {
    K: [],
    S: [],
    E: [],
    F: [],
    s: []
};

var automataUno =
    localStorage.getItem("automataUno") &&
    localStorage.getItem("automataUno") != "undefined" ?
    JSON.parse(localStorage.getItem("automataUno") || "null") : vacio;
var automataDos =
    localStorage.getItem("automataDos") &&
    localStorage.getItem("automataDos") != "undefined" ?
    JSON.parse(localStorage.getItem("automataDos") || "null") : vacio;


const store = new Vuex.Store({
    state: {
        automataUno,
        automataDos,

    },
    mutations: {
        crearAutomataUno(state, payload) {
            state.automataUno = payload;
            localStorage.setItem("automataUno", JSON.stringify(payload));
        },
        crearAutomataDos(state, payload) {
            state.automataDos = payload;
            localStorage.setItem("automataDos", JSON.stringify(payload));
        },

    },
    getters: {
        automataUno: state => {
            return state.automataUno;
        },
        automataUnoEsVacio: state => {
            return state.automataUno == null || state.automataUno == vacio;
        },
        automataDos: state => {
            return state.automataDos;
        },
        automataDosEsVacio: state => {
            return state.automataDos == null || state.automataDos == vacio;
        },
    }
});

export default store;