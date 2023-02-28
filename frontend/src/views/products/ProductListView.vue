<template>
  <v-container class="fill-height">
    <info-dialog
    :show="showDialog"
    @close="closeDialog"
    />
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Todos os nossos produtos </v-card-title>
        </v-card>
      </v-col>
    <v-divider/>
      <v-col class="mt-6" v-for="product in products" :key="product.id" cols="4">
        <products :product="product" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import apis from "@/api/apis.js"
import Products from "@/components/Products.vue"
import InfoDialog from "@/components/InfoDialog.vue"
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import AccountsApi from "@/api/accounts.api.js"

export default {
  name: "ProductsList",
  components: {
    Products,
    InfoDialog
  },
  setup() {

    const appStore = useAppStore()
    const accountsStore = useAccountsStore()

    return { appStore, accountsStore }
  },
  data() {
    return {
      loading: false,
      items: [],
      showDialog: false,
      products: [],
      authenticated: false,
    }
  },
  mounted() {
    this.listProducts()
    AccountsApi.whoami().then((response) =>{
      this.authenticated = response.authenticated
      if (!this.authenticated){
        this.showPopup()
      }
      else {
        this.accountsStore.setLoggedUser(response.user)
        
      }
    })
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  methods: {
    showPopup() {
      this.showDialog = false
      if (!this.authenticated) {
        this.showDialog = true
      }
      return this.showDialog
    },
    closeDialog() {
      this.showDialog = false
      return this.showDialog
    },
    listProducts() {
      this.loading = true
      apis.listProducts().then((data) => {
        this.products = data.products
        this.loading = false
      })
    }
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
