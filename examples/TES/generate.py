# -*- coding: utf-8 -*-
"""
 @Author: zengp
 @Data: 2024-07-03 15:07
 @Email: zengp@kth.se
"""

from rdflib import RDF, RDFS, OWL, Namespace, Graph

"""

A Brick model is a digital representation of the resources and relationships
inside a building described using the Brick schema.

A Brick model is maintained/query through the abstraction of a Graph. A Graph
consists of triples (subject, predicate, object). Subjects and objects can be
"classes" or "instances of classes" (sometimes called individuals, instances or
entities). Predicates are the "directed edges" in the graph and are sometimes
referred to as such

    +---------+        Predicate         +--------+
    | Subject |------------------------->| Object |
    +---------+                          +--------+

"""

g = Graph()

"""

Now that we have the graph object we have to decide what to put into it. At the
very least, we probably want to put in triples describing the "things" in our
building. In Brick, "things" have a name and a class, which tells us what kind
of thing they are.

The Brick schema defines a set of classes that are ready for you to use. Brick
classes includes HVAC equipment, lighting equipment, electrical equipment,
rooms and other spatial elements, zones, and points like sensors and setpoints.
You can find a list of the classes supported by Brick online:
https://brickschema.org/ontology

Before we start adding things to our Brick model, we need to define a namespace.
A "namespace" is a way of grouping information so that the names we choose for
things don't conflict with names in other Brick models (more on that later).

Namespaces are URLs; they do not have to actually point to a real web resource,
but it is of course helpful if they point to some documentation (try going to
https://brickschema.org/schema/Brick#Air_Handler_Unit as an example).

We will choose an arbitrary URL for our namespace and refer to it by the
nickname "bldg" for convenience. "bldg" is also called a "prefix".

"""

TES = Namespace("http://example.com/thermal_storage#")
g.bind("tes", TES)

"""

Here, we tell our graph what the Brick namespace is. This does *not* mean that
the contents of the Brick schema (which is a graph itself) get pulled in. It
simply allows us to refer to classes and relationships that are defined in the
Brick schema.

"""
BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)


"""

Now we can add instances to our Brick model (building graph). We use the RDF
namespace (imported above) in addition to the BRICK and BLDG namespaces.
"RDF.type" is the "type" predicate defined within the RDF graph. The RDF.type
predicate is how we create "instances" of Brick classes.

"""

# (subject, predicate, object)
g.add((TES["thermal_storage"], RDF.type, BRICK.Energy_Storage))
g.add((TES["high_temperature_tank"], RDF.type, BRICK.Water_Tank))
g.add((TES["temperature_sensor_htt_in"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["temperature_sensor_htt_out"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["flow_sensor_htt_in"], RDF.type, BRICK.Flow_Sensor))
g.add((TES["flow_sensor_htt_out"], RDF.type, BRICK.Flow_Sensor))


g.add((TES["low_temperature_tank"], RDF.type, BRICK.Water_Tank))
g.add((TES["temperature_sensor_ltt_in"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["temperature_sensor_ltt_out"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["flow_sensor_ltt_in"], RDF.type, BRICK.Flow_Sensor))
g.add((TES["flow_sensor_ltt_out"], RDF.type, BRICK.Flow_Sensor))

g.add((TES["high_heat_exchanger"], RDF.type, BRICK.Heat_Exchanger))
g.add((TES["temperature_sensor_hhex_in"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["temperature_sensor_hhex_out"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["flow_sensor_hhex_in"], RDF.type, BRICK.Flow_Sensor))
g.add((TES["flow_sensor_hhex_out"], RDF.type, BRICK.Flow_Sensor))


g.add((TES["low_heat_exchanger"], RDF.type, BRICK.Heat_Exchanger))
g.add((TES["temperature_sensor_lhex_in"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["temperature_sensor_lhex_out"], RDF.type, BRICK.Temperature_sensors))
g.add((TES["flow_sensor_lhex_in"], RDF.type, BRICK.Flow_Sensor))
g.add((TES["flow_sensor_lhex_out"], RDF.type, BRICK.Flow_Sensor))


# declare entities first
# g.add((TES["temperature_sensors"], RDF.type, BRICK.Temperature_Sensor))

# declare edges
# g.add((TES["thermal_storage"], BRICK.hasPart, TES["high_temperature_tank"]))
# g.add((TES["thermal_storage"], BRICK.hasPart, TES["low_temperature_tank"]))
# g.add((TES["thermal_storage"], BRICK.hasPart, TES["high_heat_exchanger"]))
# g.add((TES["thermal_storage"], BRICK.hasPart, TES["low_heat_exchanger"]))

g.add((TES["high_temperature_tank"], BRICK.hasPoint, TES["temperature_sensor_htt_in"]))
g.add((TES["high_temperature_tank"], BRICK.feed, TES["low_heat_exchanger"]))
g.add((TES["high_temperature_tank"], BRICK.haspart, TES["high_heat_exchanger"]))
g.add((TES["high_temperature_tank"], BRICK.hasPoint, TES["temperature_sensor_htt_out"]))
g.add((TES["high_temperature_tank"], BRICK.hasPoint, TES["flow_sensor_htt_in"]))
g.add((TES["high_temperature_tank"], BRICK.hasPoint, TES["flow_sensor_htt_out"]))

g.add((TES["low_temperature_tank"], BRICK.hasPoint, TES["temperature_sensor_ltt_in"]))
g.add((TES["low_temperature_tank"], BRICK.feed, TES["high_heat_exchanger"]))
g.add((TES["low_temperature_tank"], BRICK.haspart, TES["low_heat_exchanger"]))
g.add((TES["low_temperature_tank"], BRICK.hasPoint, TES["temperature_sensor_ltt_out"]))
g.add((TES["low_temperature_tank"], BRICK.hasPoint, TES["flow_sensor_ltt_in"]))
g.add((TES["low_temperature_tank"], BRICK.hasPoint, TES["flow_sensor_ltt_out"]))

g.add((TES["high_heat_exchanger"], BRICK.hasPoint, TES["temperature_sensor_hhex_in"]))
g.add((TES["high_heat_exchanger"], BRICK.hasPoint, TES["temperature_sensor_hhex_out"]))
g.add((TES["high_heat_exchanger"], BRICK.hasPoint, TES["flow_sensor_hhex_in"]))
g.add((TES["high_heat_exchanger"], BRICK.hasPoint, TES["flow_sensor_hhex_out"]))

g.add((TES["low_heat_exchanger"], BRICK.hasPoint, TES["temperature_sensor_lhex_in"]))
g.add((TES["low_heat_exchanger"], BRICK.hasPoint, TES["temperature_sensor_lhex_out"]))
g.add((TES["low_heat_exchanger"], BRICK.hasPoint, TES["flow_sensor_lhex_in"]))
g.add((TES["low_heat_exchanger"], BRICK.hasPoint, TES["flow_sensor_lhex_out"]))

"""
We can "serialize" this model to a file if we want to load it into another program.
"""
with open("tes.ttl", "w") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl"))