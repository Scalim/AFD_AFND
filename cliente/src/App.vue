<template>
  <div
    style="
    height: 100%;"
  >
    <sidebar-menu :menu="menu" hide-toggle collapsed :width="`260px`" />
    <b-modal
      :active.sync="editarGrafoModal"
      trap-focus
      destroy-on-hide
      aria-role="dialog"
      aria-modal
    >
      <ingresar-grafo :onGuardar="onGuardar" :grafoSeleccionado="grafoSeleccionado"/>
    </b-modal>
    <div style="padding: 30px; width: calc(100% - 50px); float: right">
      <div style="display: flex; justify-content: space-between;">
      <div>
        <b-button
          type="is-primary"
          inverted
          rounded
          icon-left="pencil"
          style="margin-bottom: 20px; margin-right: 20px;"
          size="is-medium"
          @click="seleccionGrafo(1)"
          >AFND 1</b-button
        >
        <b-button
          type="is-primary"
          inverted
          rounded
          icon-left="pencil"
          style="margin-bottom: 20px;"
          size="is-medium"
          @click="seleccionGrafo(2)"
          >AFND 2</b-button
        >
        </div>
        <a href="https://github.com/Scalim/AFD_AFND"
          ><b-icon style="color: white;" icon="github-circle" size="is-medium">
          </b-icon
        ></a>
      </div>

      <div class="is-flex" style="width: 100%;">
        <div
          class="card"
          style="width: 100%; height: calc(100vh - 80px - 45px); border-radius: 10px;"
        >
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const separator = {
  template: `<hr style="border-color: rgba(255, 255, 255, 0.5); margin: 20px;">`,
};
import IngresarGrafo from "./views/IngresarGrafo.vue";
export default {
  name: "App",
  components: {
    IngresarGrafo,
  },
  data() {
    return {
      editarGrafoModal: false,
      grafoSeleccionado: null,
      menu: [
        {
          href: "/",
          title: "Presentación",
          icon: "fa fa-user",
        },
        {
          component: separator,
        },
        {
          href: "/afd",
          title: "AFD equivalente",
          icon: "fa fa-table",
        },
        {
          href: "/operar",
          title: "Operar",
          icon: "fa fa-route",
        },
      ],
    };
  },
  methods: {
    seleccionGrafo(grafoSeleccionado){
      this.grafoSeleccionado = grafoSeleccionado;
      this.editarGrafoModal = true;
    },
    onGuardar() {
      this.editarGrafoModal = false;
      this.grafoSeleccionado = null;
      this.$buefy.toast.open({
        message: "El grafo se actualizó correctamente",
        type: "is-success",
      });
    },
  },
};
</script>

<style lang="scss">
@import "~bulma/sass/utilities/_all";
$primary: #e3007e;
$primary-invert: findColorInvert($primary);
$accent: #d5c699;
$accent-dark: #a46978;
$accent-invert: findColorInvert($accent);
$menu: #2c1035;
$menu-invert: findColorInvert($menu);
$colors: (
  "white": (
    $white,
    $black,
  ),
  "black": (
    $black,
    $white,
  ),
  "light": (
    $light,
    $light-invert,
  ),
  "dark": (
    $dark,
    $dark-invert,
  ),
  "primary": (
    $primary,
    $primary-invert,
  ),
  "accent": (
    $accent,
    $accent-invert,
  ),
  "menu": (
    $menu,
    $menu-invert,
  ),
  "info": (
    $info,
    $info-invert,
  ),
  "success": (
    $success,
    $success-invert,
  ),
  "warning": (
    $warning,
    $warning-invert,
  ),
  "danger": (
    $danger,
    $danger-invert,
  ),
);
.v-sidebar-menu .vsm--icon {
  background-color: transparent !important;
}
.v-sidebar-menu {
  background-color: $menu !important;
  .vsm_expanded {
    .vsm--item_open {
      .vsm--link {
        &_level-1 {
          background-color: $accent-dark !important;
          & .vsm--icon {
            background-color: $accent-dark !important;
          }
        }
      }
    }
  }
  .vsm--link.vsm--link_active,
  .vsm--link.vsm--link_exact-active {
    -webkit-box-shadow: 3px 0px 0px 0px $accent-dark inset !important;
    box-shadow: 3px 0px 0px 0px $accent-dark inset !important;
  }
  .vsm--mobile-bg {
    background-color: $accent-dark !important;
  }
}
html,
body {
  height: 100%;
  min-height: 100%;
}
body {
  background-color: $primary;
}
.is-full-h {
  height: 100% !important;
}
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>