<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <blockquote class="blockquote text-h4">
        Bem Vindo a Dolceria do Eliel.
        <footer >
          <small>
            <em>Aqui você encontrará diversos tipos de doces </em>
          </small>
        </footer>
      </blockquote>
      <v-img contain height="310" src="@/assets/Dc.png" />

      <div 
      class="text-h6 mb-4 pt-4"
      >
        Somos uma loja que procura entregar o melhor para o nosso cliente, 
        portanto usamos os produtos da melhor qualidade possível, 
        e fazemos o máximo para podermos entregar produtos de ótima qualidade para os nossos clientes.
      </div>
      <h1 class="text-h2 font-weight-bold">Dolceria</h1>

      <div class="py-6" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            color="primary"
            :to="{ name: 'products-list' }"
            min-width="228"
            size="x-large"
            variant="flat"
            class="my-4">
            <v-icon icon="mdi-cupcake" size="40" start />
            Veja nossos produtos
          </v-btn>
          <v-btn
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            v-if="!loggedUser"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-register' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Cadastre-se
          </v-btn>
          <v-btn
            v-if="!loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Login
          </v-btn>
          <v-btn
            v-else
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-logout' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Logout
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  }
}
</script>
