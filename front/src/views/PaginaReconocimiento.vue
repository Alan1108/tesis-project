

<template>
  <div class="contenido">
    <div class="fila">
      <div class="recuadro-carga" @dragover.prevent @drop="handleDrop" @click="handleClick">
        
        <input type="file" id="fileInput" ref="fileInput" style="display: none;" @change="handleFileUpload()">
        <div class="upload-icon" v-if="!imageLoaded"> <!-- Contenedor para el icono de carga -->
          <img src="../img/upload.png" alt="Upload Icon">
        </div>
        <div class="image-preview" v-else> <!-- Contenedor para la previsualización de la imagen -->
          <img :src="uploadedImage" alt="Uploaded Image">
        </div>
        <div class="etiqueta">
          <p v-if="!imageLoaded">Arrastra una imagen aquí o haz clic para cargarla.</p>
          <p v-else>{{ uploadedFileName }}</p>
        </div>
      </div>
    </div>
    <div class="fila">
      <div class="parrafo">
        <button class="boton-parrafo" @click="submitFile()">Clasificar Imagen</button>
        <p><strong>Información del Proyecto</strong></p>
        <p>
          Nuestra plataforma interactiva se enfoca en el análisis de imágenes de polen para detectar familias.
          Es una herramienta innovadora diseñada en colaboración entre estudiantes de software de la Universidad
          de las Fuerzas Armadas ESPE y la carrera de biotecnología. Su objetivo es proporcionar una solución
          eficaz para el análisis de imágenes de polen, con aplicaciones importantes en la investigación científica
          y la biotecnología.
        </p>
      </div>
      <div class="parrafo">
        <button class="boton-parrafo">Mostrar Contenido</button>
        <p><strong>Involucrados del Proyecto</strong></p>
        <p>
          Este proyecto ha sido posible gracias a la colaboración entre estudiantes de software de la Universidad de
          las Fuerzas Armadas ESPE y la carrera de biotecnología. Juntos, hemos trabajado para desarrollar una plataforma
          que aborde las necesidades específicas de la investigación en biotecnología, con el objetivo de mejorar la
          eficiencia y precisión en el análisis de imágenes de polen.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
//import axios from 'axios';

export default {
  name: 'PaginaReconocimiento',
  data() {
    return {
      imageLoaded: false,
      uploadedFileName: '',
      uploadedImage: '' // Almacena la URL de la imagen cargada
    };
  },
  methods: {
    handleDrop(event) {
      event.preventDefault();
      this.isDragging = false;
      const file = event.dataTransfer.files[0];
      this.handleImage(file);
    },
    handleFileUpload() {
      const file = this.$refs.fileInput.files[0];
      this.handleImage(file);
    },
    handleClick() {
      this.$refs.fileInput.click();
    },
    handleImage(file) {
      this.imageLoaded = true;
      this.uploadedFileName = file.name;
      // Cargar la imagen como un objeto Blob
      const reader = new FileReader();
      reader.onload = () => {
        this.uploadedImage = reader.result; // Establecer la URL de la imagen cargada
      };
      reader.readAsDataURL(file);
    },
    async submitFile() {
      try {
        const formData = new FormData();
        formData.append('image', this.$refs.fileInput.files[0]);
        const response = await fetch('https://sample-f5jz4k4tfa-ue.a.run.app/tag/', {
          method: 'POST',
          body: formData,
          headers: {
            'Accept': 'application/json' // Establece el tipo de respuesta esperada como JSON
          }
        });
        if (!response.ok) {
          throw new Error('Error al clasificar la imagen');
        }

        // Procesa la respuesta como JSON
        const responseData = await response.json();
        console.log('Respuesta del servidor:', responseData);

        // Aquí puedes acceder a los datos de predicción y a la imagen en base64
        const predictionData = responseData.body.data;
        const base64Image = responseData.body.image;
        console.log('Datos de predicción:', predictionData);
        console.log('Imagen base64:', base64Image);
        // Puedes mostrar la imagen en la página si es necesario
        // Ejemplo de cómo mostrar la imagen en una etiqueta img
        // document.getElementById('imagenResultado').src = 'data:image/jpeg;base64,' + base64Image;
        const byteCharacters = atob(base64Image);
        const byteNumbers = new Array(byteCharacters.length);
        for (let i = 0; i < byteCharacters.length; i++) {
          byteNumbers[i] = byteCharacters.charCodeAt(i);
        }
        const byteArray = new Uint8Array(byteNumbers);
        const blob = new Blob([byteArray], { type: 'image/jpeg' });
        
        // Crear una URL de objeto para el blob
        this.imageUrl = URL.createObjectURL(blob);
        console.log('Imagen base64:', this.imageUrl);


        this.$router.push({
          path: '/resultado',
          query: {
            predictionData: JSON.stringify(predictionData),
            base64img: this.imageUrl
          }
        }); 
        
      } catch (error) {
        console.error('Error al clasificar la imagen:', error);
      }
    }
  }
};
</script>

<style>
/* Estilos adicionales si es necesario */
</style>

<style>
.contenido {
  text-align: justify;
  display: flex;
  flex-direction: column;
}

.fila {
  display: flex;
  flex-direction: row;
}

.recuadro-carga {
  flex: 1;
  position:relative;
  margin: 40px;
  margin-bottom: 0px;
  padding: 20px;
  background-color: #ffefe8;
  border-radius: 10px;
  text-align: center;
  cursor: pointer;
  border: 5px dashed #637e76;
}


.parrafo {
  flex: 1;
  margin: 25px;
  padding: 40px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: white;
  box-sizing: border-box;
}

.boton-parrafo {
  background-color: #637e76;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  margin-bottom: 10px;
  cursor: pointer;
  width: 60%;
  font-size: 32px;
  margin-left:20px;
}

.boton-parrafo:hover {
  background-color: #4e6359;
}
.upload-icon, .image-preview {
  position: relative;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 250px; /* Ajusta el tamaño del contenedor según sea necesario */
  height: 250px; /* Ajusta el tamaño del contenedor según sea necesario */
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0; /* Color de fondo del contenedor */
  border: 1px dashed #ccc; /* Borde punteado */
  border-radius: 5px; /* Borde redondeado */
}

.upload-icon img, .image-preview img {
  max-width: 100%;
  max-height: 100%;
}
.etiqueta{
  padding-top: 40px;
}
.upload-icon img {
  width: 200px; /* Ajusta el tamaño del icono según sea necesario */
  height: 200px; /* Ajusta el tamaño del icono según sea necesario */
}
</style>
