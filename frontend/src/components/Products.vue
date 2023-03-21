<template>
  <v-card
    class="mx-auto"
  >
    <v-img
      :src="product.image_url"
      height="200px"
    /> 
    <div class="d-flex mt-4">
      <v-card-title>
        {{ product.name }}
      </v-card-title>

      <template v-if="canAddProduct()">
        <v-btn variant="plain" icon="mdi-dots-vertical">
          <v-icon icon="mdi-dots-vertical" />
          <v-menu activator="parent">
            <v-list>
              <v-list-item @click="excluirProduto(product.id)">  Excluir Produto </v-list-item>
            </v-list>
          </v-menu>
        </v-btn>
      </template>
   </div>

  <div class="d-flex">
    <v-card-subtitle style="font-size:18px">
      Quantidade disponível: {{ product.quantity }}
    </v-card-subtitle>
    <v-spacer></v-spacer>
    <v-card-subtitle style="font-size:18px">
      <v-icon> mdi-currency-usd</v-icon>
        {{ product.price }}
    </v-card-subtitle>
  </div>

    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
        @click="show = !show"
      >
        Saiba mais
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          {{ product.description }}
        </v-card-text>
      </div>
    </v-expand-transition>
    <v-card-actions v-if="loggedUser">
      <v-btn
        @click="removeProduct()"
      >
        <v-icon>mdi-minus</v-icon>
      </v-btn>
        {{ quantity }}
      <v-btn
        @click="addProduct()"
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>

      <v-btn
        @click="addToChart(product.id, product.price)"
      >
      Adicionar ao carrinho
    </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapState } from 'pinia'
import { useProductStore } from "@/stores/productsStore"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  name: "Products",
  setup() {
    const productStore = useProductStore()
    return { productStore }
  },
  props: {
    product: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    show: false,
    quantity: 0,
    selectedProducts: [],
    price: null,
  }),
  computed: {
    ...mapState(useProductStore, ["productQuantity"]),
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  methods: {
    removeProduct () {
      if (this.quantity == 0) {
        return
      }
      this.quantity -= 1
    },
    addProduct () {
      if (this.product.quantity <= this.quantity) {
        return
      }
      this.quantity += 1
    },
    addToChart (productId, productPrice) {
      if (this.quantity <= 0) return
      this.price = this.quantity * productPrice
      this.selectedProducts.push({id:productId, quantity: this.quantity, price: this.price})
      this.quantity = 0
      this.productStore.setProductQuantity(this.selectedProducts.length, this.selectedProducts)
    },
    canAddProduct() {
      if(this.loggedUser){
        return this.loggedUser.permissions.ADMIN
      }
    },
    excluirProduto(productId) {
      this.$emit("excluirProduto", productId);
    },
  },
}
</script>
