<template>
  <div class="is-full-h" style="padding: 20px; overflow-y: scroll;">
    <b-field label="Añadir alfabeto (No incluir vacío)">
      <b-taginput v-model="nuevoAlfabeto" ellipsis icon="label" placeholder="Agregar"></b-taginput>
    </b-field>
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
</template>
<script>
export default {
  name: "Alfabeto",
  props: ["alfabeto", "nodos"],
  data() {
    return {
        cantidad: null,
        nuevoAlfabeto: []
    };
  },
  mounted(){
      this.cantidad = this.nodos.length;
      this.nuevoAlfabeto = this.alfabeto;
  },
  watch: {
    cantidad: function(){
        if(this.cantidad > this.nodos.length){
            this.nodos.push({
                id: this.nodos.length,
                etiqueta: `Q${this.nodos.length}`,
                inicial: false,
                final: false
            });
        } else if(this.cantidad < this.nodos.length){
            this.nodos.pop();
        }
    },
    nuevoAlfabeto: function(){
        this.alfabeto = this.nuevoAlfabeto;
    }
  },
  methods: {}
};
</script>