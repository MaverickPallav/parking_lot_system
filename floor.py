from slot import Slot

class Floor:
    def __init__(self, floor_no, slots):
        self.floor_no = floor_no
        self.slots = slots

    def find_available_slot(self, vehicle):
        for slot in self.slots:
            if not slot.is_occupied() and slot.slot_type == vehicle.vehicle_type:
                return slot
        return None

    def get_slot_by_ticket(self, ticket_id):
        for slot in self.slots:
            if slot.ticket and slot.ticket.ticket_id == ticket_id:
                return slot
        return None

    def display_free_slots(self, vehicle_type):
        print(f"Free slots for {vehicle_type} on floor {self.floor_no}:")
        for slot in self.slots:
            if not slot.is_occupied() and slot.slot_type == vehicle_type:
                print(f"Slot No: {slot.slot_no}")

    def display_occupied_slots(self, vehicle_type):
        print(f"Occupied slots for {vehicle_type} on floor {self.floor_no}:")
        for slot in self.slots:
            if slot.is_occupied() and slot.slot_type == vehicle_type:
                print(f"Slot No: {slot.slot_no}")
