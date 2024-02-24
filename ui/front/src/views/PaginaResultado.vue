
import { withDirectives } from 'vue';

import { withDirectives } from 'vue';
<template>
    <div>
        <h1 style="text-align: center;">Resultado del Análisis</h1>

        <div style="display: flex;padding-left:5%;padding-right:5%" >
            <table >
                <tr >
                    <td>
                        <img :src="blobUrl" alt="Imagen de resultado" style="max-width: 500px; max-height: 500px;border: 4px dashed #ccc; /* Borde punteado */border-radius: 5px">
                    </td>
                    <td>
                        <div>
                            <template v-if="predictionData && predictionData.length > 0">
                                <h2>Datos de Predicción:</h2>
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
                            <button @click="loadAnotherImage">Cargar otra imagen</button>
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

table, th, td {
  border: none;
}
.general{
    border: 1px solid black;
    background-color: white;
}

th, td {
  padding: 8px;
  text-align: center;
  
}


th {
  background-color: #4e6359;
  color: white;
}
button{
    font-size: 32px;
    margin-top:5%;
}
</style>
