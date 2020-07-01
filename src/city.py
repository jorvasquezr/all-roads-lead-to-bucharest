class City:

    def __init__(self, name):
        self.__name = name
        self.__near = {}
    
    def __iter__(self):
        return iter(self.__near.values())

    def add_neighbor(self, neighbor, data):
        self.__near[neighbor] = data
    
    def get_connections(self):
        return self.__near.keys()

    def get_name(self):
        return self.__name

    def get_data(self, neighbor):
        return self.__near[neighbor]

    def get_near(self):
        return self.__near

    def get_nearNames(self):
        listkeys = list(self.__near.keys())
        keysname = []
        for key in listkeys:
            name = key.get_name()
            keysname.append(name)
        return keysname
