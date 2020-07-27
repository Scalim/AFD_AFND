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
            <b-field expanded style="margin-bottom: 5px;">
              <b-autocomplete
                rounded
                :data="alfabeto"
                keep-first
                open-on-focus
                v-model="conexiones[i]"
                field="etiqueta"
                placeholder="Ɛ"
                clearable
              >
                <template slot="empty">Sin resultados</template>
              </b-autocomplete>
            </b-field>

            <v-tooltip left>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  color="error"
                  :disabled="validarArista(i).length > 0"
                  @click="invertirArista(i)"
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-swap-horizontal-bold</v-icon>
                </v-btn>
              </template>
              <span>Invertido</span>
            </v-tooltip>
            <v-tooltip left>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  color="error"
                  :disabled="origenes.length <= 1"
                  @click="eliminarArista(i)"
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-minus-circle</v-icon>
                </v-btn>
              </template>
              <span>Eliminar</span>
            </v-tooltip>
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
  props: ["nodos", "origenes", "conexiones", "destinos", "alfabeto"],
  data: () => ({}),
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
      this.conexiones.push(null);
    },
    eliminarArista(i) {
      this.origenes.splice(i, 1);
      this.destinos.splice(i, 1);
      this.conexiones.splice(i, 1);
    },
    invertirArista(i) {
      this.origenes.push(this.destinos[i]);
      this.destinos.push(this.origenes[i]);
      this.conexiones.push(this.conexiones[i]);
    },
    validarArista(i) {
      const origen = this.origenes[i];
      const destino = this.destinos[i];
      const conexion = this.conexiones[i];

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
  },
};
</script>
