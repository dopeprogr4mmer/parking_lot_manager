import heapq

class IParkingStrategy(metaclass=ABCMeta):
    
    @abstractmethod
    def get_nearest_parking_spot():
        pass 

class RandomParking(IParkingStrategy):
    
    def get_nearest_parking_spot(parking_spots):
        pass 

class NearEntryParking(IParkingStrategy):

    
    def get_nearest_parking_spot(parking_spots):
        pass  

class NearExitParking(IParkingStrategy):
    
    def get_nearest_parking_spot(parking_spots):
        pass 