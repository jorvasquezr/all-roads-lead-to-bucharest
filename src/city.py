class City:

    def __init__(self, name):
        self.__name = name
        self.__near = {}
    
    def add_neighbor(self, neighbor, data):
        self.__near[neighbor] = data
    
    def get_connections(self):
        return self.__near.keys()

    def get_name(self):
        return self.__name

    def get_data(self, neighbor):
        return self.__near[neighbor]
