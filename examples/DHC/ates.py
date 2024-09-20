# -*- coding: utf-8 -*-
"""
 @Author: zengp
 @Data: 2024-07-10 15:02
 @Email: zengp@kth.se
"""
from rdflib import RDF, RDFS, OWL, Namespace, Graph

g = Graph()


ATES = Namespace("http://example.com/thermal_storage#")
g.bind("ATES", ATES)

"""

Here, we tell our graph what the Brick namespace is. This does *not* mean that
the contents of the Brick schema (which is a graph itself) get pulled in. It
simply allows us to refer to classes and relationships that are defined in the
Brick schema.

"""
BRICK = Namespace("https://brickschema.org/schema/Brick#")
SAREF = Namespace("https://saref.etsi.org/saref4watr")
g.bind("brick", BRICK)


g.add((ATES["cold_water_well"], RDF.type, SAREF.Pit))
g.add((ATES["temperature_sensor_cww"], RDF.type, BRICK.Temperature_sensors))
g.add((ATES["pipe_cww2hex"], RDF.type, BRICK.Pipe))

g.add((ATES["cww_hex"], RDF.type, BRICK.Heat_Exchanger))
g.add((ATES["temperature_sensor_chex_in"], RDF.type, BRICK.Temperature_sensors))
g.add((ATES["temperature_sensor_chex_out"], RDF.type, BRICK.Temperature_sensors))
g.add((ATES["flow_sensor_chex_in"], RDF.type, BRICK.Flow_Sensor))
g.add((ATES["flow_sensor_chex_out"], RDF.type, BRICK.Flow_Sensor))
g.add((ATES["pressure_sensor_chex_in"], RDF.type, BRICK.Pressure_Sensor))
g.add((ATES["pressure_sensor_chex_out"], RDF.type, BRICK.Pressure_Sensor))

g.add((ATES["chex_pipe_whex"], RDF.type, BRICK.Pipe))

g.add((ATES["warm_water_well"], RDF.type, SAREF.Pit))
g.add((ATES["temperature_sensor_www"], RDF.type, BRICK.Temperature_sensors))
g.add((ATES["pipe_www2hex"], RDF.type, BRICK.Pipe))

g.add((ATES["www_hex"], RDF.type, BRICK.Heat_Exchanger))
g.add((ATES["temperature_sensor_whex_in"], RDF.type, BRICK.Temperature_sensors))
g.add((ATES["temperature_sensor_whex_out"], RDF.type, BRICK.Temperature_sensors))
g.add((ATES["flow_sensor_whex_in"], RDF.type, BRICK.Flow_Sensor))
g.add((ATES["flow_sensor_whex_out"], RDF.type, BRICK.Flow_Sensor))
g.add((ATES["pressure_sensor_whex_in"], RDF.type, BRICK.Pressure_Sensor))
g.add((ATES["pressure_sensor_whex_out"], RDF.type, BRICK.Pressure_Sensor))

g.add((ATES["heatpump"], RDF.type, BRICK.Heat_Pump))


# create relationships
g.add((ATES["cold_water_well"], BRICK.hasPoint, ATES["temperature_sensor_cww"]))
g.add((ATES["cold_water_well"], BRICK.feeds, ATES["pipe_cww2hex"]))
g.add((ATES["pipe_cww2hex"], BRICK.feeds, ATES["cww_hex"]))

g.add((ATES["cww_hex"], BRICK.hasPoint, ATES["temperature_sensor_chex_in"]))
g.add((ATES["cww_hex"], BRICK.hasPoint, ATES["temperature_sensor_chex_out"]))
g.add((ATES["cww_hex"], BRICK.hasPoint, ATES["flow_sensor_chex_in"]))
g.add((ATES["cww_hex"], BRICK.hasPoint, ATES["flow_sensor_chex_out"]))
g.add((ATES["cww_hex"], BRICK.hasPoint, ATES["pressure_sensor_chex_in"]))
g.add((ATES["cww_hex"], BRICK.hasPoint, ATES["pressure_sensor_chex_out"]))

g.add((ATES["cww_hex"], BRICK.feeds, ATES["www_hex"]))
g.add((ATES["www_hex"], BRICK.feeds, ATES["cww_hex"]))

g.add((ATES["warm_water_well"], BRICK.hasPoint, ATES["temperature_sensor_www"]))
g.add((ATES["warm_water_well"], BRICK.feeds, ATES["pipe_www2hex"]))
g.add((ATES["pipe_www2hex"], BRICK.feeds, ATES["www_hex"]))

g.add((ATES["www_hex"], BRICK.hasPoint, ATES["temperature_sensor_whex_in"]))
g.add((ATES["www_hex"], BRICK.hasPoint, ATES["temperature_sensor_whex_out"]))
g.add((ATES["www_hex"], BRICK.hasPoint, ATES["flow_sensor_whex_in"]))
g.add((ATES["www_hex"], BRICK.hasPoint, ATES["flow_sensor_whex_out"]))
g.add((ATES["www_hex"], BRICK.hasPoint, ATES["pressure_sensor_whex_in"]))
g.add((ATES["www_hex"], BRICK.hasPoint, ATES["pressure_sensor_whex_out"]))

g.add((ATES["cww_hex"], BRICK.feeds, ATES["heatpump"]))
g.add((ATES["heatpump"], BRICK.feeds, ATES["www_hex"]))


"""
Now our query should execute and return one result (BLDG.VAV2-4.ZN-T)
"""

# sensors = g.query(
#     """SELECT ?sensor WHERE {
#     ?sensor rdf:type brick:Pressure_Sensor
# }"""
# )

# for row in sensors:
#     print(row)

# get pressure sensors in www_hex
sensors = g.query(
    """SELECT ?sensor WHERE {
    ?sensor rdf:type brick:Pressure_Sensor .
    ATES:www_hex brick:hasPoint ?sensor
}"""
)

for row in sensors:
    print(row)

"""
We can "serialize" this model to a file if we want to load it into another program.
"""
with open("ates.ttl", "w") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl"))