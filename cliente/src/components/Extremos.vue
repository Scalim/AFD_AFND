<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <div style=" padding-bottom: 30px;">
      <b-field label="Cantidad de nodos">
        <b-numberinput
          controls-position="compact"
          controls-rounded
          style="max-width: 200px"
          min="0"
          v-model="cantidad"
        ></b-numberinput>
      </b-field>
    </div>
    <div class="columns is-mobile" v-for="(nodo, i) in nodos" :key="i">
      <div class="column">
        <p class="subtitle is-5 is-center">{{ nodo.etiqueta }}</p>
      </div>
      <div class="column">
        <b-radio name="inicial" v-model="inicialActual[0]" :native-value="i"
          >Inicial</b-radio
        >
      </div>
      <div class="column">
        <b-switch v-model="finales[i]">Final</b-switch>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Extremos",
  props: ["nodos", "finales", "iniciales"],
  data() {
    return {
      cantidad: 0,
      inicialActual: [],
      primero: true
    };
  },
  mounted() {
    if(this.nodos.length != 0 && this.primero){
      this.cantidad = this.nodos.length;
      this.inicialActual = this.iniciales;
      this.primero = false;
    }
  },
  watch: {
    nodos (){
      if(this.nodos.length != 0 && this.primero){
        this.cantidad = this.nodos.length;
        this.inicialActual = this.iniciales;
        this.primero = false;
      }
    },
    inicialActual() {
      this.iniciales = this.inicialActual;
    },
    cantidad: function() {
      if (this.cantidad > this.nodos.length) {
        this.nodos.push({
          id: this.nodos.length,
          etiqueta: `Q${this.nodos.length}`,
        });
        this.finales.push(false);
      } else if (this.cantidad < this.nodos.length) {
        this.nodos.pop();
        this.finales.pop();
        if (this.inicialActual[0] >= this.nodos.length) {
          this.inicialActual = [];
        }
      }
    },
  },
  methods: {},
};
</script>
