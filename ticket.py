class Ticket:
    def __init__(self, parking_lot_id, floor_no, slot_no):
        self.ticket_id = f"{parking_lot_id}_{floor_no}_{slot_no}"
