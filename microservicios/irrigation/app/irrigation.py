from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required
import random  # Para simular datos de humedad

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/irrigation_db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Modelo de configuración de riego
class IrrigationConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_type = db.Column(db.String(50), nullable=False)
    threshold = db.Column(db.Float, nullable=False)  # Umbral de humedad para riego

@app.route('/activate-irrigation', methods=['POST'])
@jwt_required()
def activate_irrigation():
    data = request.get_json()
    crop_type = data.get('crop_type')
    # Simulación de lectura de humedad
    current_humidity = random.uniform(0, 100)  # Simulación de lectura en % de humedad
    config = IrrigationConfig.query.filter_by(crop_type=crop_type).first()

    if not config:
        return jsonify({"error": "Crop type not found"}), 404

    if current_humidity < config.threshold:
        # Activar riego
        # Lógica para activar sistema de riego real aquí
        return jsonify({"message": f"Riego activado para {crop_type}, humedad actual: {current_humidity}%"}), 200
    else:
        return jsonify({"message": f"Humedad suficiente, riego no necesario. Humedad actual: {current_humidity}%"}), 200

if __name__ == '__main__':
    app.run(debug=True)
