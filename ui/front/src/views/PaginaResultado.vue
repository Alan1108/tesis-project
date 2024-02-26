
import { withDirectives } from 'vue';

import { withDirectives } from 'vue';
<template>
    <div>
        <h1 style="text-align: center;">Resultado del Análisis</h1>

        <div style="display: flex;padding-left:5%;padding-right:5%;border-radius: 15px;" >
            <table >
                <tr >
                    <td>
                        <img :src="blobUrl" alt="Imagen de resultado" style="max-width: 500px; max-height: 500px;border: 4px solid #15323a;border-radius: 5px;box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.2);">
                    </td>
                    <td>
                        <div class="box">
                            <template v-if="predictionData && predictionData.length > 0">
                                <h2>Datos de Predicción:</h2>
                                <img src="../img/microscopio.png" style="max-width: 20%;">
                                <p>El análisis de la imagen a identificado las siguientes familias:</p>
                                <table class="general">
                                    <thead>
                                        <tr>
                                            <th >Nombre</th>
                                            <th>Porcentaje</th>
                                            <th >Color</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr class="general" v-for="(data, index) in predictionData" :key="index">
                                            <td class="general">{{ data.class_name }}</td>
                                            <td class="general">{{ data.percentage }} %</td>
                                            <td  class="general">{{ data.color }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </template>
                            <template v-else>
                                <p>No hay datos de predicción disponibles.</p>
                            </template>
                            <div style="justify-content: center;display: flex;">
                            <button @click="loadAnotherImage"><img src="../img/imagen.png">Cargar otra imagen</button>
                          </div>
                        </div>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
export default {
  name: 'PaginaResultado',
  data() {
    return {
      predictionData: [],
      blobUrl: ''
    };
  },
  mounted() {
    const predictionDataString = this.$route.query.predictionData;
    if (predictionDataString) {
      try {
        this.predictionData = JSON.parse(predictionDataString);
        this.blobUrl = this.$route.query.base64img;
        console.log('Datos de predicción:', this.predictionData);
      } catch (error) {
        console.error('Error al analizar los datos de predicción:', error);
      }
    } else {
      console.error('No se encontraron datos de predicción.');
    }
  },
  methods: {
    loadAnotherImage() {
      // Limpiar la cache y redirigir a la página de reconocimiento
      this.predictionData = [];
      this.blobUrl = '';
      this.$router.push('/reconocimiento');
    }
  }
};
</script>

<style scoped>
/* Estilos específicos para esta página */
table {
  border-collapse: collapse;
  width: 100%;
  
}

.general{
    border: 1px solid #2380a8;
    border-radius: 15px;
    background-color: white;
    
}

th, td {
  padding: 8px;
  
  text-align: center;
  
  
}


th {
  background-color: #15323a;
  border: 1px solid #2380a8;
  
  color: white;
}
button{
    font-size: 32px;
    margin-top:5%;
    display: flex; /* Utiliza flexbox */
    align-items: center;
}

button img{
  max-width: 10%;
  padding-right: 5%;
  padding-left: 5%;
}
.box{
  border: 2px solid #2380a8;
  border-radius: 15px;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.2);
  padding: 5%;
}
</style>
