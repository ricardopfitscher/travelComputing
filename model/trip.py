

class Trip:
    def __init__(self, bus, route, boarding_time, boarding_station):
        self.bus_id= bus
        self.route_id =route
        self.boarding_time = boarding_time
        self.boarding_station= boarding_station
        self.disembark_time= ''
        self.disembark_station = ''
        self.trip_cost = 0.0
