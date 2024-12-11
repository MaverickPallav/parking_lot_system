from parking_lot import ParkingLot
from vehicle import Vehicle
from floor import Floor
from slot import Slot

# Initialize Parking Lots
parking_lot1 = ParkingLot("PR1234")
parking_lot2 = ParkingLot("PR5678")

# Add floors and slots to parking lots
floor1 = Floor(1, [Slot(i, "Car") for i in range(1, 6)])
floor2 = Floor(2, [Slot(i, "Bike") for i in range(1, 4)] + [Slot(i, "Car") for i in range(4, 8)])
parking_lot1.add_floor(floor1)
parking_lot1.add_floor(floor2)

# Add a new parking lot
floor3 = Floor(1, [Slot(i, "Truck") for i in range(1, 4)])
floor4 = Floor(2, [Slot(i, "Car") for i in range(1, 6)])
parking_lot2.add_floor(floor3)
parking_lot2.add_floor(floor4)

# Example Vehicle
vehicle = Vehicle("Car", "KA01AB1234", "Red")

# Park vehicle in parking lot 1
ticket = parking_lot1.park_vehicle(vehicle)
if ticket:
    print(f"Vehicle parked in PR1234. Ticket ID: {ticket.ticket_id}")

# Unpark vehicle from parking lot 1
if ticket:
    success = parking_lot1.unpark_vehicle(ticket.ticket_id)
    if success:
        print(f"Vehicle unparked from PR1234. Ticket ID: {ticket.ticket_id}")
