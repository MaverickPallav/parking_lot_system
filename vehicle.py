class Vehicle:
    VEHICLE_TYPES = ["Car", "Bike", "Truck"]

    def __init__(self, vehicle_type, registration_number, color):
        if vehicle_type not in Vehicle.VEHICLE_TYPES:
            raise ValueError(f"Unsupported vehicle type: {vehicle_type}")
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color

    @classmethod
    def add_vehicle_type(cls, vehicle_type):
        cls.VEHICLE_TYPES.append(vehicle_type)
