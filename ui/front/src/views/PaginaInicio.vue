<template>
  <div class="inicio">
    <!-- Contenido de la página de Inicio -->
    <div class="contenido">
      <div class="fila">
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/Imagen3.png" style="max-width: 75%;border-radius: 15px;"></div>
          <p style="color: #15323a;"><Strong>Información del Proyecto</Strong><b></b></p><p>
            Plataforma interactiva enfocada en el análisis de imágenes de polen para detección de familias. 
            Herramienta diseñada en colaboración entre estudiantes de software de la Universidad 
            de las Fuerzas Armadas ESPE y la carrera de biotecnología.
          </p>
        </div>
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/Imagen2.png" style="max-width: 75%;border-radius: 15px;"></div>
          <p><Strong>Involucrados del Proyecto</Strong><b></b></p><p>
            Este proyecto ha sido posible gracias a la colaboración entre estudiantes de software de la Universidad de 
            las Fuerzas Armadas ESPE y la carrera de biotecnología. Juntos, se desarrolló una plataforma 
            con el objetivo de mejorar la 
            eficiencia y precisión en el análisis de imágenes de polen.
          </p>
        </div>
      </div>
      <div class="fila">
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/Imagen5.png" style="max-width: 75%;border-radius: 15px;"></div>
          <p><Strong>Como funciona el Proyecto</Strong><b></b></p><p>
            El funcionamiento es sencillo y eficiente. Los usuarios seleccionan una imagen de polen 
            y la cargan en la plataforma. Utilizando un modelo de clasificación desarrollado en Roboflow, la plataforma 
            analiza la imagen y determina las familias polínicas presentes.
          </p>
        </div>
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/imagen1.png" style="max-width: 75%;border-radius: 15px;"></div>
          <p><Strong>Usuarios Objetivo del Proyecto</Strong><b></b></p><p>
            Nuestra plataforma está dirigida principalmente a estudiantes e investigadores del área de biotecnología de
            la Universidad de las Fuerzas Armadas ESPE. Sin embargo, su diseño intuitivo y fácil de usar la hace accesible 
            para cualquier persona interesada en el análisis de imágenes de polen.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: 'PaginaInicio',
    // Aquí puedes agregar métodos, datos, etc., según sea necesario
  }
  </script>
  
  <style>
  .contenido {
    text-align:justify;
    display: flex; /* Usa flexbox para distribuir los elementos */
    flex-direction: column; /* Alinear los elementos en columnas */
  }

  .fila {
    display: flex; /* Usa flexbox para distribuir los elementos */
    flex-direction: row; /* Alinear los elementos en filas */
  }

  .parrafo {
    border: 2px solid #15323a;
    border-radius: 19px;
    flex: 1; /* Ocupa todo el espacio disponible */
    margin: 25px;
    padding: 20px; /* Añade espacio alrededor de los párrafos */
    font-family: 'Avenir', Helvetica, Arial, sans-serif; /* Utiliza la misma fuente que el menú */
    color: #15323a; /* Color de texto blanco */
    box-sizing: border-box;
    box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.2); /* Incluir el borde en el tamaño del elemento */
  }

  @media only screen and (max-width: 600px) {
    /* Estilos para dispositivos con ancho máximo de 600px (como dispositivos móviles) */
    .fila {
    display: flex; /* Usa flexbox para distribuir los elementos */
    flex-direction: column; /* Alinear los elementos en filas */
    }
  }
  
</style>
  