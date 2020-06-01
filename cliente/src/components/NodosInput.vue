<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <div class="is-full-h columns is-marginless is-paddingless">
      <div class="column" style="padding-right: 20px">
        <b-field grouped v-for="(nodo, i) in nodos" :key="nodo.id">
          <b-field
            expanded
            :type="validarNodo(nodo.etiqueta) != null ? 'is-danger' : ''"
            :message="validarNodo(nodo.etiqueta)"
          >
            <b-input v-model="nodos[i].etiqueta" rounded ref="input"></b-input>
          </b-field>
          <b-tooltip
            v-if="nodos.length > 1"
            label="Eliminar"
            class="is-danger"
            position="is-left"
          >
            <a @click="eliminarNodo(i)" style="margin-top: 5px;"
              ><b-icon
                pack="fa"
                class="is-danger"
                style="margin-top: 5px;"
                icon="minus-circle"
              ></b-icon
            ></a>
          </b-tooltip>
          <div v-else style="margin-top: 5px;">
            <b-icon pack="fa" icon="minus-circle" style="color: grey;"></b-icon>
          </div>
        </b-field>
        <b-button
          type="is-primary"
          outlined
          :disabled="!sonTodosValidos"
          rounded
          expanded
          @click="agregarNodo"
          icon-left="plus-circle"
          >Agregar nodo</b-button
        >
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
  name: "NodosInput",
  props: ["nodos"],
  data: () => ({
    indiceMaximo: 0,
  }),
  mounted() {
    if (!this.nodos.length) {
      this.nodos.push({
        id: this.nodos.length + 1,
        etiqueta: "A",
      });
    }
  },
  computed: {
    sonTodosValidos() {
      for (const nodo of this.nodos) {
        if (this.validarNodo(nodo)) {
          return false;
        }
      }
      return true;
    },
  },
  methods: {
    agregarNodo() {
      this.indiceMaximo++;
      var valorAsciiA = 65;
      var caracter = String.fromCharCode(valorAsciiA + this.indiceMaximo);
      this.nodos.push({
        id: this.nodos.length + 1,
        etiqueta: caracter,
      });
      this.$nextTick(() => {
        this.$refs.input[this.nodos.length - 1].focus();
      });
    },
    eliminarNodo(i) {
      this.nodos.splice(i, 1);
    },

    validarNodo(etiqueta) {
      if (etiqueta != null && etiqueta != "") {
        if (this.nodos.filter((n) => n.etiqueta == etiqueta).length > 1) {
          return "No puede repetir las etiquetas";
        }
      } else {
        return "Debe asignar una etiqueta válida";
      }
      return null;
    },
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
    },
  },
};
</script>
