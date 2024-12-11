import unittest
from parking_lot import ParkingLot
from vehicle import Vehicle
from floor import Floor
from slot import Slot

class TestParkingLotSystem(unittest.TestCase):

    def setUp(self):
        self.parking_lot1 = ParkingLot("PR1234")
        self.parking_lot2 = ParkingLot("PR5678")
        
        floor1 = Floor(1, [Slot(i, "Car") for i in range(1, 6)])
        floor2 = Floor(2, [Slot(i, "Bike") for i in range(1, 4)] + [Slot(i, "Car") for i in range(4, 8)])
        self.parking_lot1.add_floor(floor1)
        self.parking_lot1.add_floor(floor2)
        
        floor3 = Floor(1, [Slot(i, "Truck") for i in range(1, 4)])
        floor4 = Floor(2, [Slot(i, "Car") for i in range(1, 6)])
        self.parking_lot2.add_floor(floor3)
        self.parking_lot2.add_floor(floor4)

    def test_park_vehicle_multiple_lots(self):
        vehicle = Vehicle("Car", "KA01AB1234", "Red")
        ticket1 = self.parking_lot1.park_vehicle(vehicle)
        self.assertIsNotNone(ticket1)
        
        vehicle2 = Vehicle("Truck", "KA01AB5678", "Blue")
        ticket2 = self.parking_lot2.park_vehicle(vehicle2)
        self.assertIsNotNone(ticket2)

    def test_add_new_vehicle_type(self):
        Vehicle.add_vehicle_type("Bus")
        vehicle = Vehicle("Bus", "KA01AB9999", "Green")
        self.assertEqual(vehicle.vehicle_type, "Bus")

if __name__ == "__main__":
    unittest.main()
