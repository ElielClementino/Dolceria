<template>
<v-container>
  <v-card
    class="mx-auto"
  >
    <v-toolbar color="purple">

      <v-toolbar-title>Produtos adicionados no carrinho</v-toolbar-title>

      <v-spacer></v-spacer>
      <v-toolbar-title >Total da sua compra: R$ {{ valueToPay }}</v-toolbar-title>
    <v-btn
      size="large"
      rounded="pill"
      dense
      append-icon="mdi-chevron-right"
      :disabled="valueToPay <= 0"
      @click="buyProducts()"
    >
        FINALIZAR COMPRA
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
                  subtitle: `Você adicionou ${this.products[idx][0].quantity} unidades do bolo de morango que custam ${item["price"]} cada.`,
                },
                { type: 'divider', inset: true },
              )
        )
      },
      async buyProducts () {
        await apis.buyProducts(this.products)
        this.productStore.clearProductQuantity()
        this.$router.push({name: "thanks-for-buying"})
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