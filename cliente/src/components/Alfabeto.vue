<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <b-field label="Añadir alfabeto (No incluir vacío)">
      <b-taginput
        ellipsis
        icon="label"
        v-bind:value="value"
        @input="updateValue"
        placeholder="Agregar"
      ></b-taginput>
    </b-field>
  </div>
</template>
<script>
export default {
  name: "Alfabeto",
  props: {
    value: {
      type: Array,
    },
  },
  data: () => ({
    alfabetoActual: [],
    primero: true,
  }),
  computed: {},
  mounted() {
    if (this.alfabeto && this.alfabeto.length != 0 && this.primero) {
      this.alfabetoActual = this.alfabeto;
      this.primero = false;
    }
  },
  watch: {
    alfabeto(val) {
      if (val.length != 0 && this.primero) {
        this.alfabetoActual = val;
        this.primero = false;
      }
    },
    alfabetoActual() {
      this.alfabeto = this.alfabetoActual;
    },
  },
  methods: {
    updateValue: function(value) {
      this.$emit("input", value);
    },
  },
};
</script>
