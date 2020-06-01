<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
        <p class="title">¿Grafo Euleriano o Hamiltoniano?</p>
        <b-button
          type="is-primary"
          outlined
          rounded
          expanded
          class="button"
          :loading="cargando"
          @click="obtenerCamino"
          >Determinar</b-button
        >
        <div v-if="respuesta">
          <p>
            {{
              `El camino ${
                this.objetoRespuesta[0].es ? "" : "no"
              } es Hamiltoniano${
                this.objetoRespuesta[0].es
                  ? " y su camino es: " + this.objetoRespuesta[0].camino
                  : ""
              }.`
            }}
          </p>
          <p>
            {{
              `El camino ${
                this.objetoRespuesta[1].es ? "" : "no"
              } es Euleriano${
                this.objetoRespuesta[1].es
                  ? " y su camino es: " + this.objetoRespuesta[1].camino
                  : ""
              }.`
            }}
          </p>
        </div>
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

export default {
  name: "MatrizCaminos",
  components: {
    Grafo,
  },
  data: () => ({
    indiceMaximo: 1,
    cargando: false,
    respuesta: false,
    objetoRespuesta: null,
    nodos: [],
    cy: null,
    config: {
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#7958d5",
            label: "data(id)",
          },
        },
      ],
      layout: { name: "grid", rows: 3 },
    },
  }),
  mounted() {
    this.respuesta = false;
    this.objetoRespuesta = null;
    this.cargando = false;
  },
  watch: {
    elementos() {
      this.$nextTick(() => {
        const cy = this.$refs.cy.instance;
        this.afterCreated(cy);
      });
    },
  },
  computed: {
    elementos() {
      var nodos = [];
      for (const etiqueta of this.nodos) {
        if (etiqueta && etiqueta != "") {
          nodos.push({
            data: { id: etiqueta },
            position: {
              x: 1,
              y: 1,
            },
            group: "nodes",
          });
        }
      }
      return nodos;
    },
  },
  methods: {
    agregarNodo() {
      this.indiceMaximo++;
      var valorAsciiA = 65;
      var caracter = String.fromCharCode(valorAsciiA + this.indiceMaximo);
      this.nodos.push(caracter);
    },
    eliminarNodo(i) {
      this.nodos.splice(i, 1);
    },
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
    },
    obtenerCamino() {
      this.cargando = true;
      var data = {
        grafo: this.$store.getters.grafo,
      };
      axios({
        method: "post",
        url: this.$apiUrl + "/camino",
        data: data,
      })
        .then((r) => {
          var respuesta = r.data;
          var hamilton = {
            es: false,
            camino: [],
          };
          var euler = {
            es: false,
            camino: [],
          };
          for (let index = 0; index < respuesta.length; index++) {
            const element = respuesta[index];
            var atributo = Object.keys(element);

            if (atributo == "hamiltoniano") {
              hamilton.es = element.hamiltoniano;
            } else if (atributo == "euleriano") {
              euler.es = element.euleriano;
            } else if (atributo == "caminoEuleriano") {
              euler.camino = element.caminoEuleriano;
            } else {
              hamilton.camino = element.caminoHamiltoniano;
            }
          }

          this.objetoRespuesta = [hamilton, euler];
          this.respuesta = true;
          this.cargando = false;
        })
        .catch((e) => {
          this.cargando = false;
          console.log(e);
        });
    },
  },
};
</script>

<style>
#cytoscape-div {
  min-height: 100px;
  height: 100%;
}

#cytoscape-div,
#cytoscape-div > div,
#cytoscape-div > div > canvas {
  min-height: 100px !important;
  height: 100% !important;
}
</style>
