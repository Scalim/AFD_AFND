<template>
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
          @click="obtener()"
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
              @click="sobreescribir()"
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
              @click="sobreescribir()"
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
    operaciones: ["Complemento", "Unión", "Concatenación", "Intersección"],
    automatas: ["Autómata 1", "Autómata 2"],
    resultado: null,
    automataX: null,
    automataY: null,
    operacion: null,
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
    },
    obtener(){
      var automataUno;
      var automataDos;
      var nombre;
      var data;

      if(this.operaciones.indexOf(this.operacion) == 0){
        nombre = "complemento";
        if(this.automatas.indexOf(this.automataX) == 0){
          data = [this.$store.getters.automataUno];
        } else {
          data = [this.$store.getters.automataDos];
        }
      } else if (this.operaciones.indexOf(this.operacion) == 1){
        nombre = "union";
        if(this.automatas.indexOf(this.automataX) == 0 && this.automatas.indexOf(this.automataY) == 0){
          data = [this.$store.getters.automataUno, this.$store.getters.automataUno];
        } else if(this.automatas.indexOf(this.automataX) == 0 && this.automatas.indexOf(this.automataY) == 1){
          data = [this.$store.getters.automataUno, this.$store.getters.automataDos];
        } else if(this.automatas.indexOf(this.automataX) == 1 && this.automatas.indexOf(this.automataY) == 0){
          data = [this.$store.getters.automataDos, this.$store.getters.automataUno];
        } else {
          data = [this.$store.getters.automataDos, this.$store.getters.automataDos];
        }
      } else if (this.operaciones.indexOf(this.operacion) == 2){
        nombre = "concatenacion";
        if(this.automatas.indexOf(this.automataX) == 0 && this.automatas.indexOf(this.automataY) == 0){
          data = [this.$store.getters.automataUno, this.$store.getters.automataUno];
        } else if(this.automatas.indexOf(this.automataX) == 0 && this.automatas.indexOf(this.automataY) == 1){
          data = [this.$store.getters.automataUno, this.$store.getters.automataDos];
        } else if(this.automatas.indexOf(this.automataX) == 1 && this.automatas.indexOf(this.automataY) == 0){
          data = [this.$store.getters.automataDos, this.$store.getters.automataUno];
        } else {
          data = [this.$store.getters.automataDos, this.$store.getters.automataDos];
        }
      } else {
        nombre = "interseccion";
        if(this.automatas.indexOf(this.automataX) == 0 && this.automatas.indexOf(this.automataY) == 0){
          data = [this.$store.getters.automataUno, this.$store.getters.automataUno];
        } else if(this.automatas.indexOf(this.automataX) == 0 && this.automatas.indexOf(this.automataY) == 1){
          data = [this.$store.getters.automataUno, this.$store.getters.automataDos];
        } else if(this.automatas.indexOf(this.automataX) == 1 && this.automatas.indexOf(this.automataY) == 0){
          data = [this.$store.getters.automataDos, this.$store.getters.automataUno];
        } else {
          data = [this.$store.getters.automataDos, this.$store.getters.automataDos];
        }
      }
      axios.post(`${this.$apiUrl}/operar`,{
        'operacion': nombre,
        'automatas': data
      })
      .then( r => {
        console.log("RESULTADO: ", r.data);
        this.resultado = r.data;
      })
      .catch(e => {
        console.log(e);
      })
    }
  },
};
</script>
