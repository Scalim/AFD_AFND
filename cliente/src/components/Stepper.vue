<template>
  <section class="is-full-h">
    <b-steps
      size="is-small"
      class="is-full-h"
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
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5;"
      >
        <alfabeto-input></alfabeto-input>
      </b-step-item>
      <b-step-item
        step="2"
        label="Extremos"
        :clickable="false"
        class="is-full-h"
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5;"
      >
        <extremos></extremos>
      </b-step-item>

      <b-step-item
        step="3"
        class="is-full-h"
        label="Conexiones"
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5;"
        :clickable="false"
      >
        <aristas-input
          :nodos="nodos"
          :origenes="origenes"
          :destinos="destinos"
          :pesos="pesos"
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
          >
            Atrás
          </b-button>
          <b-button
            v-if="pasoActual != 2"
            outlined
            rounded
            type="is-primary"
            icon-pack="fas"
            icon-right="forward"
            :disabled="next.disabled || (pasoActual == 0 && !sonNodosValidos)"
            @click.prevent="next.action"
          >
            Siguiente
          </b-button>
          <b-button
            v-else
            rounded
            type="is-primary"
            icon-pack="fas"
            icon-right="forward"
            @click="onFinalizar"
          >
            Finalizar
          </b-button>
        </div>
      </template>
    </b-steps>
  </section>
</template>

<script>
import AristasInput from "./AristasInput.vue";
import NodosInput from "./NodosInput.vue";
import AlfabetoInput from "./AlfabetoInput";
import Extremos from "./Extremos";

export default {
  name: "StepperData",
  props: ["nodos", "origenes", "destinos", "pesos", "onFinalizar"],
  components: {
    AristasInput,
    NodosInput,
    AlfabetoInput,
    Extremos
  },
  data() {
    return {
      pasoActual: 0,
      prevIcon: "chevron-left",
      nextIcon: "chevron-right",
    };
  },
  updated(){
    // console.log("PASO", this.pasoActual);
  },
  computed: {
    sonNodosValidos() {
      if (!this.nodos || !this.nodos.length) {
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
