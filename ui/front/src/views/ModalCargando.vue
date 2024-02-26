<template>
    <div class="modal" v-if="cargando">
      <div class="modal-contenido">
        <img src="../img/load2.gif" style="max-width: 50%;" alt="Cargando...">
        <p style="font-size: 18px;">Cargando...</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ModalCargando',
    props: {
      cargando: Boolean
    }
  }
  </script>
  
  <style>
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-contenido {
    max-width: 500px;
    background-color: #e9f0f3;
    padding: 20px;
    border-radius: 5px;
    text-align: center;
  }
  </style>
  