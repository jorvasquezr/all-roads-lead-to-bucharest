from city import City

class Country:

    def __init__(self):
        self.__cities = {}
        self.__amount = 0

    def __iter__(self):
        return iter(self.__cities.values())

    def get_cities(self):
        return self.__cities

    def get_amount(self):
        return self.__amount

    def add_city(self, name):
        self.__amount += 1
        new_city = City(name)
        self.__cities[name] = new_city
        return new_city

    def get_city(self, n):
        if (n in self.__cities):
            return self.__cities[n]
        else:
            return None

    def add_route(self, frm, to, data):
        if (frm not in self.__cities):
            self.add_city(frm)
        if (to not in self.__cities):
            self.add_city(to)

        self.__cities[frm].add_neighbor(self.__cities[to], data)
        self.__cities[to].add_neighbor(self.__cities[frm], data)

    def get_routes(self):
        return self.__cities.keys()
