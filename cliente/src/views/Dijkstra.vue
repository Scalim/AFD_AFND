<template>
  <div class="is-flex" style="width: 100%;">
    <div
      class="card"
      style="width: 100%; height: calc(100vh - 80px); border-radius: 10px;"
    >
      <div class="is-full-h" style="padding: 20px;">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div
            class="column is-6"
            style="overflow-y: scroll; padding-right: 20px"
          >
            <p class="title">Camino más corto</p>
            <div class="column">
              <b-field grouped style="margin-top: 20px;">
                <b-field expanded>
                  <b-autocomplete
                    rounded
                    v-model="origen"
                    :data="nodos"
                    keep-first
                    open-on-focus
                    field="etiqueta"
                    placeholder="Nodo de origen"
                    clearable
                  >
                    <template slot="empty">Sin resultados</template>
                  </b-autocomplete>
                </b-field>
                <b-field expanded>
                  <b-autocomplete
                    rounded
                    v-model="destino"
                    :data="nodos"
                    keep-first
                    open-on-focus
                    field="etiqueta"
                    placeholder="Nodo de destino"
                    clearable
                  >
                    <template slot="empty">Sin resultados</template>
                  </b-autocomplete>
                </b-field>
              </b-field>
              <b-button
                type="is-primary"
                outlined
                rounded
                expanded
                :loading="cargando"
                @click="dijkstra"
                >Calcular</b-button
              >
              <div v-if="respuesta">
                <p>
                  {{this.objetoRespuesta.ruta.length != 0 ? `La duración del camino es de${this.objetoRespuesta.pesoTotal}` : 'No se especifíca duración.'}}
                </p>
                <p>{{this.objetoRespuesta.ruta.length != 0 ? `La ruta fue ${this.objetoRespuesta.ruta}` : 'No hay una ruta específica.'}}</p>
              </div>
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
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Grafo from "../components/Grafo.vue";

export default {
  name: "Dijkstra",
  components: {
    Grafo,
  },
  data: () => ({
    indiceMaximo: 1,
    cargando: false,
    respuesta: false,
    objetoRespuesta: null,
    origen: null,
    destino: null,
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
  watch: {
    elementos() {
      this.$nextTick(() => {
        const cy = this.$refs.cy.instance;
        this.afterCreated(cy);
      });
    },
  },
  mounted() {
    this.respuesta = false;
    this.objetoRespuesta = null;
    var nodosStore = this.$store.state.nodos;
    var nodosActuales = [];
    for (let index = 0; index < nodosStore.length; index++) {
      const element = nodosStore[index];
      nodosActuales.push(element.etiqueta);
    }
    this.nodos = nodosActuales;
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
    dijkstra() {
      this.cargando = true;
      var data = {
        grafo: this.$store.getters.grafo,
        inicio: this.origen,
        final: this.destino,
      };
      axios({
        method: "post",
        url: this.$apiUrl + "/dijkstra",
        data: data,
      })
        .then((r) => {
          this.objetoRespuesta = r.data;
          this.respuesta = true;
          this.cargando = false;
        })
        .catch((e) => {
          console.log(e);
          this.cargando = false;
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
