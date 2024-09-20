# -- coding: utf-8 --
"""
 @Author: zengp
 @Data: 2024-08-23 11:08
 @Email: zengp@kth.se
"""

from rdflib import RDF, Namespace, Graph

g = Graph()

PVT = Namespace("http://example.com/PVT#")
g.bind("PVT", PVT)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
# g.bind("brick", BRICK)

#1. Declare the components
g.add((PVT["PVT_collector"], RDF.type, BRICK.PVT_Panel))
g.add((PVT["heat_exchanger"], RDF.type, BRICK.Heat_Exchanger))
g.add((PVT["in_temperature_sensor"], RDF.type, BRICK.Temperature_sensors))
g.add((PVT["in_flow_sensor"], RDF.type, BRICK.Flow_Sensor))
g.add((PVT["in_pressure_sensor"], RDF.type, BRICK.Pressure_Sensor))
g.add((PVT["pump"], RDF.type, BRICK.Pump))
g.add((PVT["out_temperature_sensor"], RDF.type, BRICK.Temperature_sensors))
g.add((PVT["out_flow_sensor"], RDF.type, BRICK.Flow_Sensor))
g.add((PVT["out_pressure_sensor"], RDF.type, BRICK.Pressure_Sensor))
g.add((PVT["control_valve"], RDF.type, BRICK.Control_Valve))

g.add((PVT["hex_temperature_sensor"], BRICK.type, BRICK.Temperature_sensors))
g.add((PVT["hex_flow_sensor"], BRICK.type, BRICK.Flow_Sensor))
g.add((PVT["hex_pressure_sensor"], BRICK.type, BRICK.Pressure_Sensor))

g.add((PVT["solar_irradiance_sensor"], BRICK.type, BRICK.Solar_Irradiance_Sensor))
g.add((PVT["electric_meter"], BRICK.type, BRICK.Electric_Meter))

#2. Create the relationships between the components
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["in_temperature_sensor"]))
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["in_flow_sensor"]))
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["in_pressure_sensor"]))
g.add((PVT["PVT_collector"], BRICK.isFedBy, PVT["pump"]))
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["out_temperature_sensor"]))
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["out_flow_sensor"]))
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["out_pressure_sensor"]))
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["control_valve"]))
g.add((PVT["PVT_collector"], BRICK.feeds, PVT["heat_exchanger"]))
g.add((PVT["PVT_collector"], BRICK.feeds, PVT["electric_meter"]))
g.add((PVT["PVT_collector"], BRICK.hasPoint, PVT["solar_irradiance_sensor"]))

g.add((PVT["heat_exchanger"], BRICK.hasPoint, PVT["hex_temperature_sensor"]))
g.add((PVT["heat_exchanger"], BRICK.feeds, PVT["pump"]))
g.add((PVT["heat_exchanger"], BRICK.hasPoint, PVT["hex_flow_sensor"]))
g.add((PVT["heat_exchanger"], BRICK.hasPoint, PVT["hex_pressure_sensor"]))

"""
We can "serialize" this model to a file if we want to load it into another program.
"""
with open("pvt.ttl", "w") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl"))