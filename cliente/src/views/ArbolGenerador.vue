<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
        <h1 class="title">Árbol generador mínimo</h1>
        <div v-if="arbol != null && arbol.length">
          <div v-for="(arista, i) in arbol" :key="i">
            <p>{{ i + 1 + ". " + obtenerPaso(arbol, i) }}</p>

            <div style="height: 200px;">
              <grafo
                :nodos="getGrafoByArbol(arbol, i).nodos"
                :origenes="getGrafoByArbol(arbol, i).origenes"
                :destinos="getGrafoByArbol(arbol, i).destinos"
                :pesos="getGrafoByArbol(arbol, i).pesos"
                :config="config"
              />
            </div>
          </div>
          <div>
            <p>
              {{ `El peso total es de ${getPesoTotal(arbol)}` }}
            </p>
          </div>
        </div>
        <b-button
          style="margin-top: 20px;"
          type="is-primary"
          outlined
          rounded
          expanded
          class="button"
          :loading="cargando"
          @click="obtenerArbol()"
          >Generar</b-button
        >
      </div>

      <div class="column is-6" style="border-left: 2px solid #f5f5f5; ">
        <grafo
          :nodos="$store.state.nodos"
          :origenes="$store.state.origenes"
          :destinos="$store.state.destinos"
          :pesos="$store.state.pesos"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Grafo from "../components/Grafo.vue";
import IngresarGrafo from "../views/IngresarGrafo";

export default {
  name: "MatrizCaminos",
  components: {
    Grafo,
    IngresarGrafo,
  },
  data: () => ({
    cargando: false,
    arbol: null,
    config: {
      userPanningEnabled: false,
      userZoomingEnabled: false,
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#7958d5",
            label: "data(id)",
          },
        },
        {
          selector: "edge",
          style: {
            width: 3,
            label: "data(weight)",
            "curve-style": "bezier",
            "line-color": "#ccc",
            "target-arrow-color": "#ccc",
            "target-arrow-shape": "triangle",
          },
        },
      ],
      layout: { name: "circle", row: 1 },
    },
  }),

  methods: {
    getPesoTotal(arbol) {
      var total = 0;
      for (const arista of arbol) {
        total += arista[2];
      }
      return total;
    },
    getGrafoByArbol(arbol, i) {
      var arbolActual = arbol.slice(0, i + 1);
      var nodos = [];
      var origenes = [];
      var destinos = [];
      var pesos = [];

      for (const arista of arbolActual) {
        origenes.push(arista[0]);
        destinos.push(arista[1]);
        pesos.push(arista[2]);

        if (nodos.indexOf(arista[0]) == -1) {
          nodos.push({
            etiqueta: arista[0],
          });
        }
        if (nodos.indexOf(arista[1]) == -1) {
          nodos.push({
            etiqueta: arista[1],
          });
        }
      }

      return {
        nodos,
        origenes,
        destinos,
        pesos,
      };
    },
    obtenerArbol() {
      this.cargando = true;
      axios({
        method: "post",
        url: this.$apiUrl + "/arbol",
        data: {
          grafo: this.$store.getters.grafo,
        },
      })
        .then((r) => {
          this.arbol = r.data.arbol;
          this.cargando = false;
        })
        .catch((e) => {
          this.cargando = false;
          console.log(e);
        });
    },
    obtenerPaso(arbol, i) {
      var arbolActual = arbol.slice(0, i + 1);
      var pasoActual = arbolActual.pop();
      return pasoActual[0] + " ➜ " + pasoActual[1] + ` (${pasoActual[2]})`;
    },
  },
};
</script>
