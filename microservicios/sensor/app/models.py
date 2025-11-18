class SensorData:
    def __init__(self, id, temperature, humidity, soil_moisture):
        self.id = id
        self.temperature = temperature
        self.humidity = humidity
        self.soil_moisture = soil_moisture
    
    def __repr__(self):
        return f"<SensorData {self.id}, Temp: {self.temperature}, Humidity: {self.humidity}>"
