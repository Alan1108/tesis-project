<template>
  <div id="app">
    <!-- Menú horizontal -->
    <nav class="menu">
      <ul>
        <li><router-link to="/" class="menu-link">Inicio</router-link></li>
        <li><router-link to="/reconocimiento" class="menu-link">Reconocimiento</router-link></li>
        <li><router-link to="/contacto" class="menu-link">Contacto</router-link></li>
      </ul>
    </nav>

    <!-- Contenido de la página actual (determinado por la ruta) -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  // Aquí puedes agregar métodos, datos, etc., según sea necesario
  
  
}

</script>

<style>
body{
  margin: 0;
  background-color: #c69774;
  box-sizing: border-box; /* Asegura que el ancho y alto incluyan el padding y borde */
}
#app {
  margin: 0;
  padding: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #c69774;
}

/* Estilos para el menú horizontal */
.menu {
  background-color: #637e76;
  padding: 3px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.2);
}

.menu ul {
  list-style-type: none;
  padding: 0;
}

.menu ul li {
  display: inline;
  margin-right: 50px;
}

.menu-link {
  font-weight: bold;
  color: white;
  text-decoration: none; /* Para evitar subrayado en los enlaces */
}
</style>
