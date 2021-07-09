from datetime import datetime

class Station:
    def __init__(self, name, latitude, longitude, region):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.region = region
        self.timestamp = ""

    def set_current_timestamp(self):
    	self.timestamp = datetime.now()

    def set_timestamp(self, time):
    	self.timestamp = time