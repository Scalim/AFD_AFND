<template>
  <div class="is-flex" style="width: 100%;">
    <div
      class="card"
      style="width: 100%; height: calc(100vh - 80px - 45px); border-radius: 10px;"
    >
      <div class="is-full-h">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div class="column is-paddingless is-7">
            <stepper
              :nodos="nodos"
              :origenes="origenes"
              :destinos="destinos"
              :conexiones="conexiones"
              :alfabeto="alfabeto"
              :iniciales="iniciales"
              :finales="finales"
              :onFinalizar="onFinalizar"
            />
          </div>
          <div
            class="column is-paddingless is-5"
            style="border-left: 2px solid #f5f5f5; "
          >
            <grafo
              :nodos="nodos"
              :origenes="origenes"
              :destinos="destinos"
              :finales="finales"
              :iniciales="iniciales"
              :conexiones="conexiones"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Stepper from "../components/Stepper.vue";
import Grafo from "../components/Grafo.vue";

export default {
  name: "Main",
  props: ["onGuardar", "grafoSeleccionado"],
  components: {
    Stepper,
    Grafo,
  },
  data: () => ({
    nodos: [],
    origenes: [],
    destinos: [],
    conexiones: [],
    iniciales: [],
    finales: [],
    alfabeto: [],
  }),
  mounted() {
    if (this.grafoSeleccionado == 1) {
      this.nodos = this.$store.state.nodosUno;
      this.origenes = this.$store.state.origenesUno;
      this.destinos = this.$store.state.destinosUno;
      this.conexiones = this.$store.state.conexionesUno;
      this.alfabeto = this.$store.state.alfabetoUno;
      this.iniciales = this.$store.state.inicialesUno;
      this.finales = this.$store.state.finalesUno;
    }
    if (this.grafoSeleccionado == 2) {
      this.nodos = this.$store.state.nodosDos;
      this.origenes = this.$store.state.origenesDos;
      this.destinos = this.$store.state.destinosDos;
      this.conexiones = this.$store.state.conexionesDos;
      this.alfabeto = this.$store.state.alfabetoDos;
      this.iniciales = this.$store.state.inicialesDos;
      this.finales = this.$store.state.finalesDos;
    }
  },
  watch: {
    grafoSeleccionado: function () {
      if (this.grafoSeleccionado == 1) {
        this.nodos = this.$store.state.nodosUno;
        this.origenes = this.$store.state.origenesUno;
        this.destinos = this.$store.state.destinosUno;
        this.conexiones = this.$store.state.conexionesUno;
        this.alfabeto = this.$store.state.alfabetoUno;
        this.iniciales = this.$store.state.inicialesUno;
        this.finales = this.$store.state.finalesUno;
      }
      if (this.grafoSeleccionado == 2) {
        this.nodos = this.$store.state.nodosDos;
        this.origenes = this.$store.state.origenesDos;
        this.destinos = this.$store.state.destinosDos;
        this.conexiones = this.$store.state.conexionesDos;
        this.alfabeto = this.$store.state.alfabetoDos;
        this.iniciales = this.$store.state.inicialesDos;
        this.finales = this.$store.state.finalesDos;
      }
    }
  },
  methods: {
    onFinalizar() {
      if (this.grafoSeleccionado == 1) {
        this.$store.commit("crearAutomataUno", {
          nodos: this.nodos,
          origenes: this.origenes,
          destinos: this.destinos,
          conexiones: this.conexiones,
          alfabeto: this.alfabeto,
          iniciales: this.iniciales,
          finales: this.finales
        });
      }
      if (this.grafoSeleccionado == 2) {
        this.$store.commit("crearAutomataDos", {
          nodos: this.nodos,
          origenes: this.origenes,
          destinos: this.destinos,
          conexiones: this.conexiones,
          alfabeto: this.alfabeto,
          iniciales: this.iniciales,
          finales: this.finales
        });
      }
      this.onGuardar();
    },
  },
};
</script>
