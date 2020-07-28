<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
        <h1 class="title is-marginless">AFND a AFD</h1>
        <span class="subtitle"
          >Transformar Autómata Finito No Determinista a Autómata Finito
          Determinista</span
        >

        <p v-if="eraAfd != null" style="padding: 20px 0 20px 0;">
          {{
            `El autómata ${eraAfd ? "ya" : "No"} era AFD ${
              !eraAfd
                ? "y se transformó correctamente"
                : "por lo que no se transformó"
            }`
          }}
        </p>

        <b-field expanded label="Autómata" style="margin-top: 20px;">
          <b-select
            expanded
            placeholder="Selecciona un autómata"
            v-model="automata"
          >
            <option
              v-for="(automata, i) in automatas"
              :value="automata"
              :disabled="
                i == 0
                  ? $store.state.automataUnoEsVacio
                  : $store.state.automataDosEsVacio
              "
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

      <div
        class="column is-6"
        style="border-left: 2px solid #f5f5f5; "
        v-if="afd != null"
      >
        <div class="columns">
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
              >Sobreescribir Autómata 1</b-button
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
              >Sobreescribir Autómata 2</b-button
            >
          </div>
        </div>
        <grafo :quintupla="afd" />
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
    eraAfd: null,
    automatas: ["Autómata 1", "Autómata 2"],
    automata: null,
    afd: null,
  }),

  methods: {
    sobreescribir(index) {
      if (index == 1) {
        this.$store.commit("crearAutomataUno", this.afd);
      }
      if (index == 2) {
        this.$store.commit("crearAutomataDos", this.afd);
      }
    },
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
