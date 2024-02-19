import { createRouter, createWebHistory } from 'vue-router';
import Inicio from './views/PaginaInicio.vue';
import Reconocimiento from './views/PaginaReconocimiento.vue';
import Contacto from './views/PaginaContacto.vue';
import Resultado from './views/PaginaResultado.vue';

const routes = [
  { path: '/', component: Inicio },
  { path: '/reconocimiento', component: Reconocimiento },
  { path: '/contacto', component: Contacto },
  { path: '/resultado', name: 'PaginaResultado', component: Resultado }
];

const router = createRouter({
  history: createWebHistory(),
  base: process.env.BASE_URL,
  routes
});

export default router;