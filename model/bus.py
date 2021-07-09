from category.category import Category

class Bus:
    def __init__(self, bus_id, category):
        self.bus_id = bus_id
        self.route=[]
        self.bus_category=Category(category)

    def get_regions_crossed(self, ini_time, end_time):
    	regions = []
    	count = 0
    	for station in route:
    		if station.timestamp > ini_time and station.timestamp < end_time and station.region not in regions:
    			regions.append(station.region)
    			count = count +1
    	return count

