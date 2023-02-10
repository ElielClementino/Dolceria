<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-img
      :src="product.image_url"
      height="200px"
    ></v-img>
    <v-card-title>
      {{ product.name }}
    </v-card-title>

    <v-card-subtitle style="font-size:18px">
      Valor: {{ product.price }}
    </v-card-subtitle>

    <v-card-subtitle style="font-size:18px">
      Quantidade disponível: {{ product.quantity }}
    </v-card-subtitle>
    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
        @click="show = !show"
      >
        Descrição
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
    }
  }
}
</script>
