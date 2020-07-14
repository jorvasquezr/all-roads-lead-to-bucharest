class Distance:
    distances = {}

    @staticmethod
    def add_distance(cityName, distance):
        Distance.distances[cityName] = distance

    @staticmethod
    def get_distance(cityName):
        if (cityName in Distance.distances):
            return Distance.distances[cityName]
        else:
            return None

    @staticmethod
    def get_distances():
        return Distance.distances.keys()
    @staticmethod
    def get_distancesValues():
        return Distance.distances.values()
    
