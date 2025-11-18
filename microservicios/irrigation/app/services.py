from datetime import datetime, timedelta

class IrrigationService:
    def __init__(self):
        self.irrigation_schedule = {}  # Aquí almacenamos los horarios de riego.

    def check_soil_moisture(self, irrigation_system):
        """Simula la verificación de la humedad del suelo. En realidad, esto vendría de los datos del sensor."""
        return irrigation_system.soil_moisture
    
    def should_irrigate(self, irrigation_system):
        """Determina si el sistema de riego debe activarse en función de la humedad."""
        if self.check_soil_moisture(irrigation_system) < 40:  # Umbral para riego
            return True
        return False
    
    def irrigate(self, irrigation_system):
        """Simula el proceso de riego. En la realidad, esto controlaría el sistema de riego físico."""
        if self.should_irrigate(irrigation_system):
            irrigation_system.last_watered = datetime.utcnow()
            irrigation_system.soil_moisture = 100  # Después del riego, la humedad del suelo es del 100%.
            print(f"Regando zona {irrigation_system.zone}.")
            return {"message": f"Zona {irrigation_system.zone} regada!"}
        return {"message": f"Zona {irrigation_system.zone} no necesita riego."}
