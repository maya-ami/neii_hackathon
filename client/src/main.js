import Vue from "vue";
import App from "./App.vue";
import store from "./vuex/store.js";
import "./assets/styles/styles.scss";
// import LazyLoadDirective from "./directives/LazyLoadDirective";
import VueLazyload from "vue-lazyload";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

Vue.config.productionTip = false;
// Vue.directive("lazyload", LazyLoadDirective);
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);
Vue.use(VueLazyload, {
  preLoad: 2.3,
  error: "empty.png",
  loading: "empty.png",
  attempt: 1
});
new Vue({
  render: h => h(App),
  store
}).$mount("#app");
