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
        <p class="subtitle is-5 is-center">{{ nodo }}</p>
      </div>
      <div class="column">
        <b-radio
          name="inicial"
          v-model="inicialesActual[0]"
          :native-value="nodo"
          >Inicial</b-radio
        >
      </div>
      <div class="column">
        <b-switch v-model="finalesBoleanos[i]">Final</b-switch>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Extremos",
  props: ["nodos", "finales", "iniciales", "indiceInicio"],
  data() {
    return {
      cantidad: 0,
      finalesBoleanos: [],
      inicialesActual: [],
      primero: true,
    };
  },
  mounted() {
    for (let i = 0; i < this.cantidad; i++) {
      this.finalesBoleanos[i] = false;
    }

    if (this.nodos.length != 0 && this.primero) {
      this.cantidad = this.nodos.length;
      this.inicialesActual = this.iniciales;
      let finalesBooleanosCopia = [...this.finalesBooleanos];
      for (const final of this.finales) {
        finalesBooleanosCopia[this.nodos.indexOf(final)] = true;
      }
      this.finalesBoleanos = finalesBooleanosCopia;
      this.primero = false;
    }
  },
  watch: {
    finalesBoleanos(val) {
      while (this.finales.length) {
        this.finales.pop();
      }

      for (let i = 0; i < val.length; i++) {
        const esFinal = val[i];
        if (esFinal) {
          this.finales.push(this.nodos[i]);
        }
      }
    },
    nodos() {
      if (this.nodos.length != 0 && this.primero) {
        this.cantidad = this.nodos.length;
        this.inicialesActual = this.iniciales;
        this.primero = false;
      }
    },
    inicialActual() {
      this.iniciales = this.inicialesActual;
    },
    cantidad: function() {
      if (this.cantidad > this.nodos.length) {
        this.nodos.push(
          `${this.indiceInicio == 1 ? "Q" : "P"}${this.nodos.length + 1}`
        );
        this.finalesBoleanos.push(false);
      } else if (this.cantidad < this.nodos.length) {
        this.nodos.pop();
        this.finales = this.finales.filter((f) => this.nodos.indexOf(f) != -1);
        this.inicialesActual = this.inicialesActual.filter(
          (i) => this.nodos.indexOf(i) != -1
        );
      }
    },
  },
  methods: {},
};
</script>
