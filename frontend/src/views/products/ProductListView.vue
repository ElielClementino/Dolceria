<template>
  <v-container class="fill-height">
    <info-dialog
    :show="showDialog"
    @close="closeDialog"
    />

      <v-text-field
        v-model="pesquisa"
        placeholder="Pesquise um produto"
        :loading="loading"
      > 
      </v-text-field>

    <v-row class="mt-2">
      <v-col v-for="product in productsFilter" :key="product.id">
        <products 
          :product="product" 
          @excluirProduto="excluirProduto"
        />
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
      pesquisa: "",
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
      productsFilter() {
        return this.products.filter((e) => {
          return e.name.toLowerCase().includes(this.pesquisa.toLowerCase());
        });
      },
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
    },
    excluirProduto(productId){
      console.log(' bateu')
      apis.excluirProduto(productId).then((data) =>{
        this.listProducts()
      })
    }
  },
}
</script>

<style scoped></style>
