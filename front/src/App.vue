<template>
  <div id="app">
    <!-- Menú horizontal -->
    <nav class="menu">
      <ul>
        <li><router-link to="/" class="menu-link"><img src="./img/inicio.png">Inicio</router-link></li>
        <li><router-link to="/reconocimiento" class="menu-link"><img src="./img/clasificar.png">Reconocimiento</router-link></li>
        <li><router-link to="/contacto" class="menu-link"><img src="./img/contactos.png">Contacto</router-link></li>
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
  color: #15323a;
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
  background-color: #ffffff;
}

/* Estilos para el menú horizontal */
.menu {
  background-color: #15323a;
  padding: 3px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.2);
}

.menu ul {
  font-size: 18px;
  align-items: center;
  padding: 0;
}
li:hover{
  background-color: #2380a8;
}

.menu ul li {
  vertical-align: middle;
  display: inline;
  border-radius: 10px;
  margin-right: 60px;
  padding: 10px;
}

.menu-link {
  vertical-align: middle;
  font-weight: bold;
  color: white;
  text-decoration: none; /* Para evitar subrayado en los enlaces */
}
p{
  color: #15323a;
}
ul li img{
  vertical-align: middle;
  padding-right: 7px;
  max-width: 25px;
 
}
</style>
