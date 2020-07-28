<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
        <h1 class="title is-marginless">Simplificar</h1>
        <span class="subtitle">Simplificar Autómata Finito Determinista</span>

        <b-button
          style="margin-top: 20px;"
          type="is-primary"
          outlined
          rounded
          expanded
          class="button"
          :loading="cargando"
          @click="obtenerArbol()"
          >Simplificar</b-button
        >
      </div>

      <div class="column is-6" style="border-left: 2px solid #f5f5f5; ">
        <grafo
          :nodos="$store.state.nodos"
          :origenes="$store.state.origenes"
          :destinos="$store.state.destinos"
          :pesos="$store.state.pesos"
        />
        <div class="columns" v-if="resultado != null">
          <div class="column is-6">
            <b-button
              style="margin-top: 20px;"
              type="is-primary"
              outlined
              rounded
              expanded
              class="button"
              :loading="cargando"
              @click="sobreescribir(1)"
              >Sobreescribir Autómata 1 con este resultado</b-button
            >
          </div>
          <div class="column is-6">
            <b-button
              style="margin-top: 20px;"
              type="is-primary"
              outlined
              rounded
              expanded
              class="button"
              :loading="cargando"
              @click="sobreescribir(2)"
              >Sobreescribir Autómata 2 con este resultado</b-button
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Grafo from "../components/Grafo.vue";

export default {
  components: {
    Grafo,
  },
  data: () => ({
    cargando: false,
    resultado: null,
  }),
  methods: {
    sobreescribir(automata){
      if(automata == 1){
        this.$store.commit("crearAutomataUno", {

        });
      } else {
        this.$store.commit("crearAutomataDos", {

        })
      }
    }
  },
};
</script>
