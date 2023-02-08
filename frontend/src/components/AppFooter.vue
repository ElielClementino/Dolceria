<template>
  <v-footer :absolute="!fixed" app style="padding:0 !important">
    <div class="bg-purple d-flex w-100 align-center px-4">
      <strong class="strong">{{ year }} - Dolceria - Eliel</strong>

      <v-spacer/>
      <a 
      v-for="link, idx in links"
      :key="idx"
      :href="link"
      target="_blank"
      >
      <v-btn
        class="mx-4"
        :icon="icons[idx]"
        variant="plain"
        :size="60"
      >
      </v-btn>
      </a>
    </div>

  </v-footer>
</template>

<script>
  export default {
    props: {
      fixed: {
        type: Boolean,
        default: true,
      },
      user: {
        type: Object,
        default: null,
      },
  },
    data: () => ({
      year: new Date().getFullYear(),
      icons: [
        'mdi-github',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
      links: [
        'https://github.com/ElielClementino',
        'https://twitter.com/',
        'https://www.linkedin.com/in/eliel-clementino-3070b0224/',
        'https://instagram.com/'
      ]
    })
  }
</script>

<style scoped>
a {
  text-decoration:none;
  font-weight: bolder;
  font-size:2rem;
}
</style>