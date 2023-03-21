<template>
<v-container>
  <v-card
    class="mx-auto"
  >
    <v-toolbar color="purple">
      <v-toolbar-title >Total da sua compra: R$ {{ valueToPay }}</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn
        @click="limparCarrinho"
        :disabled="valueToPay <= 0">
        <v-icon class="mr-2">mdi-cart-arrow-down</v-icon>
          Limpar Carrinho
      </v-btn>

      <v-btn
        :disabled="valueToPay <= 0"
        @click="buyProducts()"
      >
        <v-icon class="mr-2">mdi-cart-check</v-icon>
          Finalizar Compra
      </v-btn>
    </v-toolbar>

    <v-list
      :items="items"
      item-props
      lines="three"
    >
      <template v-slot:subtitle="{ subtitle }">
        <div v-html="subtitle"></div>
      </template>
    </v-list>
  </v-card>
</v-container>
</template>

<script>

import { mapState } from "pinia"
import apis from "@/api/apis.js"
import { useProductStore } from "@/stores/productsStore"

  export default {
    setup() {
      const productStore = useProductStore()
      return { productStore }
    },
    data: () => ({
      filteredProducts: [],
      valueToPay: 0,
      items: [
        { type: 'subheader', title: 'Produtos' },
      ],
    }),
    methods: {
      async filterProducts () {
        if (!this.products) return

        this.filteredProducts = await apis.filterProducts(this.products)
        for (let idx=0; idx < this.products.length; idx++){
          this.valueToPay += this.products[idx][0].price
        }
        this.filteredProducts.products.map((item, idx) => 
          this.items.push(
                {
                  prependAvatar:item["image_url"],
                  title: item["name"],
                  subtitle: `Quantidade: ${this.products[idx][0].quantity} <br>
                  Valor ${item["price"]} cada.`,
                },
                { type: 'divider', inset: true },
              )
        )
      },
      async buyProducts () {
        await apis.buyProducts(this.products)
        this.productStore.clearProductQuantity()
        this.$router.push({name: "thanks-for-buying"})
      },

      limparCarrinho (){
        this.products = []
        this.items = [
        { type: 'subheader', title: 'Produtos' },
        ]
        this.valueToPay = 0
        this.productStore.clearProductQuantity()
      }
    },
    computed: {
      ...mapState(useProductStore, ["products"])
    },
    mounted () {
      this.filterProducts()
    }
  }
</script>