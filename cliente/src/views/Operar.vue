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
        <h1 class="title is-marginless">Operar autómatas</h1>
        <span class="subtitle"
          >Complemento, unión, concatenación e intersección</span
        >
        <b-field expanded label="Operación" style="margin-top: 10px;">
          <b-select
            expanded
            placeholder="Selecciona una operación"
            v-model="operacion"
          >
            <option
              v-for="(operacion, i) in operaciones"
              :value="operacion"
              :key="i"
            >
              {{ operacion }}
            </option>
          </b-select>
        </b-field>
        <b-field grouped style="margin: 0; margin-top: 20px;">
          <b-field expanded label="Autómata X">
            <b-select
              expanded
              placeholder="Selecciona un autómata"
              v-model="automataX"
            >
              <option
                v-for="(automata, i) in automatas"
                :value="automata"
                :key="i"
              >
                {{ automata }}
              </option>
            </b-select>
          </b-field>
          <b-field
            expanded
            label="Autómata Y"
            v-if="operacion != 'Complemento'"
          >
            <b-select
              expanded
              placeholder="Selecciona un autómata"
              v-model="automataY"
            >
              <option
                v-for="(automata, i) in automatas"
                :value="automata"
                :key="i"
              >
                {{ automata }}
              </option>
            </b-select>
          </b-field>
        </b-field>

        <b-button
          style="margin-top: 30px;"
          type="is-primary"
          outlined
          rounded
          expanded
          class="button"
          :loading="cargando"
          @click="obtenerArbol()"
          >Operar</b-button
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
    operaciones: ["Complemento", "Unión", "Concatenación", "Intersección"],
    automatas: ["Autómata 1", "Autómata 2"],
    resultado: null,
    automataX: null,
    automataY: null,
    operacion: null,
  }),

  methods: {},
};
</script>
