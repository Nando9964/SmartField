import random
from datetime import datetime

class SensorService:
    def __init__(self):
        self.sensor_data_store = {}  # Simulamos una base de datos en memoria
    
    def generate_sensor_data(self, id):
        """Simula la recolección de datos de un sensor."""
        return {
            'id': id,
            'temperature': random.uniform(20.0, 35.0),  # Temperatura en grados Celsius
            'humidity': random.uniform(40.0, 90.0),  # Humedad en porcentaje
            'soil_moisture': random.uniform(10.0, 80.0),  # Humedad del suelo en porcentaje
            'timestamp': datetime.utcnow().isoformat()  # Marca temporal
        }

    def get_sensor_data(self, id):
        """Simula la obtención de datos de un sensor para el ID proporcionado."""
        if id not in self.sensor_data_store:
            self.sensor_data_store[id] = self.generate_sensor_data(id)
        
        return self.sensor_data_store[id]
