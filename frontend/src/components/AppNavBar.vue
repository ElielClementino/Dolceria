<template>
  <v-app-bar>
    <v-app-bar-title>{{ title }}</v-app-bar-title>
    <template #append>
      <v-btn v-if="loggedUser" icon="mdi-cart" :to="{ name: 'base-home' }">
      </v-btn>
      <v-btn
        :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
        @click.stop="themeClick"></v-btn>
      <v-btn icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list>
            <v-list-item v-if="loggedUser" :to="{ name: 'new-product' }"> Adicionar Produto </v-list-item>
            <v-list-item v-if="loggedUser" :to="{ name: 'accounts-logout' }"> Deslogar </v-list-item>
            <v-list-item v-if="canAddProduct()" :to="{ name: 'accounts-login' }"> Login </v-list-item>
            <v-list-item :to="{ name: 'base-home' }"> Página inicial </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script>

import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import { useProductStore } from "@/stores/productsStore"

export default {
  props: {
    title: {
      type: String,
      required: false,
      default: "Dolceria",
    },
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {}
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
    canAddProduct() {
      if(this.loggedUser){
        return this.loggedUser.permissions.ADMIN
      }
    }
  },
    computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
    ...mapState(useProductStore, ["productStore"])
  },
}
</script>
