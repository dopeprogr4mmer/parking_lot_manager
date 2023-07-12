from parking_spot import ParkingSpot
from parking_manager import ParkingLotManager
from ticket_generator import TicketGenerator
from payment_handler import PaymentHandler


class EntryManager:

    def enter(gate_number, vehicle_type, vehicle_id, parking_strategy):
        parking_spot_id = ParkingLotManager.allocate_parking_spot(  
                            vehicle_type=vehicle_type, 
                            vehicle_id=vehicle_id,
                            parking_strategy=parking_strategy, 
                            gate_number=gate_number
                        )
        ticket = TicketGenerator(parking_spot_id, vehicle_type, vehicle_id).generate_ticket()


class ExitManager:
    
    def exit(ticket, payment_strategy, payment_method):
        payment_status = PaymentHandler(ticket, payment_strategy, payment_method).pay()
        if payment_status:
            ParkingLotManager.deallocate_parking_spot(ticket)
            