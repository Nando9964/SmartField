from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import random  # Para simular los datos de monitoreo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/monitoring_db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Modelo para la información de monitoreo
class MonitoringData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_type = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    nutrient_level = db.Column(db.Float, nullable=False)

@app.route('/monitor', methods=['POST'])
@jwt_required()
def monitor_data():
    data = request.get_json()
    crop_type = data.get('crop_type')
    temperature = random.uniform(20, 30)  # Temperatura simulada
    humidity = random.uniform(40, 80)  # Humedad simulada
    nutrient_level = random.uniform(30, 100)  # Nivel de nutrientes simulado

    # Guardar los datos de monitoreo
    new_data = MonitoringData(
        crop_type=crop_type,
        temperature=temperature,
        humidity=humidity,
        nutrient_level=nutrient_level
    )
    db.session.add(new_data)
    db.session.commit()

    return jsonify({
        "crop_type": crop_type,
        "temperature": temperature,
        "humidity": humidity,
        "nutrient_level": nutrient_level
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
