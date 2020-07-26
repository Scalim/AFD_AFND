<template>
  <cytoscape
    ref="cy"
    :config="config"
    :afterCreated="afterCreated"
    style="height: 100%;"
  >
    <cy-element
      v-for="def in elementos"
      :key="`${def.data.id}`"
      sync
      :definition="def"
    />
  </cytoscape>
</template>

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

<script>
export default {
  name: "Grafo",
  props: {
    nodos: Array,
    origenes: Array,
    destinos: Array,
    conexiones: Array,
    iniciales: Array,
    finales: Array,
  },
  data() {
    return {
      // nodos: [],
      // origenes: [],
      // destinos: [],
      // pesos: [],
      config: {
        type: Object,
        layout: { name: "circle", row: 1 },
        style: [
          {
            selector: "node",
            css: {
              label: "data(etiqueta)",
            },
          },
          {
            selector: ".inicial",
            css: {
              shape: "triangle",
            },
          },
          {
            selector: ".noInicial",
            css: {},
          },
          {
            selector: ".final",
            css: {
              "background-color": "#58d5b2",
            },
          },
          {
            selector: ".noFinal",
            css: {
              "background-color": "#c458d5",
            },
          },
          {
            selector: "edge",
            css: {
              label: "data(weight)",
              width: 3,
              "curve-style": "bezier",
              "line-color": "#ccc",
              "target-arrow-color": "#ccc",
              "target-arrow-shape": "triangle",
            },
          },
        ],
      },
    };
  },
  mounted() {
    // this.nodos = [
    //   { id: 1, etiqueta: "A", inicial: true, final: false },
    //   { id: 2, etiqueta: "B" , inicial: false, final: true},
    //   { id: 3, etiqueta: "C" , inicial: false, final: false},
    //   { id: 4, etiqueta: "D" , inicial: true, final: true}
    // ];
    // this.origenes = ["A"];
    // this.destinos = ["B"];
    // this.pesos = ["0"];
  },
  watch: {
    iniciales() {
      this.$nextTick(async () => {
        const cy = await this.$refs.cy.instance;
        await this.afterCreated(cy);
      });
    },
    elementos() {
      this.$nextTick(async () => {
        const cy = await this.$refs.cy.instance;
        cy.elements().remove();
        cy.add(this.elementos);
        await this.afterCreated(cy);
      });
    },
  },
  computed: {
    elementos() {
      var elementos = [];
      for (let i = 0; i < this.nodos.length; i++) {
        const nodo = this.nodos[i];
        if (nodo && nodo.etiqueta && nodo.etiqueta != "") {
          elementos.push({
            classes: [
              this.iniciales[0] == i ? "inicial" : "noInicial",
              this.finales[i] ? "final" : "noFinal",
            ],
            data: { id: nodo.etiqueta, etiqueta: nodo.etiqueta },
            position: {
              x: 1,
              y: 1,
            },
            group: "nodes",
          });
        }
      }
      for (let i = 0; i < this.origenes.length; i++) {
        const origen = this.origenes[i];
        const destino = this.destinos[i];
        const conexion = this.conexiones[i];
        if (origen && destino) {
          elementos.push({
            data: {
              id: origen + destino,
              source: origen,
              target: destino,
              weight: conexion,
              // type: "loop"
            },
            group: "edges",
          });
        }
      }
      return elementos;
    },
  },
  methods: {
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
      // cy.style(this.config.style).update();
    },
  },
};
</script>
