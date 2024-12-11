class Slot:
    SLOT_TYPES = ["Car", "Bike", "Truck"]

    def __init__(self, slot_no, slot_type):
        if slot_type not in Slot.SLOT_TYPES:
            raise ValueError(f"Unsupported slot type: {slot_type}")
        self.slot_no = slot_no
        self.slot_type = slot_type
        self.occupied = False
        self.vehicle = None
        self.ticket = None

    def is_occupied(self):
        return self.occupied

    def occupy(self, vehicle, ticket):
        if vehicle.vehicle_type != self.slot_type:
            raise ValueError(f"Cannot park vehicle of type {vehicle.vehicle_type} in a {self.slot_type} slot")
        self.occupied = True
        self.vehicle = vehicle
        self.ticket = ticket

    def unoccupy(self):
        self.occupied = False
        self.vehicle = None
        self.ticket = None

    @classmethod
    def add_slot_type(cls, slot_type):
        cls.SLOT_TYPES.append(slot_type)
