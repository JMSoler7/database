import axios from 'axios'

const token = document.head.querySelector('meta[name="csrf-token"]')

if (token) {
  axios.defaults.headers.common['X-CSRFToken'] = token.content
}

const Api = () =>
  axios.create({
    baseURL: '/api/',
    data: {},
  })

export default {
  get: (url, config) =>
    Api().get(`${url}/`, config)
      .then(response => Promise.resolve(response.data))
      .catch(error => Promise.reject(error)),

  put: (url, data, config) =>
    Api().put(`${url}/`, data, config)
      .then(response => Promise.resolve(response))
      .catch(error => Promise.reject(error)),

  post: (url, data, config) =>
    Api().post(`${url}/`, data, config)
      .then(response => Promise.resolve(response))
      .catch(error => Promise.reject(error)),
}
