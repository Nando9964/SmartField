class IrrigationSystem:
    def __init__(self, id, zone, last_watered, soil_moisture):
        self.id = id
        self.zone = zone
        self.last_watered = last_watered
        self.soil_moisture = soil_moisture
    
    def __repr__(self):
        return f"<IrrigationSystem {self.id}, Zone: {self.zone}>"
