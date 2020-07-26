<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <b-field label="Añadir alfabeto (No incluir vacío)">
      <b-taginput
        v-model="alfabetoActual"
        ellipsis
        icon="label"
        placeholder="Agregar"
      ></b-taginput>
    </b-field>
  </div>
</template>
<script>
export default {
  name: "Alfabeto",
  props: ["alfabeto"],
  data: () => ({
    alfabetoActual: [],
    primero: true,
  }),
  mounted() {
    if(this.alfabeto.length != 0 && this.primero){
      this.alfabetoActual = this.alfabeto;
      this.primero = false;
    }
  },
  watch: {
    alfabeto(){
      if(this.alfabeto.length != 0 && this.primero){
        this.alfabetoActual = this.alfabeto;
        this.primero = false;
      }
    },
    alfabetoActual() {
      this.alfabeto = this.alfabetoActual;
    },
  },
  methods: {},
};
</script>
