import Axios from "axios";

const api = Axios.create({
  baseURL: "http://localhost:8000/api",
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
    "Accept": "application/json",
  },
});

api.interceptors.request.use(
  (config) => {
    if (localStorage.getItem("access")) {
      config.headers.Authorization = `JWT ${localStorage.getItem("access")}`;
    }

    return config;
  },
  (error) => Promise.reject(error)
);

export default api;
