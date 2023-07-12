from metaclass import ABCMeta, abstractmethod

class IVehicleParking(metaclass=ABCMeta):
    """ Interface class to intantiate parking_spot object for different types of vehicle objects """

    @staticmethod
    @abstractmethod
    def allocate_parking_spot():
        pass

    @staticmethod
    @abstractmethod
    def deallocate_parking_spot():
        pass


@singelton
class TwoWheelerParking(IVehicleParking):
    """ concrete class to intantiate TwoWheeler manager object """

    avialable_parking_spots = []
    reserved_parking_spots = []

    def allocate_parking_spot(gate_number, parking_strategy):
        nearest_parking_spot = parking_strategy(gate_number, avialable_parking_spots)
        nearest_parking_spot.park_vehicle(vehicle_id=vehicle_id, vehicle_type=vehicle_type)
        avialable_parking_spots.remove(nearest_parking_spot)
        reserved_parking_spots.append(nearest_parking_spot)
        return nearest_parking_spot.get_spot_id()

    def deallocate_parking_spot(parking_spot_id):
        parking_spot = [_ for _  in avialable_parking_spots if _.get_spot_id()==parking_spot_id][0]
        reserved_parking_spots.remove(parking_spot) 
        avialable_parking_spots.append(parking_spot)


@singelton
class DMVParking(IVehicleParking):
    """ concrete class to intantiate DMV manager object """

    avialable_parking_spots = []
    reserved_parking_spots = []

    def allocate_parking_spot(gate_number, parking_strategy):
        nearest_parking_spot = parking_strategy(gate_number, avialable_parking_spots)
        avialable_parking_spots.remove(nearest_parking_spot)
        reserved_parking_spots.append(nearest_parking_spot)


@singelton
class LargeVehicleParking(IVehicleParking):
    """ concrete class to intantiate LargeVehicle manager object """

    avialable_parking_spots = []
    reserved_parking_spots = []

    def allocate_parking_spot(gate_number, parking_strategy):
        nearest_parking_spot = parking_strategy(gate_number, avialable_parking_spots)
        avialable_parking_spots.remove(nearest_parking_spot)
        reserved_parking_spots.append(nearest_parking_spot)


class ParkingLotManager:
    """ Factory class for managing parking lot for different types of vehicles """ 

    vehicle_object_mapping = {
        "two-wheeler": TwoWheelerParking(),
        "dmv": DMVParking(),
        "large-vehicle": LargeVehicleParking()
    }

    @staticmethod
    def allocate_parking_spot(vehicle_type, parking_strategy, gate_number):
    	parking_area = ParkingLotManager.vehicle_object_mapping.get(vehicle_type, None)
    	parking_spot_id = parking_area.allocate_parking_spot(gate_number, parking_strategy)
    	return parking_spot_id

    @staticmethod
    def deallocate_parking_spot(ticket):
    	parking_area = ParkingLotManager.vehicle_object_mapping.get(ticket.vehicle_type, None)
    	parking_area.deallocate_parking_spot(ticket.parking_spot_id)