<template>
  <div class="is-flex" style="width: 100%;">
    <div
      class="card"
      style="width: 100%; height: calc(100vh - 80px - 45px); border-radius: 10px;"
    >
      <div class="is-full-h" style="padding: 20px;">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div class="column is-paddingless is-7">
            <stepper
              :nodos="nodos"
              :origenes="origenes"
              :destinos="destinos"
              :pesos="pesos"
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
              :pesos="pesos"
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
  props: ["onFinalizar", "grafoSeleccionado"],
  components: {
    Stepper,
    Grafo,
  },
  data: () => ({
    nodos: [],
    origenes: [],
    destinos: [],
    pesos: [],
  }),
  mounted() {
    if(this.grafoSeleccionado == 1){
      this.nodos = this.$store.state.nodos;
      this.origenes = this.$store.state.origenes;
      this.destinos = this.$store.state.destinos;
      this.pesos = this.$store.state.pesos;
    } else if(this.grafoSeleccionado == 2){
      this.nodos = this.$store.state.nodos;
      this.origenes = this.$store.state.origenes;
      this.destinos = this.$store.state.destinos;
      this.pesos = this.$store.state.pesos;
    }
  },
  methods: {
    onFinalizar() {
      this.$store.commit("crearGrafo", {
        nodos: this.nodos,
        origenes: this.origenes,
        destinos: this.destinos,
        pesos: this.pesos,
      });
    },
  },
};
</script>
