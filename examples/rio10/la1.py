# -*- coding: utf-8 -*-
"""
 @Author: zengp
 @Data: 2024-09-26 11:29
 @Email: zengp@kth.se
"""

from rdflib import RDF, RDFS, OWL, Namespace, Graph, Literal, XSD

g = Graph()
g.bind("rdfs", RDFS)

LA1 = Namespace("https://twinvista.se/Svenska-Bostäder/Rio10/Sandhamnsgatan10/LA1#")
g.bind("la1", LA1)
BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)
S223 = Namespace("http://data.ashrae.org/standard223#")
g.bind("s223", S223)

"""
1. Declare the connectable objects
"""
g.add((LA1["VVX"], RDF.type, S223.HeatExchanger))
g.add((LA1["VVX"], RDFS.comment, Literal("This is the heat exchanger VVX", datatype=XSD.string)))

"""
1.1.1 Brown part declaration
"""
g.add((LA1["exhaust_air_outside_space"], RDF.type, BRICK.Outdoor_Area))
g.add((LA1["exhaust_air_outside_space"], RDFS.comment, Literal("Outside space in for exhaust air", datatype=XSD.string)))

g.add((LA1["brown_duct"], RDF.type, S223.Duct))
g.add((LA1["brown_duct"], RDFS.comment, Literal("Outlet brown duct in la1", datatype=XSD.string)))

g.add((LA1["brown_duct_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["brown_duct_outlet_point"], RDFS.comment, Literal("Outlet point of brown duct", datatype=XSD.string)))

g.add((LA1["brown_duct_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["brown_duct_inlet_point"], RDFS.comment, Literal("Inlet point of brown duct", datatype=XSD.string)))

g.add((LA1["ST2:2_airdamper"], RDF.type, BRICK.Return_Damper))
g.add((LA1["ST2:2_airdamper"], RDFS.comment, Literal("Return air damper, ST2:2", datatype=XSD.string)))

g.add((LA1["ST2:2_airdamper_position"], RDF.type, S223.Property))
g.add((LA1["ST2:2_airdamper_position"], RDFS.comment, Literal("Position of the damper, ST2:2", datatype=XSD.string)))

"""
1.1.2 Make the connections in the brown part
"""
g.add((LA1["brown_duct"], S223.cnx, LA1["brown_duct_inlet_point"]))
g.add((LA1["brown_duct"], S223.cnx, LA1["brown_duct_outlet_point"]))
g.add((LA1["brown_duct_outlet_point"], S223.cnx, LA1["exhaust_air_outside_space"]))
g.add((LA1["ST2:2_airdamper"], S223.cnx, LA1["brown_duct_inlet_point"]))
g.add((LA1["ST2:2_airdamper_position"], S223.cnx, LA1["ST2:2_airdamper"]))

"""
1.2 Blue part declaration
"""
g.add((LA1["supply_air_outdorr_space"], RDF.type, BRICK.Outdoor_Area))
g.add((LA1["supply_air_outdorr_space"], RDFS.comment, Literal("Outside space in for supply air", datatype=XSD.string)))

g.add((LA1["blue_duct"], RDF.type, S223.Duct))
g.add((LA1["blue_duct"], RDFS.comment, Literal("Inlet air blue duct in la1", datatype=XSD.string)))

g.add((LA1["blue_duct_junction"], RDF.type, S223.Junction))
g.add((LA1["blue_duct_junction"], RDFS.comment, Literal("Junction of the blue duct", datatype=XSD.string)))

g.add((LA1["blue_duct_outlet_point_vvx"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["blue_duct_outlet_point_vvx"], RDFS.comment, Literal("Outlet point of the blue duct to VVX", datatype=XSD.string)))

g.add((LA1["blue_duct_outlet_point_damper"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["blue_duct_outlet_point_damper"], RDFS.comment, Literal("Outlet point of the blue duct to the ST2:1", datatype=XSD.string)))
g.add((LA1["ST2:1_airdamper"], RDF.type, BRICK.Return_Damper))
g.add((LA1["ST2:1_airdamper"], RDFS.comment, Literal("Return air damper, ST2:1", datatype=XSD.string)))
g.add((LA1["ST2:1_airdamper_position"], RDF.type, S223.Property))
g.add((LA1["ST2:1_airdamper_position"], RDFS.comment, Literal("Position of the damper, ST2:1", datatype=XSD.string)))

g.add((LA1["blue_duct_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["blue_duct_inlet_point"], RDFS.comment, Literal("Inlet point of the blue duct", datatype=XSD.string)))

g.add((LA1["GT41_temperature_sensor"], RDF.type, S223.TemperatureSensor))
g.add((LA1["GT41_temperature_sensor"], RDFS.comment, Literal("GT41 temperature sensor, measures the temperature of the inlet air", datatype=XSD.string)))

g.add((LA1["inlet_air_filter"], RDF.type, BRICK.IntakeAirFilter))
g.add((LA1["inlet_air_filter"], RDFS.comment, Literal("Filter of inlet air", datatype=XSD.string)))

g.add((LA1["inlet_air_filter_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["inlet_air_filter_outlet_point"], RDFS.comment, Literal("Outlet point of the inlet air filter", datatype=XSD.string)))

g.add((LA1["ST1_outside_airdamper"], RDF.type, BRICK.Outside_Damper))
g.add((LA1["ST1_outside_airdamper"], RDFS.comment, Literal("Outside air damper, ST1", datatype=XSD.string)))

g.add((LA1["ST1_outside_airdamper_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["ST1_outside_airdamper_outlet_point"], RDFS.comment, Literal("Outlet point of the ST1 outside air damper", datatype=XSD.string)))

g.add((LA1["TF_supply_air_fan"], RDF.type, BRICK.Supply_Fan))
g.add((LA1["TF_supply_air_fan"], RDFS.comment, Literal("Supply air fan TF", datatype=XSD.string)))

g.add((LA1["TF_supply_air_fan_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["TF_supply_air_fan_outlet_point"], RDFS.comment, Literal("Outlet point of the supply air fan", datatype=XSD.string)))

g.add((LA1["FO_supply_air_fan_efficiency"], RDF.type, S223.Property))
g.add((LA1["FO_supply_air_fan_efficiency"], RDFS.comment, Literal("Supply air fan efficiency FO", datatype=XSD.string)))

"""
1.2.1 Make the connections in the blue part
"""
g.add((LA1["supply_air_outdorr_space"], S223.cnx, LA1["blue_duct_inlet_point"]))
g.add((LA1["GT41_temperature_sensor"], S223.cnx, LA1["blue_duct_inlet_point"]))

g.add((LA1["blue_duct_inlet_point"], S223.cnx, LA1["inlet_air_filter"]))
g.add((LA1["inlet_air_filter"], S223.cnx, LA1["inlet_air_filter_outlet_point"]))

g.add((LA1["inlet_air_filter_outlet_point"], S223.cnx, LA1["ST1_outside_airdamper"]))
g.add((LA1["ST1_outside_airdamper"], S223.cnx, LA1["ST1_outside_airdamper_outlet_point"]))
g.add((LA1["ST1_outside_airdamper_outlet_point"], S223.cnx, LA1["TF_supply_air_fan"]))
g.add((LA1["FO_supply_air_fan_efficiency"], S223.cnx, LA1["TF_supply_air_fan"]))
g.add((LA1["TF_supply_air_fan"], S223.cnx, LA1["TF_supply_air_fan_outlet_point"]))

g.add((LA1["TF_supply_air_fan_outlet_point"], S223.cnx, LA1["blue_duct_junction"]))
g.add((LA1["blue_duct_junction"], S223.cnx, LA1["blue_duct_outlet_point_vvx"]))
g.add((LA1["blue_duct_outlet_point_vvx"], S223.cnx, LA1["VVX"]))
g.add((LA1["blue_duct_junction"], S223.cnx, LA1["blue_duct_outlet_point_damper"]))
g.add((LA1["blue_duct_outlet_point_damper"], S223.cnx, LA1["ST2:1_airdamper"]))
g.add((LA1["ST2:1_airdamper"], S223.cnx, LA1["ST2:1_airdamper_position"]))

"""
3. Build the graph
"""
with open("rio10_la1.ttl", "w") as f:
    f.write(g.serialize(format="ttl"))

"""
Test query to find the brown_duct
"""
# Define the query with prefixes
query = """
SELECT ?duct WHERE {
    ?duct rdf:type s223:Duct .
    ?duct s223:cnx+ la1:VVX .
}
"""

# Execute the query
ducts = g.query(query)

# Print the results
for row in ducts:
    print(row)
