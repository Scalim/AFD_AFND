import Vue from "vue";
import App from "./App.vue";
import Buefy from "buefy";
import VueKatex from "vue-katex";
import VueCytoscape from "vue-cytoscape";
import router from "./router";
import store from "./store";
import VueSidebarMenu from 'vue-sidebar-menu';

import "katex/dist/katex.min.css";
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;

Vue.use(Buefy);
Vue.use(VueCytoscape);
Vue.use(VueSidebarMenu);
Vue.use(VueKatex, {
  globalOptions: {},
});
Vue.prototype.$apiUrl = "http://localhost:5151";

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");