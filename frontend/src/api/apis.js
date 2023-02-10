import api from "./config.js"

export default {
  addNewProduct: (product) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/products/add/product", {product})
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  listProducts: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/products/list/products")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  filterProducts: (products) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/products/filter/products", products)
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  buyProducts: () => {
    return new Promise((resolve, reject) => {
      api
        .delete("/api/products/buy/products")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  }
}
