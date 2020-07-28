<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
        <h1 class="title is-marginless">AFND a AFD</h1>
        <span class="subtitle"
          >Transformar Autómata Finito No Determinista a Autómata Finito
          Determinista</span
        >

        <b-field expanded label="Autómata">
          <b-select
            expanded
            placeholder="Selecciona un autómata"
            v-model="automata"
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

        <b-button
          style="margin-top: 20px;"
          type="is-primary"
          outlined
          rounded
          expanded
          class="button"
          :loading="cargando"
          @click="transformar()"
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
              @click="sobreescribir(1)"
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
  name: "MatrizCaminos",
  components: {
    Grafo,
  },
  data: () => ({
    cargando: false,
    eraAfd: null,
    automatas: ["Autómata 1", "Autómata 2"],
    automata: null,
    afd: null,
  }),

  methods: {
    sobreescribir(index) {},
    transformar() {
      this.cargando = true;
      var data;
      if (this.automata == "Autómata 1") {
        data = this.$store.getters.automataUno;
      } else {
        data = this.$store.getters.automataDos;
      }

      axios({
        method: "post",
        url: this.$apiUrl + "/transformar",
        data: data,
      })
        .then((r) => {
          this.cargando = false;
          this.afd = r.data.transformado;
          this.eraAfd = r.data.eraAfd;
        })
        .catch((e) => {
          this.cargando = false;
        });
    },
  },
};
</script>
