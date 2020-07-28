<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column" style="padding-right: 20px">
        <b-field
          v-for="(conexion, i) in conexiones"
          :key="i"
          :type="validarArista(i) != null ? 'is-danger' : ''"
          :message="validarArista(i)"
        >
          <b-field grouped class="is-marginless">
            <b-field expanded style="margin-bottom: 5px;">
              <b-autocomplete
                rounded
                v-model="conexiones[i][0]"
                :data="nodos"
                keep-first
                open-on-focus
                placeholder="Nodo de origen"
                clearable
              >
                <template slot="empty">Sin resultados</template>
              </b-autocomplete>
            </b-field>
            <b-field expanded style="margin-bottom: 5px;">
              <b-autocomplete
                rounded
                v-model="conexiones[i][2]"
                :data="nodos"
                keep-first
                open-on-focus
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
                v-model="conexiones[i][1]"
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
                  :disabled="conexiones.length <= 1"
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
  props: ["nodos", "conexiones", "alfabeto"],
  data: () => ({}),
  computed: {
    sonTodosValidos() {
      for (let i = 0; i < this.conexiones.length; i++) {
        if (this.validarArista(i).length) {
          return false;
        }
      }
      return true;
    },
  },
  methods: {
    agregarArista() {
      this.conexiones.push([null, null, null]);
    },
    eliminarArista(i) {
      this.conexiones.splice(i, 1);
    },
    invertirArista(i) {
      const conexion = this.conexiones[i];
      this.conexiones.push(conexion[2], conexion[1], conexion[0]);
    },
    validarArista(i) {
      const conexion = this.conexiones[i];

      const origen = conexion[0];
      const destino = conexion[2];

      var errores = [];

      if (!origen || origen == "") {
        errores.push("Debe seleccion un nodo de origen");
      } else if (this.nodos.indexOf(origen) == -1) {
        errores.push("Debe seleccion un nodo de origen válido");
      }

      if (!destino || destino == "") {
        errores.push("Debe seleccion un nodo de destino");
      } else if (this.nodos.indexOf(destino) == -1) {
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
