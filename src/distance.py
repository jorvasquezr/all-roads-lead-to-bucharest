class Distance:

    def __init__(self):
        self.__distances = {}
        self.__amount = 0

    def __iter__(self):
        return iter(self.__distances.values())

    def get_cities(self):
        return self.__distances

    def get_amount(self):
        return self.__amount

    def add_distance(self, cityName, distance):
        self.__amount += 1
        self.__distances[cityName] = distance
    
    def get_distance(self, cityName):
        if (cityName in self.__distances):
            return self.__distances[cityName]
        else:
            return None
    
    def get_distances(self):
        return self.__distances.keys()