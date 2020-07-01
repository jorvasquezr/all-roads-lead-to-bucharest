import json
from pathlib import Path

from city import City
from country import Country



base_path = Path(__file__).parent
file_path = (base_path / "./data/country.json")
jsonFile = open(file_path)

jsonCountry = json.loads(jsonFile.read())

country = Country()

for city in jsonCountry:
    city_name = city["name"]
    for route in city["routes"]:
        country.add_route(city_name, route["to"], [route["data"]["distance"],route["data"]["status"],route["data"]["danger"]])

