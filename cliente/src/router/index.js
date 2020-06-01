import Vue from "vue";
import VueRouter from "vue-router";
import Presentacion from "../views/Presentacion";
import MatrizCaminos from "../views/MatrizCaminos";
import Dijkstra from "../views/Dijkstra";
import HamiltonianoEuleriano from "../views/HamiltonianoEuleriano";
import FlujoMaximo from "../views/FlujoMaximo";
import ArbolGenerador from "../views/ArbolGenerador";

Vue.use(VueRouter);

const routes = [{
        path: "/",
        name: "presentacion",
        component: Presentacion
    },
    {
        path: "/matriz",
        name: "matriz",
        component: MatrizCaminos
    },
    {
        path: "/dijkstra",
        name: "camino-mas-corto",
        component: Dijkstra
    },
    {
        path: "/hamiltoniano-euleriano",
        name: "hamiltoniano-euleriano",
        component: HamiltonianoEuleriano
    },
    {
        path: "/flujo",
        name: "flujo",
        component: FlujoMaximo
    },
    {
        path: "/arbol",
        name: "arbol",
        component: ArbolGenerador
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.VUE_APP_BASE_URL,
    routes
});

export default router;