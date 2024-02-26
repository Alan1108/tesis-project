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
        <button class="boton-parrafo" @click="submitFile()"><img src="../img/clasificar.png" alt="+">Clasificar Imagen</button>
        <p>
          Sube la imagen en los formatos admitidos para que el programa analice e identifique las familias encontradas
          , la imagen subida va a ser almacenada para mejorar el entrenamiento del modelo neuronal para futuras
          actualizaciones.
        </p>
      </div>
      <div class="parrafo">
        
        <router-link to="/familias"><button class="boton-parrafo"> <img src="../img/quimica.png" alt="+">Lista de Familias</button></router-link>
        <p>
          Conoce las 26 familias de polínicos que el programa puede identificar.
        </p>
      </div>
    </div>
    <ModalCargando :cargando="cargando" />
  </div>
</template>

<script>
//import axios from 'axios';
import ModalCargando from './ModalCargando.vue';
export default {
  name: 'PaginaReconocimiento',
  components:{
    ModalCargando
  },
  data() {
    return {
      imageLoaded: false,
      cargando: false,
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
      this.cargando = true;
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
      } finally {
        this.cargando = false; // Ocultar el modal de carga
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
  background-color: #cff1ff;
  border-radius: 10px;
  text-align: center;
  cursor: pointer;
  border: 5px dashed #15323a;
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
  background-color: #15323a;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  margin-bottom: 10px;
  cursor: pointer;
  width: 100%;
  font-size: 32px;
  text-decoration: none;
}
.boton-parrafo img{
  max-width: 5%;
  padding-right: 5%;
}

.boton-parrafo:hover {
  background-color: #2380a8;
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
  background-color: #ffff; /* Color de fondo del contenedor */
  border: 1px dashed #2380a8; /* Borde punteado */
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
.router-link-exact-active {
  text-decoration: none; /* Quitar subrayado de enlaces activos */
}
</style>
