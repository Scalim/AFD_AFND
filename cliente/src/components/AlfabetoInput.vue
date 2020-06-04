<template>
  <div>
    <b-field label="Ingresar alfabeto posible">
      <b-taginput :value="alfabeto"></b-taginput>
    </b-field>
    <b-field expanded label="Cantidad de nodos">
      <b-numberinput controls-position="compact" controls-rounded style="max-width: 200px" min="0"></b-numberinput>
    </b-field>
  </div>
</template>
<script>
export default {
  name: "AlfabetoInput",
  data() {
    return {
      alfabeto: null
    };
  },
  watch:{
      alfabeto(){
          this.console.log("ALFABETO:", this.alfabeto);
      }
  },
  methods: {}
};
</script>