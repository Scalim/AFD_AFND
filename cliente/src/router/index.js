import Vue from "vue";
import VueRouter from "vue-router";
import Presentacion from "../views/Presentacion";
import AFD from "../views/AFD";
import Simplificar from "../views/Simplificar";
import Operar from "../views/Operar";

Vue.use(VueRouter);

const routes = [{
        path: "/",
        name: "presentacion",
        component: Presentacion
    },
    {
        path: "/operar",
        name: "operar",
        component: Operar
    },
    {
        path: "/afd",
        name: "afd",
        component: AFD
    },
    {
        path: "/simplificar",
        name: "simplificar",
        component: Simplificar
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.VUE_APP_BASE_URL,
    routes
});

export default router;