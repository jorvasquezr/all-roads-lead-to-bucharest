#!/usr/bin/env python3
import json
from pathlib import Path
import sys
from country import Country
from distance import Distance
from a_StarAlgorithm import A_StarAlgorithm


def main(command, data):
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

    for distance in jsonDistance:
        Distance.add_distance(distance["name"], distance["distanceToBucarest"])

    if(command == "todasLasCiudades"):
        print("Costo\tRuta")
        for n in list(country.get_routes()):
            print(A_StarAlgorithm.calculateBestRouteFrom(country.get_city(n)))
        command =""

    if(command == "ciudad"):
        header= "Costo\tRuta\n"
        if (len(data)==1):
            try:
                r= A_StarAlgorithm.calculateBestRouteFrom(country.get_city(data[0]))
                print(header+r)
            except:
                print("Error: ciudad "+data[0]+" no se encuentra en los datos")
        else:
            print("Error: Formato incorrecto")
        command =""

    if(command == "ciudades"):
        header= "Costo\tRuta\n"
        resultado = ""

        if (len(data)>=1):
            for n in data:
                try:
                    resultado += A_StarAlgorithm.calculateBestRouteFrom(country.get_city(n)) + "\n"
                except:
                    print("Error: ciudad "+n+" no se encuentra en los datos")
            print(header + resultado)
        else:
            print("Error: Formato incorrecto")
        command =""
    if(command == "ayuda"):
        print("Consultar una ciudad: ./main ciudad <nombreCiudad> \nConsultar multiples ciudades: ./main ciudades <nombreCiudad1> <nombreCiudad2> <nombreCiudad3> ... \nConsultar todas las ciudades: ./main todasLasCiudades")
        print("Formato del resultado: Costo [Ciudad1, Ciudad2, ... , Bucharest]")
        command =""
    if(command != ""):
        print("Comando desconocido")
        

def __main__():
    city = ""
    data = []
    try:
        city = sys.argv[1]
        data = sys.argv[2:len(sys.argv)]
        main(city,data)
    except:
        print("Error en el formato, si necesita ayuda intente ./main ayuda")

__main__()


