from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Definir las URLs de los microservicios
AUTH_SERVICE_URL = "http://auth-service:5000"
IRRIGATION_SERVICE_URL = "http://irrigation-service:5000"
MONITORING_SERVICE_URL = "http://monitoring-service:5000"
SENSOR_SERVICE_URL = "http://sensor-service:5000"

# Ruta para la autenticación
@app.route('/auth', methods=['POST'])
def auth():
    try:
        data = request.get_json()  # Obtén los datos enviados
        response = requests.post(f"{AUTH_SERVICE_URL}/auth", json=data)  # Redirige la petición al microservicio de autenticación
        return jsonify(response.json()), response.status_code  # Retorna la respuesta del microservicio
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error al comunicar con el microservicio de autenticación", "details": str(e)}), 500

# Ruta para el riego
@app.route('/irrigation', methods=['POST'])
def irrigation():
    try:
        data = request.get_json()
        response = requests.post(f"{IRRIGATION_SERVICE_URL}/irrigation", json=data)  # Redirige la solicitud al microservicio de riego
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error al comunicar con el microservicio de riego", "details": str(e)}), 500

# Ruta para el monitoreo
@app.route('/monitoring', methods=['GET'])
def monitoring():
    try:
        response = requests.get(f"{MONITORING_SERVICE_URL}/monitoring")  # Redirige la solicitud al microservicio de monitoreo
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error al comunicar con el microservicio de monitoreo", "details": str(e)}), 500

# Ruta para el sensor
@app.route('/sensor', methods=['GET'])
def sensor():
    try:
        response = requests.get(f"{SENSOR_SERVICE_URL}/sensor")  # Redirige la solicitud al microservicio del sensor
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error al comunicar con el microservicio del sensor", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)