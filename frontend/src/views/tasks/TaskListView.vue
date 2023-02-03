<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Tasks </v-card-title>
        </v-card>
      </v-col>

      <v-col cols="12">
        <task-form :form-label="'Nova Tarefa'" @new-task="addNewTask" />
      </v-col>

      <v-col v-for="item in items" :key="item.id" cols="12">
        <task :task="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"
import Task from "@/components/Task.vue"
import TaskForm from "@/components/TaskForm.vue"

export default {
  name: "TasksList",
  components: { Task, TaskForm },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      items: [],
      product: {
          "name": "Red Velvet",
          "image_url": "https://url.py",
          "description": "O Bolo Red Velvet é um bolo de textura muito leve e macia, levemente amanteigado e com um discreto sabor a chocolate. A sua massa é de cor vermelha, o que contrasta com o branco do creme queijo no recheio e cobertura-.",
          "quantity": 30,
          "price": 55.50,
      }
    }
  },
  mounted() {
    this.getTasks()
    this.addNewProduct(this.product)
  },
  methods: {
    getTasks() {
      this.loading = true
      TasksApi.getTasks().then((data) => {
        this.items = data.todos
        this.loading = false
      })
    },
    addNewTask(task) {
      this.loading = true
      TasksApi.addNewTask(task.title).then((task) => {
        this.appStore.showSnackbar(`Nova tarefa adicionada #${task.id}`)
        this.getTasks()
        this.loading = false
        console.log("oi")
      })
    },
    addNewProduct(product) {
      TasksApi.addNewProduct(product)
    }
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
