<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="container" style="height: 100%; padding: 40px;">
      <p class="title">Universidad Tecnológica Metropolitana</p>
      <p class="subtitle">INFB8061 - Grafos y Lenguajes Formales</p>

      <div style="display: flex; justify-content: space-between;">
        <persona
          v-for="integrante in integrantes"
          :key="integrante.nombre"
          :redes="integrante.redes"
          :nombre="integrante.nombre"
          :imagen="integrante.imagen"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Persona from "../components/Persona.vue";
export default {
  components: {
    Persona,
  },
  data: () => ({
    integrantes: [
      {
        nombre: "Javier Garrido",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80979585-88368600-8df5-11ea-8d6b-0a2541ba09bb.png",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/Scalim",
            icono: "github-circle",
            color: "#000",
          },
        ],
      },
      {
        nombre: "Mariam Maldonado",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80976941-114bbe00-8df2-11ea-9d68-6c42c6846944.jpeg",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/mariam6697",
            icono: "github-circle",
            color: "#000",
          },
          {
            nombre: "Twitter",
            url: "https://twitter.com/mariam_vmm",
            icono: "twitter",
            color: "#1da1f2",
          },
        ],
      },
      {
        nombre: "Carlos Montuyao",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80985782-ad2ef700-8dfd-11ea-93ab-23f6434a7422.png",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/Dymmon",
            icono: "github-circle",
            color: "#000",
          },
        ],
      },
      {
        nombre: "Jorge Verdugo",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80977076-3e986c00-8df2-11ea-80c9-d62518f47e34.jpeg",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/mapacheverdugo",
            icono: "github-circle",
            color: "#000",
          },
          {
            nombre: "Instagram",
            url: "http://instagram.com/mapacheverdugo",
            icono: "instagram",
            color: "#c13584",
          },
          {
            nombre: "Twitter",
            url: "https://twitter.com/mapacheverdugo",
            icono: "twitter",
            color: "#1da1f2",
          },
        ],
      },
      {
        nombre: "Javiera Vergara",
        imagen:
          "https://user-images.githubusercontent.com/16374322/80976999-23c5f780-8df2-11ea-8343-061da9c2b69c.jpeg",
        redes: [
          {
            nombre: "GitHub",
            url: "https://github.com/PollitoMayo",
            icono: "github-circle",
            color: "#000",
          },
          {
            nombre: "Twitter",
            url: "https://twitter.com/pollitomayonesa",
            icono: "twitter",
            color: "#1da1f2",
          },
          {
            nombre: "DeviantArt",
            url: "https://www.deviantart.com/pollitomayo",
            icono: "deviantart",
            color: "#4dc47d",
          },
        ],
      },
    ],
  }),
};
</script>