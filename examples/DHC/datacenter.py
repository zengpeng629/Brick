# -- coding: utf-8 --
"""
 @Author: zengp
 @Data: 2024-09-17 14:18
 @Email: zengp@kth.se
"""

from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()

Datacenter = Namespace("http://example.com/Datacenters#")
g.bind("Datacenter", Datacenter)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

g.add((Datacenter["heat_pump"], RDF.type, BRICK.Heat_Pump))
g.add((Datacenter["IT_workstations"], RDF.type, BRICK.Room))
g.add((Datacenter["cold_water_pipe"], RDF.type, BRICK.Pipe))
g.add((Datacenter["hot_water_pipe"], RDF.type, BRICK.Pipe))
g.add((Datacenter["water_in_temperature_sensor"], RDF.type, BRICK.Temperature_Sensor))
g.add((Datacenter["water_out_temperature_sensor"], RDF.type, BRICK.Temperature_Sensor))
g.add((Datacenter["water_in_flow_sensor"], RDF.type, BRICK.Flow_Sensor))
g.add((Datacenter["water_out_flow_sensor"], RDF.type, BRICK.Flow_Sensor))
g.add((Datacenter["district_cold_water_pipe"], RDF.type, BRICK.District_Cold_Water_Pipe))
g.add((Datacenter["district_hot_water_pipe"], RDF.type, BRICK.District_Hot_Water_Pipe))

# Create relationships
g.add((Datacenter["district_cold_water_pipe"], BRICK.feeds, Datacenter["heat_pump"]))
g.add((Datacenter["heat_pump"], BRICK.feeds, Datacenter["cold_water_pipe"]))
g.add((Datacenter["cold_water_pipe"], BRICK.feeds, Datacenter["IT_workstations"]))
g.add((Datacenter["cold_water_pipe"], BRICK.hasPoint, Datacenter["water_in_temperature_sensor"]))
g.add((Datacenter["cold_water_pipe"], BRICK.hasPoint, Datacenter["water_in_flow_sensor"]))

g.add((Datacenter["hot_water_pipe"], BRICK.feeds, Datacenter["heat_pump"]))
g.add((Datacenter["heat_pump"], BRICK.feeds, Datacenter["district_hot_water_pipe"]))
g.add((Datacenter["IT_workstationsh"], BRICK.feeds, Datacenter["ot_water_pipe"]))
g.add((Datacenter["hot_water_pipe"], BRICK.hasPoint, Datacenter["water_out_temperature_sensor"]))
g.add((Datacenter["hot_water_pipe"], BRICK.hasPoint, Datacenter["water_out_flow_sensor"]))

# """
# We can "serialize" this model to a file if we want to load it into another program.
# """
with open("Datacenter.ttl", "w") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl"))