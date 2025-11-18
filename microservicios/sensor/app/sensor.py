from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
import random  # Para simular datos de sensores

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

@app.route('/sensor-data', methods=['GET'])
@jwt_required()
def get_sensor_data():
    # Simulando datos del sensor
    temperature = random.uniform(20, 30)
    humidity = random.uniform(40, 80)
    soil_moisture = random.uniform(10, 100)

    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture": soil_moisture
    })

if __name__ == '__main__':
    app.run(debug=True)
