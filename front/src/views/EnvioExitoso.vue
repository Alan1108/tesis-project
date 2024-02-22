<template>
    <div class="envio-exitoso">
      <div class="contenido">
        <div class="mensaje">
          <h1>¡Tu mensaje se ha enviado con éxito!</h1>
        </div>
        <div class="imagen">
          <img src="../img/visto.png" alt="Visto verde">
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EnvioExitoso'
  };
  </script>
  
  <style scoped>
  .envio-exitoso {
    background-color: #f8dfd4;
    border-radius: 10px;
    padding: 20px;
  }
  
  .contenido {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  
  .imagen {
    margin-top: 20px;
  }
  </style>
  