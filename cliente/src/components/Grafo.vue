<template>
  <cytoscape ref="cy" :config="config" :afterCreated="afterCreated" style="height: 100%;">
    <cy-element v-for="def in elementos" :key="`${def.data.id}`" sync :definition="def" />
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
  // props: {
  //   nodos: Array,
  //   origenes: Array,
  //   destinos: Array,
  //   pesos: Array,
  //   config: {
  //     type: Object,
  //     default: {
  //       style: [
  //         {
  //           selector: "node",
  //           style: {
  //             "background-color": "#7958d5",
  //             label: "data(id)",
  //           },
  //         },
  //         {
  //           selector: "edge",
  //           style: {
  //             label: "data(weight)",
  //             width: 3,
  //             "curve-style": "bezier",
  //             "line-color": "#ccc",
  //             "target-arrow-color": "#ccc",
  //             "target-arrow-shape": "triangle",
  //           },
  //         },
  //       ],
  //       layout: { name: "circle", row: 1 },
  //     },
  //   },
  // },
  data() {
    return {
      nodos: [],
      origenes: [],
      destinos: [],
      pesos: [],
      config: {
        type: Object,
        layout: { name: "circle", row: 1 },
        style: [
          {
            selector: "node",
            css: {
              label: "data(etiqueta)",
            }
          },
          {
            selector: ".inicial",
            css: {
              "shape": "triangle",
            }
          },
          {
            selector: ".noInicial",
            css: {
            }
          },
          {
            selector: ".final",
            css: {
              "background-color": "#58d5b2",
            }
          },
          {
            selector: ".noFinal",
            css: {
              "background-color": "#c458d5",
            }
          },
          {
            selector: "edge",
            css: {
              label: "data(weight)",
              width: 3,
              "curve-style": "bezier",
              "line-color": "#ccc",
              "target-arrow-color": "#ccc",
              "target-arrow-shape": "triangle"
            }
          }
        ],
      }
    };
  },
  mounted() {
    this.nodos = [
      { id: 1, etiqueta: "A", inicial: true, final: false },
      { id: 2, etiqueta: "B" , inicial: false, final: true},
      { id: 3, etiqueta: "C" , inicial: false, final: false},
      { id: 4, etiqueta: "D" , inicial: true, final: true}
    ];
    this.origenes = ["A"];
    this.destinos = ["B"];
    this.pesos = ["0"];
  },
  watch: {
    elementos() {
      this.$nextTick(async () => {
        const cy = this.$refs.cy.instance;
        await this.afterCreated(cy);
      });
    }
  },
  computed: {
    elementos() {
      var elementos = [];
      for (const nodo of this.nodos) {
        if (nodo && nodo.etiqueta && nodo.etiqueta != "") {
          elementos.push({
            classes: [nodo.inicial ? 'inicial' : 'noInicial', nodo.final ? 'final' : 'noFinal'],
            data: { id: nodo.etiqueta, etiqueta: nodo.etiqueta},
            position: {
              x: 1,
              y: 1
            },
            group: "nodes"
          });
        }
      }
      for (let i = 0; i < this.origenes.length; i++) {
        const origen = this.origenes[i];
        const destino = this.destinos[i];
        const peso = this.pesos[i];
        if (origen && destino) {
          elementos.push({
            data: {
              id: origen + destino,
              source: origen,
              target: destino,
              weight: peso,
              // type: "loop"
            },
            group: "edges"
          });
        }
      }
      return elementos;
    }
  },
  methods: {
    async afterCreated(cy) {
      await cy;
      cy.layout({ name: "circle", row: 1 }).run();
    }
  }
};
</script>
