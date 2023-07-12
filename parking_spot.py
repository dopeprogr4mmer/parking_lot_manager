class ParkingSpot:
    """ class for inititalizing parking spot object """

    def __init__(self, spot_id):
        self._id = spot_id
        self.vehicle_id = None
        self.vehicle_type = None
        self.parking_status = False
        
    def park_vehicle(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.parking_status = True 

    def unpark_vehicle(Self):
        self.vehicle_id = None
        self.vehicle_type = None
        self.parking_status = False 

    def get_spot_id(self):
        return self._id

if __name__ == "__main__":
    obj_list = []
    for id_ in range(101, 300):
        obj_list.append(ParkingSpot(id_))
    print(len(obj_list))
    for obj in obj_list:
        if obj.id == 105:
            print(obj.parking_status)
