# -*- coding: utf-8 -*-
"""
 @Author: zengp
 @Data: 2024-09-05 16:12
 @Email: zengp@kth.se
"""

from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()


Building = Namespace("http://example.com/Buildings#")
g.bind("Building", Building)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

g.add((Building["hot_water_distribution_system"], RDF.type, BRICK.Water_Distribution))

g.add((Building["pipe_1"], RDF.type, BRICK.Pipe))
g.add((Building["floor_1"], RDF.type, BRICK.Floor))
g.add((Building["room_101"], RDF.type, BRICK.Room))
g.add((Building["hot_water_meter_101"], RDF.type, BRICK.Hot_Water_Meter))
g.add((Building["radiator_101"], RDF.type, BRICK.Radiator))
g.add((Building["temperature_sensor_101"], RDF.type, BRICK.Temperature_Sensor))
g.add((Building["flow_meter_101"], RDF.type, BRICK.Flow_Meter))

g.add((Building["floor_2"], RDF.type, BRICK.Floor))
g.add((Building["pipe_2"], RDF.type, BRICK.Pipe))
g.add((Building["room_201"], RDF.type, BRICK.Room))
g.add((Building["hot_water_meter_201"], RDF.type, BRICK.Hot_Water_Meter))
g.add((Building["radiator_201"], RDF.type, BRICK.Radiator))
g.add((Building["temperature_sensor_201"], RDF.type, BRICK.Temperature_Sensor))
g.add((Building["flow_meter_201"], RDF.type, BRICK.Flow_Meter))

g.add((Building["floor_3"], RDF.type, BRICK.Floor))
g.add((Building["pipe_3"], RDF.type, BRICK.Pipe))
g.add((Building["room_301"], RDF.type, BRICK.Room))
g.add((Building["hot_water_meter_301"], RDF.type, BRICK.Hot_Water_Meter))
g.add((Building["radiator_301"], RDF.type, BRICK.Radiator))
g.add((Building["temperature_sensor_301"], RDF.type, BRICK.Temperature_Sensor))
g.add((Building["flow_meter_301"], RDF.type, BRICK.Flow_Meter))

# Create relationships
g.add((Building["hot_water_distribution_system"], BRICK.feeds, Building["pipe_1"]))
g.add((Building["hot_water_distribution_system"], BRICK.feeds, Building["pipe_2"]))
g.add((Building["hot_water_distribution_system"], BRICK.feeds, Building["pipe_3"]))

g.add((Building["floor_1"], BRICK.hasPart, Building["room_101"]))
g.add((Building["floor_2"], BRICK.hasPart, Building["room_201"]))
g.add((Building["floor_3"], BRICK.hasPart, Building["room_301"]))

g.add((Building["room_101"], BRICK.hasPoint, Building["hot_water_meter_101"]))
g.add((Building["room_101"], BRICK.hasPoint, Building["radiator_101"]))
g.add((Building["room_201"], BRICK.hasPoint, Building["hot_water_meter_201"]))
g.add((Building["room_201"], BRICK.hasPoint, Building["radiator_201"]))
g.add((Building["room_301"], BRICK.hasPoint, Building["hot_water_meter_301"]))
g.add((Building["room_301"], BRICK.hasPoint, Building["radiator_301"]))


g.add((Building["pipe_1"], BRICK.feeds, Building["radiator_101"]))
g.add((Building["radiator_101"], BRICK.hasPoint, Building["temperature_sensor_101"]))
g.add((Building["radiator_101"], BRICK.hasPoint, Building["flow_meter_101"]))
g.add((Building["pipe_2"], BRICK.feeds, Building["radiator_201"]))
g.add((Building["radiator_201"], BRICK.hasPoint, Building["temperature_sensor_201"]))
g.add((Building["radiator_201"], BRICK.hasPoint, Building["flow_meter_201"]))
g.add((Building["pipe_3"], BRICK.feeds, Building["radiator_301"]))
g.add((Building["radiator_301"], BRICK.hasPoint, Building["temperature_sensor_301"]))
g.add((Building["radiator_301"], BRICK.hasPoint, Building["flow_meter_301"]))

# Query 1: Find all temperature sensors
sensors = g.query(
    """SELECT ?sensor WHERE {
    ?sensor rdf:type brick:Temperature_Sensor
}"""
)

for row in sensors:
    print(row)

# Query 2: Find temperature sensor in floor 3
sensors_floor3 = g.query(
    """SELECT ?sensor WHERE {
    ?sensor rdf:type brick:Temperature_Sensor .
    ?radiator brick:hasPoint ?sensor .
    ?room brick:hasPoint ?radiator .
    Building:floor_3 brick:hasPart ?room
}"""
)

for row in sensors_floor3:
    print(row)
    
# """
# We can "serialize" this model to a file if we want to load it into another program.
# """
with open("building.ttl", "w") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl"))