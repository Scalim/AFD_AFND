<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column" style="padding-right: 20px">
        <b-field
          v-for="(origen, i) in origenes"
          :key="i"
          :type="validarArista(i) != null ? 'is-danger' : ''"
          :message="validarArista(i)"
        >
          <b-field grouped class="is-marginless">
            <b-field expanded style="margin-bottom: 5px;">
              <b-autocomplete
                rounded
                v-model="origenes[i]"
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
            <b-field expanded style="margin-bottom: 5px;">
              <b-autocomplete
                rounded
                v-model="destinos[i]"
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
            <b-field expanded style="margin-bottom: -12px;">
              <b-numberinput
                controls-position="compact"
                controls-rounded
                style="max-width: 200px"
                min="0"
                v-model="pesos[i]"
              ></b-numberinput>
            </b-field>

            <b-tooltip
              v-if="origenes.length > 1"
              label="Eliminar"
              class="is-danger"
              position="is-left"
              style="margin-top: -25px;"
            >
              <a @click="eliminarArista(i)" style="margin-top: 30px;">
                <b-icon
                  pack="fa"
                  class="is-danger"
                  icon="minus-circle"
                ></b-icon>
              </a>
            </b-tooltip>
            <div v-else style="margin-top: 5px;">
              <b-icon
                pack="fa"
                icon="minus-circle"
                style="color: grey;"
              ></b-icon>
            </div>
          </b-field>
        </b-field>
        <div class="is-marginless is-paddingless">
          <b-button
            type="is-primary"
            outlined
            rounded
            :disabled="!sonTodosValidos"
            expanded
            @click="agregarArista"
            icon-left="plus-circle"
            >Agregar arista</b-button
          >
        </div>
      </div>
    </div>
  </div>
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
  name: "AristasInput",
  props: ["nodos", "origenes", "destinos", "pesos"],
  data: () => ({
    config: {
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
  mounted() {},
  computed: {
    sonTodosValidos() {
      for (let i = 0; i < this.origenes.length; i++) {
        if (this.validarArista(i).length) {
          return false;
        }
      }
      return true;
    },
  },
  methods: {
    agregarArista() {
      this.origenes.push(null);
      this.destinos.push(null);
      this.pesos.push(0);
    },
    eliminarArista(i) {
      this.origenes.splice(i, 1);
      this.destinos.splice(i, 1);
      this.pesos.splice(i, 1);
    },
    validarArista(i) {
      const origen = this.origenes[i];
      const destino = this.destinos[i];
      const peso = this.pesos[i];

      var errores = [];

      if (!origen || origen == "") {
        errores.push("Debe seleccion un nodo de origen");
      } else if (!this.nodos.filter((n) => n.etiqueta == origen).length) {
        errores.push("Debe seleccion un nodo de origen válido");
      }

      if (!destino || destino == "") {
        errores.push("Debe seleccion un nodo de destino");
      } else if (!this.nodos.filter((n) => n.etiqueta == destino).length) {
        errores.push("Debe seleccion un nodo de destino válido");
      }

      if (peso == null || peso < 0) {
        errores.push("Debe ingresar un peso válido");
      }
      return errores;
    },

    getNodosFiltrados(valor) {
      if (valor != null) {
        return this.nodos.filter((n) => {
          n.toString()
            .toLowerCase()
            .includes(valor.toString().toLowerCase);
        });
      }
      return this.nodos;
    },
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
    },
  },
};
</script>
