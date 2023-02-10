<template>
  <v-dialog
    transition="dialog-top-transition"
    v-model="showDialog"
  >
    <v-card class="pa-5">
      <v-card-title class="text-h5"> INFORMAÇÃO IMPORTANTE </v-card-title>
      <v-card-text class="text-h6">
        Para que você consiga comprar nossos produtos é necessário que esteja logado. Mas você pode olhar nossos produtos sem problemas <v-icon>mdi-emoticon-happy</v-icon>, basta clicar em "fechar". Caso não possua uma conta o botão de registro lhe levará para a tela de registro, e caso queira logar, o botão de login lhe levará para a tela de login.
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn
          color="primary"
          size="x-large" 
          @click="login"
        > 
            Login 
        </v-btn>
        <v-btn 
          color="primary" 
          size="x-large" 
          :to="{ name: 'accounts-register' }"
          >
            Registro
        </v-btn>
        <v-btn 
          color="primary" 
          size="x-large" 
          @click="close"
        >
          Fechar
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "InfoDialog",
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["close"],
  computed: {
    showDialog: {
      get() {
        return this.show
      },
    },
  },
  methods: {
    close() {
      this.$emit("close")
    },
    login() {
      this.$router.push({ name: 'accounts-login' })
    }
  },
}
</script>
