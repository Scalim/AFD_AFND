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
            return JSON.parse(localStorage.getItem("automataUno"));
        },
        automataUnoEsVacio: state => {

            return state.automataUno.E == [] && state.automataUno.K == [] && state.automataUno.F == [] && state.automataUno.S == [] && state.automataUno.s == [];
        },
        automataDos: state => {

            return JSON.parse(localStorage.getItem("automataDos"));
        },
        automataDosEsVacio: state => {
            console.log(state.automataDos.E, state.automataDos.K, state.automataDos.F, state.automataDos.K, state.automataDos.S, state.automataDos.s)
            return state.automataDos.E == [] && state.automataDos.K == [] && state.automataDos.F == [] && state.automataDos.S == [] && state.automataDos.s == [];
        },
    }
});

export default store;