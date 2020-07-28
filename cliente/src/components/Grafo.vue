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
    quintupla: Object,
  },
  data() {
    return {
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
            selector: ".inicial.final",
            css: {
              shape: "square",
              "background-image": require("../assets/nodo-if.png"),
              "background-fit": "contain contain",
              "background-color": "#fff",
            },
          },
          {
            selector: ".inicial.noFinal",
            css: {
              shape: "square",
              "background-image": require("../assets/nodo-i.png"),
              "background-fit": "contain cover",
              "background-color": "#fff",
            },
          },
          {
            selector: ".noInicial.final",
            css: {
              shape: "square",
              "background-image": require("../assets/nodo-f.png"),
              "background-fit": "cover cover",
              "background-color": "#fff",
            },
          },
          {
            selector: ".noInicial.noFinal",
            css: {
              shape: "square",
              "background-image": require("../assets/nodo.png"),
              "background-fit": "cover cover",
              "background-color": "#fff",
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
  mounted() {},
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
      for (let i = 0; i < this.quintupla.K.length; i++) {
        const nodo = this.quintupla.K[i];
        console.log(nodo);
        if (nodo) {
          elementos.push({
            classes: [
              this.quintupla.S.indexOf(nodo) != -1 ? "inicial" : "noInicial",
              this.quintupla.F.indexOf(nodo) != -1 ? "final" : "noFinal",
            ],
            data: { id: nodo, etiqueta: nodo },
            position: {
              x: 1,
              y: 1,
            },
            group: "nodes",
          });
        }
      }
      for (let i = 0; i < this.quintupla.s.length; i++) {
        const conexion = this.quintupla.s[i];
        const origen = conexion[0];
        const destino = conexion[2];
        const letra = conexion[1];

        if (origen && destino) {
          elementos.push({
            data: {
              id: origen + destino,
              source: origen,
              target: destino,
              weight: letra || "Ɛ",
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
    buildNodo(esFinal, esInicial, colorPrincipal, colorFlecha) {
      let data = `
        <svg id="Capa_1" data-name="Capa 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024.5 859.06">
          <defs>
            <style>.cls-1,.cls-2{fill:${colorPrincipal};}.cls-1,.cls-3{}.cls-3{fill:${
        colorFlecha ? colorFlecha : colorPrincipal
      };}</style>
            </defs>
          <circle class="cls-1" cx="594.97" cy="429.53" r="321.63"/>
          ${
            esFinal
              ? '<path class="cls-2" d="M594.47,941.53a429.63,429.63,0,0,1-167.2-825.29,429.63,429.63,0,0,1,334.4,791.52A426.79,426.79,0,0,1,594.47,941.53Zm0-799.06A369.52,369.52,0,1,0,855.77,250.7,367.14,367.14,0,0,0,594.47,142.47Z" transform="translate(0.5 -82.47)"/>'
              : ""
          }
          ${
            esInicial
              ? '<polygon class="cls-3" points="273.34 429.53 0.5 196.31 0.5 662.75 273.34 429.53"/>'
              : ""
          }
        </svg>
      `;
      return "data:image/svg+xml;base64," + btoa(data);
    },
  },
};
</script>
