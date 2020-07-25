<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <div class="columns is-mobile" v-for="(nodo, index) in nodos" :key="index">
      <div class="column">
        <p class="subtitle is-5 is-center">{{nodo.etiqueta}}</p>
      </div>
      <div class="column">
        <b-switch v-model="iniciales[index]">Inicial</b-switch>
      </div>
      <div class="column">
        <b-switch v-model="finales[index]">Final</b-switch>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Extremos",
  props: ["nodos"],
  data() {
    return {
      inicioIndex: null,
      iniciales: [],
      finales: []
    };
  },
  mounted(){
    this.nodos.forEach(nodo => {
      this.iniciales.push(nodo.inicial);
      this.finales.push(nodo.final);
    });
  },
  watch: {
    iniciales: function() {
      if (this.inicioIndex != null) {
        this.iniciales[this.inicioIndex] = false;
        this.nodos[this.inicioIndex].inicial = false;
        this.inicioIndex = null;
      }
      for (let index = 0; index < this.iniciales.length; index++) {
        if (this.iniciales[index]) {
          this.inicioIndex = index;
          this.nodos[index].inicial = true;
        }
      }
    },
    finales: function(){
      for (let index = 0; index < this.finales.length; index++) {
        this.nodos[index].final = this.finales[index];
      }
    }
  },
  methods: {}
};
</script>