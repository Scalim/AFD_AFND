<template>
  <section class="is-full-h">
    <b-steps
      size="is-small"
      class="is-full-h"
      style="padding: 10px 0 10px 0;"
      v-model="pasoActual"
      :animated="true"
      :rounded="true"
      :has-navigation="true"
      :icon-prev="prevIcon"
      :icon-next="nextIcon"
    >
      <b-step-item
        step="1"
        label="Alfabeto"
        :clickable="false"
        class="is-full-h"
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5; padding: 10px;"
      >
        <alfabeto v-model="alfabeto"></alfabeto>
      </b-step-item>
      <b-step-item
        step="2"
        label="Extremos"
        :clickable="false"
        class="is-full-h"
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5;  padding: 10px;"
      >
        <extremos
          :nodos="nodos"
          :finales="finales"
          :iniciales="iniciales"
        ></extremos>
      </b-step-item>

      <b-step-item
        step="3"
        class="is-full-h"
        label="Conexiones"
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5; padding: 10px;"
        :clickable="false"
      >
        <aristas-input
          :nodos="nodos"
          :origenes="origenes"
          :destinos="destinos"
          :conexiones="conexiones"
          :alfabeto="alfabeto"
        />
      </b-step-item>
      <template slot="navigation" slot-scope="{ previous, next }">
        <div
          style="heigth: 100%; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center;"
        >
          <b-button
            outlined
            rounded
            type="is-primary"
            icon-pack="fas"
            icon-left="backward"
            :disabled="previous.disabled"
            @click.prevent="previous.action"
            >Atrás</b-button
          >
          <b-button
            v-if="pasoActual != 2"
            outlined
            rounded
            type="is-primary"
            icon-pack="fas"
            icon-right="forward"
            :disabled="!puedeAvanzar"
            @click.prevent="next.action"
            >Siguiente</b-button
          >
          <b-button
            v-else
            rounded
            type="is-primary"
            icon-pack="fas"
            icon-right="forward"
            :disabled="!sonNodosValidos"
            @click="onFinalizar"
            >Finalizar</b-button
          >
        </div>
      </template>
    </b-steps>
  </section>
</template>

<script>
import AristasInput from "./AristasInput.vue";
import NodosInput from "./NodosInput.vue";
import Extremos from "./Extremos";
import Alfabeto from "./Alfabeto";

export default {
  name: "StepperData",
  props: [
    "nodos",
    "origenes",
    "destinos",
    "finales",
    "iniciales",
    "conexiones",
    "alfabeto",
    "onFinalizar",
  ],
  components: {
    AristasInput,
    NodosInput,
    Extremos,
    Alfabeto,
  },
  data() {
    return {
      pasoActual: 0,
      prevIcon: "chevron-left",
      nextIcon: "chevron-right",
    };
  },
  mounted() {},
  watch: {
    alfabeto() {
      console.log("LARGO ALFABETO: ", this.alfabeto.length);
    },
  },
  computed: {
    puedeAvanzar() {
      if (this.pasoActual == 0) {
        return this.alfabeto.length > 0;
      }
      if (this.pasoActual == 1) {
        let tieneInicial =
          this.iniciales[0] != null && this.iniciales[0] < this.nodos.length;
        let tieneFinal = false;

        for (const final of this.finales) {
          tieneFinal = tieneFinal || final;
        }
        return tieneInicial && tieneFinal;
      }
      return false;
    },
    sonNodosValidos() {
      if (this.pasoActual == 1 && (!this.alfabeto || !this.alfabeto.length)) {
        return false;
      }

      for (const nodo of this.nodos) {
        if (!nodo.etiqueta || nodo.etiqueta == "") {
          return false;
        } else {
          if (
            this.nodos.filter((n) => n.etiqueta == nodo.etiqueta).length > 1
          ) {
            return false;
          }
        }
      }
      return true;
    },
  },
};
</script>

<style>
.b-steps .steps,
.b-steps .step-navigation {
  padding: 10px;
}

.b-steps .step-navigation {
  padding-left: 20px;
  padding-right: 20px;
}
.step-content {
  padding: 0 !important;
  height: calc(100% - 65px - 56px);
}
</style>
