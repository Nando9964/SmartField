import axios from 'axios'

// Instancia de Axios para la autenticación
const authApi = axios.create({
  baseURL: 'http://auth:5000',  // Aquí 'auth' es el nombre del servicio en Docker Compose
  timeout: 10000,
})

// Instancia de Axios para el servicio de riego
const irrigationApi = axios.create({
  baseURL: 'http://irrigation:5000',
  timeout: 10000,
})

// Instancia de Axios para el servicio de monitoreo
const monitoringApi = axios.create({
  baseURL: 'http://monitoring:5000',
  timeout: 10000,
})

// Instancia de Axios para el servicio de sensores
const sensorApi = axios.create({
  baseURL: 'http://sensor:5000',
  timeout: 10000,
})

// Función de autenticación
export const authenticateUser = (username, password) => {
  return authApi.post('/auth/login', { username, password })
}

// Función de riego
export const getIrrigationData = () => {
  return irrigationApi.get('/irrigation')
}

// Función de monitoreo
export const getMonitoringData = () => {
  return monitoringApi.get('/monitoring')
}

// Función de sensores
export const getSensorData = () => {
  return sensorApi.get('/sensor')
}
