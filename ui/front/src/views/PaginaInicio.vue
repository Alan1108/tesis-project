<template>
  <div class="inicio">
    <!-- Contenido de la página de Inicio -->
    <div class="contenido">
      <div class="fila">
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/analisis.png" style="max-width: 20%;"></div>
          <p style="color: #15323a;"><Strong>Información del Proyecto</Strong><b></b></p><p>
            Nuestra plataforma interactiva se enfoca en el análisis de imágenes de polen para detectar familias. 
            Es una herramienta innovadora diseñada en colaboración entre estudiantes de software de la Universidad 
            de las Fuerzas Armadas ESPE y la carrera de biotecnología. Su objetivo es proporcionar una solución 
            eficaz para el análisis de imágenes de polen, con aplicaciones importantes en la investigación científica 
            y la biotecnología.
          </p>
        </div>
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/participantes.png" style="max-width: 37%;"></div>
          <p><Strong>Involucrados del Proyecto</Strong><b></b></p><p>
            Este proyecto ha sido posible gracias a la colaboración entre estudiantes de software de la Universidad de 
            las Fuerzas Armadas ESPE y la carrera de biotecnología. Juntos, hemos trabajado para desarrollar una plataforma 
            que aborde las necesidades específicas de la investigación en biotecnología, con el objetivo de mejorar la 
            eficiencia y precisión en el análisis de imágenes de polen.
          </p>
        </div>
      </div>
      <div class="fila">
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/programa.png" style="max-width: 20%;"></div>
          <p><Strong>Como funciona el Proyecto</Strong><b></b></p><p>
            El funcionamiento de nuestra plataforma es sencillo y eficiente. Los usuarios seleccionan una imagen de polen 
            y la cargan en la plataforma. Utilizando un modelo de clasificación desarrollado en Roboflow, la plataforma 
            analiza la imagen y determina las familias polínicas presentes. Los resultados se presentan de manera clara y 
            organizada, facilitando su interpretación y uso en investigaciones posteriores.
          </p>
        </div>
        <div class="parrafo">
          <div style="justify-content: center;display: flex;">
          <img src="../img/observacion.png" style="max-width: 20%;"></div>
          <p><Strong>Usuarios Objetivo del Proyecto</Strong><b></b></p><p>
            Nuestra plataforma está dirigida principalmente a estudiantes e investigadores del área de biotecnología de
            la Universidad de las Fuerzas Armadas ESPE. Sin embargo, su diseño intuitivo y fácil de usar la hace accesible 
            para cualquier persona interesada en el análisis de imágenes de polen. Creemos que esta herramienta será 
            invaluable para la comunidad científica, contribuyendo al avance del conocimiento en el campo de la biotecnología.
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
    padding: 40px; /* Añade espacio alrededor de los párrafos */
    font-family: 'Avenir', Helvetica, Arial, sans-serif; /* Utiliza la misma fuente que el menú */
    color: #15323a; /* Color de texto blanco */
    box-sizing: border-box;
    box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.2); /* Incluir el borde en el tamaño del elemento */
  }
  
</style>
  