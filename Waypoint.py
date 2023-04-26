class Waypoint:
    def __init__(self, number, latitude, longitude, altitude):
        self.number = number
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def to_string(self):
        return "{0}\t0\t3\t16\t0\t0\t0\t0\t{1}\t{2}\t{3}\t1\n".format(
            self.number, self.latitude, self.longitude, self.altitude
        )
