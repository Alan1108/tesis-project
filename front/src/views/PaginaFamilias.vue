<template>
    <div class="familias">
      <h1>Familias de Polínicos</h1>
      <p style="font-size: 18px;padding-bottom: 10px;">A continuación están las 26 familias de polinicos que identifica el sistema mediante la carga de imágenes. Conoce sus nombres, su distribución geográfica y el recurso utilizado para su identificación.</p>
      
      <!-- Aquí se divide la tabla en partes -->
        <table class="tabla-familias">
            <thead>
                <tr>
                <th style="width: 9%;text-align: center;">No.</th>
                <th style="width: 12%;text-align: center;">Familia</th>
                <th style="width: 35%;text-align: center;">Distribución Geográfica</th>
                <th style="width: 32%;text-align: center;">Grano de Polen</th>
                <th style="width: 12%;text-align: center;">Recurso Utilizado</th>
                </tr>
            </thead>
            <tbody>
                <!-- Filas de la tabla -->
                <tr v-for="familia in familiasMostradas" :key="familia.id" :class="{ 'fila-par': familia.id % 2 === 0, 'fila-impar': familia.id % 2 !== 0 }">
                <td style="width: 9%; text-align: center;">{{ familia.id }}</td>
                <td style="width: 12%; text-align: center;">{{ familia.nombre }}</td>
                <td style="width: 35%;">{{ familia.distribucion }}</td>
                <td style="width: 32%;"><img :src="familia.imagen" alt="Grano de Polen" class="imagen-polen"></td>
                <td style="width: 12%; text-align: center;">{{ familia.recurso }}</td>
                </tr>
            </tbody>
        </table>
        <div class="paginacion">
            <button class="botonpaginado" @click="paginaAnterior" :disabled="pagina === 1">
                <img src="../img/flecha.png" style="transform: rotate(180deg)"> Anterior</button>
            <button class="botonpaginado" @click="paginaSiguiente" :disabled="pagina === totalPaginas">Siguiente
                <img src="../img/flecha.png">
            </button>
        </div>
    </div>
  </template>
  
  <script>
    import AizoaceaeImage from '../img/familias/Aizoaceae.jpg';
    import AlismataceaeImage from '../img/familias/Alismataceae.jpg';
    import Arecaceae from '../img/familias/Arecaceae.jpg';
    import Anacardaceae from '../img/familias/Anacardaceae.jpg';
    import Asteraceae from '../img/familias/Asteraceae.jpg';
    import Berberidaceae from '../img/familias/Berberidaceae.jpg';
    import Burseraceae from '../img/familias/Burseraceae.jpg';
    import Cyperaceae from '../img/familias/Cyperaceae.jpg';
    import Cytinaceae from '../img/familias/Cytinaceae.jpg';
    import Euphorbiaceae  from '../img/familias/Euphorbiaceae.jpg';
    import Fabaceae from '../img/familias/Fabaceae.jpg';
    import Lardizabalaceae from '../img/familias/Lardizabalaceae.jpg';
    import Loranthaceae from '../img/familias/Loranthaceae.jpg';
    import Lythraceae from '../img/familias/Lythraceae.jpg';
    import Melastomataceae from '../img/familias/Melastomataceae.jpg';
    import Molluginaceae from '../img/familias/Molluginaceae.jpg';
    import Oleaceae from '../img/familias/Oleaceae.jpg';
    import Papaveraceae from '../img/familias/Papaveraceae.jpg';
    import Piperaceae from '../img/familias/Piperaceae.jpg';
    import Plantaginaceae  from '../img/familias/Plantaginaceae.jpg';
    import Plumbaginaceae from '../img/familias/Plumbaginaceae.jpg';
    import Poaceae from '../img/familias/Poaceae.jpg';
    import Polygalaceae from '../img/familias/Polygalaceae.jpg';
    import Rosaceae from '../img/familias/Rosaceae.jpg';
    import Salicaceae from '../img/familias/Salicaceae.jpg';
    import Vitaceae from '../img/familias/Vitaceae.jpg';

  export default {
    
    name: 'PaginaFamilias',
    data() {
      return {
        pagina: 1,
        tamanoPagina: 7,
        familias: [
            {
                id: 1,
                nombre: 'Aizoaceae',
                distribucion: 'Partes secas de zonas tropicales y subtropicales. Entorno de África, Mediterráneo, Asia Menor y la costa occidental de América (Norte, Sur y Caribe).',
                imagen: AizoaceaeImage,
                recurso: 'Polen y néctar'
            },
            {
                id: 2,
                nombre: 'Alismataceae',
                distribucion: 'Zonas tropicales de los 5 continentes (pantropical), zonas de clima templado y neotropicales',
                imagen: AlismataceaeImage,
                recurso: 'Polen y néctar'
            },
            {
                id: 3,
                nombre: 'Arecaceae',
                distribucion: 'Trópicos y subtrópicos de ambos hemisferios, extendiéndose a regiones más cálidas',
                imagen: Arecaceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 4,
                nombre: 'Anacardaceae',
                distribucion: 'En zonas tropicales y subtropicales.',
                imagen: Anacardaceae,
                recurso: 'Polen, néctar y resinas'
            },
            {
                id: 5,
                nombre: 'Asteraceae',
                distribucion: 'Todos los ambientes y continentes, excepto la Antártida.',
                imagen: Asteraceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 6,
                nombre: 'Berberidaceae',
                distribucion: 'Bosques mesófilos (humedad y temperatura promedio) de Asia y América.',
                imagen: Berberidaceae,
                recurso: 'Polen'
            },
            {
                id: 7,
                nombre: 'Burseraceae',
                distribucion: 'Zonas paleotropicales de América del Sur, Asia continental y África.',
                imagen: Burseraceae,
                recurso: 'Polen'
            },
            {
                id: 8,
                nombre: 'Cyperaceae',
                distribucion: 'Zonas de marismas y vegetación ártica, zonas tropicales de Asia, América y África.',
                imagen: Cyperaceae,
                recurso: 'Polen'
            },
            {
                id: 9,
                nombre: 'Cytinaceae',
                distribucion: 'Áreas mediterráneas, África y Madagascar. Neotrópico desde México hasta Colombia.',
                imagen: Cytinaceae,
                recurso: 'Polen'
            },
            {
                id: 10,
                nombre: 'Euphorbiaceae',
                distribucion: 'Zonas tropicales y selvas, desiertos secos y calurosos.',
                imagen: Euphorbiaceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 11,
                nombre: 'Fabaceae',
                distribucion: 'Cordillera de los Andes, América del Sur y sus zonas tropicales.',
                imagen: Fabaceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 12,
                nombre: 'Lardizabalaceae',
                distribucion: 'Bosques tropicales, bosques mixtos templado-cálidos de Asia y América del Sur (zona oriental).',
                imagen: Lardizabalaceae,
                recurso: 'Polen'
            },
            {
                id: 13,
                nombre: 'Loranthaceae',
                distribucion: 'Zonas intertropicales de América del Sur, tierras bajas de áreas vecinas de Chile y Argentina.',
                imagen: Loranthaceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 14,
                nombre: 'Lythraceae',
                distribucion: 'Bosques abiertos, bosques tropicales y subtropicales, tierras rocosas, pastizales, riberas de arroyos, manglares, costas asiáticas y americanas.',
                imagen: Lythraceae,
                recurso: 'Polen'
            },
            {
                id: 15,
                nombre: 'Melastomataceae',
                distribucion: 'Zonas tropicales de Asia, América y África (pantropical).',
                imagen: Melastomataceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 16,
                nombre: 'Molluginaceae',
                distribucion: 'Regiones tropicales y subtropicales de ambos hemisferios. Hábitat seco, abierto y hostil.',
                imagen: Molluginaceae,
                recurso: 'Polen'
            },
            {
                id: 17,
                nombre: 'Oleaceae',
                distribucion: 'Regiones templadas, frías y cálidas de Asia, África y América del Sur.',
                imagen: Oleaceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 18,
                nombre: 'Papaveraceae',
                distribucion: 'Asia central y occidental, altas montañas de Europa, América a lo largo de la costa del Pacífico, en climas áridos a cálidos.',
                imagen: Papaveraceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 19,
                nombre: 'Piperaceae',
                distribucion: 'Regiones tropicales de los hemisferios norte y sur, con la mayor concentración en América Latina y Malasia, EE. UU.',
                imagen: Piperaceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 20,
                nombre: 'Plantaginaceae ',
                distribucion: 'Zonas templadas a tropicales, considerada una familia cosmopolita.',
                imagen: Plantaginaceae ,
                recurso: 'Polen y néctar'
            },
            {
                id: 21,
                nombre: 'Plumbaginaceae',
                distribucion: 'Hábitats costeros fríos a áridos y salinos de Asia Central y regiones subtropicales y tropicales de las Américas.',
                imagen: Plumbaginaceae,
                recurso: 'Polen'
            },
            {
                id: 22,
                nombre: 'Poaceae',
                distribucion: 'Desde ambientes desérticos a húmedos, hábitats marinos y altas montañas del Asia tropical, pastizales, pampas en América del Sur y estepas del viejo continente.',
                imagen: Poaceae,
                recurso: 'Polen'
            },
            {
                id: 23,
                nombre: 'Polygalaceae',
                distribucion: 'Zonas tropicales de América, Asia, Australia.',
                imagen: Polygalaceae,
                recurso: 'Polen'
            },
            {
                id: 24,
                nombre: 'Rosaceae',
                distribucion: 'Amplia distribución desde zonas frías a cálidas en los cinco continentes.',
                imagen: Rosaceae,
                recurso: 'Polen y néctar'
            },
            {
                id: 25,
                nombre: 'Salicaceae',
                distribucion: 'Europa, Asia, África, toda América.',
                imagen: Salicaceae,
                recurso: 'Polen'
            },
            {
                id: 26,
                nombre: 'Vitaceae',
                distribucion: 'Regiones tropicales-húmedas de Asia y América del Sur.',
                imagen: Vitaceae,
                recurso: 'Polen y néctar'
            },
        ]
      };
    },
    computed: {
    // Calcula el índice de inicio de la página actual
        indiceInicio() {
        return (this.pagina - 1) * this.tamanoPagina;
        },
        // Calcula el índice de fin de la página actual
        indiceFin() {
        return this.indiceInicio + this.tamanoPagina;
        },
        // Obtiene las familias que se muestran en la página actual
        familiasMostradas() {
        return this.familias.slice(this.indiceInicio, this.indiceFin);
        },
        // Calcula el número total de páginas
        totalPaginas() {
        return Math.ceil(this.familias.length / this.tamanoPagina);
        }
    },
    methods: {
    // Función para ir a la página anterior
    paginaAnterior() {
      if (this.pagina > 1) {
        this.pagina--;
      }
    },
    // Función para ir a la página siguiente
    paginaSiguiente() {
      if (this.pagina < this.totalPaginas) {
        this.pagina++;
      }
    },
    
  }
  };
  </script>
  
  <style scoped>
  .familias {
    margin-top: 20px;
    padding-left: 10%;
    padding-right: 10%;
    padding-bottom: 10%;
  }
  
  .tabla-familias {
    width: 100%;
    border-collapse: collapse;
    
  }
  
  .tabla-familias th,
  .tabla-familias td {
    border: 1px solid #2380a8;
    padding: 8px;
    text-align: left;
  }
  
  .tabla-familias th {
    background-color: #15323a;
    color: white;
    font-weight: bold;
  }
  
  .fila-par {
    background-color: #cff1ff;
  }
  
  .fila-impar {
    background-color: #ffffff;
  }
  
  .imagen-polen {
    width: 100%;
    height: auto;
    max-width: 480px;
    max-height: 270px;
  }
  .paginacion {
  margin-top: 20px;
}

.paginacion button {
  margin-right: 10px;
}

.botonpaginado{
    background-color: #15323a;
    font-size: 18px;
}
.botonpaginado:hover {
  background-color: #2380a8;
}
.botonpaginado img{
    max-width: 10%;
}
  </style>
  