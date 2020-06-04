<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <div v-for="(nodo, index) in nodos" :key="index" >
      <b-field expanded>
        <b-input :placeholder="`Q${index}`" disabled></b-input>
        <b-switch :v-model="inicio">Inicio</b-switch>
        <b-switch :v-model="finales[index]">Final</b-switch>
      </b-field>
    </div>
  </div>
</template>
<script>
export default {
  name: "Extremos",
  data() {
    return {
      nodos: 5,
      inicio: null,
      finales: []
    };
  },
  watch: {
    inicio() {
      console.log("INICIO:", this.inicio);
    },
    finales() {
      console.log("INICIO:", this.finales);
    }
  },
  methods: {}
};
</script>