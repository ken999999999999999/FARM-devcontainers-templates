import axios from "axios"

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 1000,
  headers: { Authorization: `Bearer ${sessionStorage.getItem("token")}` },
})
