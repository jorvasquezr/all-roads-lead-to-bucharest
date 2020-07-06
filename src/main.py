import json
from pathlib import Path

from city import City
from country import Country

from distance import Distance


base_path_graph = Path(__file__).parent
file_path_graph = (base_path_graph / "./data/country.json")
jsonFileGraph = open(file_path_graph)

jsonCountry = json.loads(jsonFileGraph.read())

country = Country()

for city in jsonCountry:
    city_name = city["name"]
    for route in city["routes"]:
        country.add_route(city_name, route["to"], [route["data"]["distance"],route["data"]["status"],route["data"]["danger"]])


base_path_table = Path(__file__).parent
file_path_table = (base_path_table / "./data/distanceTable.json")
jsonFileTable = open(file_path_table)

jsonDistance = json.loads(jsonFileTable.read())

distances = Distance()

for distance in jsonDistance:
    distances.add_distance(distance["name"], distance["distanceToBucarest"])

