<template>
<v-container>
  <v-card
    class="mx-auto"
  >
    <v-toolbar color="purple">

      <v-toolbar-title>Produtos adicionados no carrinho</v-toolbar-title>

      <v-spacer></v-spacer>
      <v-toolbar-title >Total da sua compra: R$ {{ valueToPay }}</v-toolbar-title>
    <v-btn>
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
    data: () => ({
      filteredProducts: [],
      valueToPay: 0,
      items: [
        { type: 'subheader', title: 'Produtos' },
        {
          prependAvatar:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHgzVLj9HXP1PD5NVNx5D4mZMpJKrGRUXcrQ&usqp=CAU',
          title: 'Morango com chantilly',
          subtitle: 'Você adicionou 30 unidades do bolo de morango que custam 65.55 cada.',
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://img.cybercook.com.br/receitas/975/bolo-de-cenoura-31.jpeg',
          title: 'Cenoura com calda de chocolate',
          subtitle: 'Você adicionou 20 unidades do bolo de cenoura que custam 55.55 cada.',
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnHWSpUbf87DTkCX2BBELNAyypVYaj-8BSh7o67I56qg&s',
          title: 'Red Velvet',
          subtitle: 'Você adicionou 10 unidades do bolo red velvet que custam 75.55 cada.',
        }
      ],
    }),
    methods: {
      async filterProducts () {

        if (!this.products){
          return
        }
        this.filteredProducts = await apis.filterProducts(this.products)
        for (let idx=0; idx < this.products.length; idx++){
          this.valueToPay += this.products[idx][0].price
        }
        this.filteredProducts.products.map(item => 
          this.items.push(
                {
                  prependAvatar:item["image_url"],
                  title: item["name"],
                  subtitle: `Você adicionou ${this.products.quantity} unidades do bolo de morango que custam ${item["price"]} cada.`,
                },
                { type: 'divider', inset: true },
              )
        )
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