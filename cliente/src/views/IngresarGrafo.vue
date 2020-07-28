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
              :conexiones="conexiones"
              :nodos="nodos"
              :alfabeto="alfabeto"
              :iniciales="iniciales"
              :finales="finales"
              :indiceInicio="grafoSeleccionado"
              :onFinalizar="onFinalizar"
            />
          </div>
          <div
            class="column is-paddingless is-5"
            style="border-left: 2px solid #f5f5f5; "
          >
            <grafo :quintupla="quintupla" />
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
  data() {
    return {
      nodos: [],
      iniciales: [],
      alfabeto: [],
      finales: [],
      conexiones: [],
    };
  },
  computed: {
    quintupla() {
      return {
        K: this.nodos,
        S: this.iniciales,
        E: this.alfabeto,
        F: this.finales,
        s: this.conexiones,
      };
    },
  },
  mounted() {
    if (this.grafoSeleccionado == 1 && !this.$store.state.automataUnoEsVacio) {
      this.nodos = this.$store.state.automataUno.K;
      this.iniciales = this.$store.state.automataUno.S;
      this.alfabeto = this.$store.state.automataUno.E;
      this.finales = this.$store.state.automataUno.F;
      this.conexiones = this.$store.state.automataUno.s;
    } else if (
      this.grafoSeleccionado == 2 &&
      !this.$store.state.automataDosEsVacio
    ) {
      this.nodos = this.$store.state.automataDos.K;
      this.iniciales = this.$store.state.automataDos.S;
      this.alfabeto = this.$store.state.automataDos.E;
      this.finales = this.$store.state.automataDos.F;
      this.conexiones = this.$store.state.automataDos.s;
    }
  },
  watch: {
    grafoSeleccionado: function() {
      if (
        this.grafoSeleccionado == 1 &&
        !this.$store.state.automataUnoEsVacio
      ) {
        this.nodos = this.$store.state.automataUno.K;
        this.iniciales = this.$store.state.automataUno.S;
        this.alfabeto = this.$store.state.automataUno.E;
        this.finales = this.$store.state.automataUno.F;
        this.conexiones = this.$store.state.automataUno.s;
      } else if (
        this.grafoSeleccionado == 2 &&
        !this.$store.state.automataDosEsVacio
      ) {
        this.nodos = this.$store.state.automataDos.K;
        this.iniciales = this.$store.state.automataDos.S;
        this.alfabeto = this.$store.state.automataDos.E;
        this.finales = this.$store.state.automataDos.F;
        this.conexiones = this.$store.state.automataDos.s;
      }
    },
  },
  methods: {
    onFinalizar() {
      if (this.grafoSeleccionado == 1) {
        this.$store.commit("crearAutomataUno", this.quintupla);
      }
      if (this.grafoSeleccionado == 2) {
        this.$store.commit("crearAutomataDos", this.quintupla);
      }
      this.onGuardar();
    },
  },
};
</script>
