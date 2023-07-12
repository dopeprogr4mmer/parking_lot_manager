from datetime import datetime

class TicketGenerator:

    ticket_id = 1001

    def __init__(self, parking_spot_id, vehicle_type, vehicle_id):
        self.ticket_id = TicketGenerator.ticket_id 
        TicketGenerator.ticket_id += 1
        self.parking_time = datetime.now() 
        self.parking_spot_id = parking_spot_id
        self.vehicle_type = vehicle_type
        self.vehicle_id = vehicle_id

    def generate_ticket(self):
        ticket = {
            "ticket_id": self.ticket_id,
            "parking_time": self.parking_time,
            "parking_spot": self.parking_spot_id,
            "vehicle_type": self.vehicle_type,
            "vehicle_plate_number": self.vehicle_id
        }
        return ticket