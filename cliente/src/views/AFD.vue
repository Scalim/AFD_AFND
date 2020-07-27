<template>
<<<<<<< HEAD
  <div class="is-flex" style="width: 100%;">
    <div
      class="card"
      style="width: 100%; height: calc(100vh - 80px - 45px); border-radius: 10px;"
    >
      <div class="is-full-h" style="padding: 20px;">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div class="column is-paddingless is-7">
            
          </div>
          <div
            class="column is-paddingless is-5"
            style="border-left: 2px solid #f5f5f5; "
          >
            
=======
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
        <h1 class="title is-marginless">AFND a AFD</h1>
        <span class="subtitle"
          >Transformar Autómata Finito No Determinista a Autómata Finito
          Determinista</span
        >

        <b-button
          style="margin-top: 20px;"
          type="is-primary"
          outlined
          rounded
          expanded
          class="button"
          :loading="cargando"
          @click="obtenerArbol()"
          >Transformar</b-button
        >
      </div>

      <div class="column is-6" style="border-left: 2px solid #f5f5f5; ">
        <grafo
          :nodos="$store.state.nodos"
          :origenes="$store.state.origenes"
          :destinos="$store.state.destinos"
          :pesos="$store.state.pesos"
        />
        <div class="columns" v-if="afd != null">
          <div class="column is-6">
            <b-button
              style="margin-top: 20px;"
              type="is-primary"
              outlined
              rounded
              expanded
              class="button"
              :loading="cargando"
              @click="obtenerArbol()"
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
              @click="obtenerArbol()"
              >Sobreescribir Autómata 2 con este resultado</b-button
            >
>>>>>>> 506e0c61f9e12cb233c2ea6af1fb1443d5369a0c
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
  name: "MatrizCaminos",
  components: {
    Grafo,
  },
  data: () => ({
    cargando: false,
    afd: null,
  }),

  methods: {},
};
</script>
