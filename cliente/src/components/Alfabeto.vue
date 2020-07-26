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
  }),
  mounted() {
    this.alfabetoActual = this.alfabeto;
  },
  watch: {
    alfabetoActual() {
      console.log("cambio alfabetoActual", this.alfabetoActual);
      this.alfabeto = this.alfabetoActual;
    },
  },
  methods: {},
};
</script>
