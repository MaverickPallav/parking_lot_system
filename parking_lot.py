import threading
from floor import Floor
from ticket import Ticket
from slot import Slot
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, parking_lot_id):
        self.parking_lot_id = parking_lot_id
        self.floors = []
        self.lock = threading.Lock()

    def add_floor(self, floor):
        with self.lock:
            self.floors.append(floor)

    def find_available_slot(self, vehicle, strategy="default"):
        if strategy == "default":
            return self._default_strategy(vehicle)
        # Add more strategies as needed
        raise ValueError("Unknown slot finding strategy")

    def _default_strategy(self, vehicle):
        for floor in self.floors:
            slot = floor.find_available_slot(vehicle)
            if slot:
                return slot
        return None

    def park_vehicle(self, vehicle):
        with self.lock:
            slot = self.find_available_slot(vehicle)
            if slot:
                ticket = Ticket(self.parking_lot_id, slot.floor.floor_no, slot.slot_no)
                slot.occupy(vehicle, ticket)
                return ticket
            return None

    def unpark_vehicle(self, ticket_id):
        with self.lock:
            for floor in self.floors:
                slot = floor.get_slot_by_ticket(ticket_id)
                if slot:
                    slot.unoccupy()
                    return True
            return False

    def display_free_slots(self, vehicle_type):
        with self.lock:
            for floor in self.floors:
                floor.display_free_slots(vehicle_type)

    def display_occupied_slots(self, vehicle_type):
        with self.lock:
            for floor in self.floors:
                floor.display_occupied_slots(vehicle_type)
