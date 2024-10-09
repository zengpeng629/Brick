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
REC = Namespace("https://w3id.org/rec#")
g.bind("rec", REC)

"""
1. Declare the connectable objects
"""
g.add((LA1["VVX"], RDF.type, BRICK.Air_Handler_Unit))
g.add((LA1["VVX"], RDFS.comment, Literal("FTX", datatype=XSD.string)))

"""
1.1.1 Brown part declaration
"""
g.add((LA1["exhaust_air_outside_space"], RDF.type, BRICK.Outdoor_Area))
g.add((LA1["exhaust_air_outside_space"], RDFS.comment, Literal("Outside space in for exhaust air", datatype=XSD.string)))

g.add((LA1["brown_duct"], RDF.type, S223.Duct))
g.add((LA1["brown_duct"], RDFS.comment, Literal("Outlet brown duct in la1", datatype=XSD.string)))

g.add((LA1["brown_duct_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["brown_duct_outlet_point"], RDFS.comment, Literal("Outlet point of brown duct", datatype=XSD.string)))

g.add((LA1["brown_duct_inlet_point_damper"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["brown_duct_inlet_point_damper"], RDFS.comment, Literal("Inlet point of brown duct from damper", datatype=XSD.string)))

g.add((LA1["brown_duct_inlet_point_vvx"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["brown_duct_inlet_point_vvx"], RDFS.comment, Literal("Inlet point of brown duct from vvx", datatype=XSD.string)))

g.add((LA1["ST2:2_airdamper"], RDF.type, BRICK.Return_Damper))
g.add((LA1["ST2:2_airdamper"], RDFS.comment, Literal("Return air damper, ST2:2", datatype=XSD.string)))

g.add((LA1["ST2:2_airdamper_position"], RDF.type, S223.Property))
g.add((LA1["ST2:2_airdamper_position"], RDFS.comment, Literal("Position of the damper, ST2:2", datatype=XSD.string)))
g.add((LA1["ST2:2_airdamper_position"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_AU03.txt", datatype=XSD.string)))
"""
1.1.2 Make the connections in the brown part
"""
g.add((LA1["ST2:2_airdamper"], S223.cnx, LA1["brown_duct_inlet_point_damper"]))
g.add((LA1["ST2:2_airdamper_position"], S223.cnx, LA1["ST2:2_airdamper"]))
g.add((LA1["VVX"], S223.cnx, LA1["brown_duct_inlet_point_vvx"]))
g.add((LA1["brown_duct"], S223.cnx, LA1["brown_duct_inlet_point_damper"]))
g.add((LA1["brown_duct"], S223.cnx, LA1["brown_duct_inlet_point_vvx"]))

g.add((LA1["brown_duct"], S223.cnx, LA1["brown_duct_outlet_point"]))
g.add((LA1["brown_duct_outlet_point"], S223.cnx, LA1["exhaust_air_outside_space"]))


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
g.add((LA1["ST2:1_airdamper_position"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_AU03.txt", datatype=XSD.string)))

g.add((LA1["blue_duct_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["blue_duct_inlet_point"], RDFS.comment, Literal("Inlet point of the blue duct from outside", datatype=XSD.string)))

g.add((LA1["blue_duct_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["blue_duct_outlet_point"], RDFS.comment, Literal("Outlet point of the blue duct to filter", datatype=XSD.string)))

g.add((LA1["GT41_temperature_sensor"], RDF.type, S223.TemperatureSensor))
g.add((LA1["GT41_temperature_sensor"], RDFS.comment, Literal("GT41 temperature sensor, measures the temperature of the inlet air", datatype=XSD.string)))
g.add((LA1["GT41_temperature_sensor"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_AI03.txt", datatype=XSD.string)))

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
g.add((LA1["FO_supply_air_fan_efficiency"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_AU01.txt", datatype=XSD.string)))

"""
1.2.1 Make the connections in the blue part
"""
g.add((LA1["supply_air_outdorr_space"], S223.cnx, LA1["blue_duct_inlet_point"]))
g.add((LA1["blue_duct_inlet_point"], S223.cnx, LA1["blue_duct"]))
g.add((LA1["GT41_temperature_sensor"], S223.cnx, LA1["blue_duct"]))
g.add((LA1["blue_duct"], S223.cnx, LA1["blue_duct_outlet_point"]))
g.add((LA1["blue_duct_outlet_point"], S223.cnx, LA1["inlet_air_filter"]))
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
1.3.1 red part declaration
"""
g.add((LA1["red_duct"], RDF.type, S223.Duct))
g.add((LA1["red_duct"], RDFS.comment, Literal(" before heating red duct in la1", datatype=XSD.string)))

g.add((LA1["red_duct_heated"], RDF.type, S223.Duct))
g.add((LA1["red_duct_heated"], RDFS.comment, Literal("After heating red duct in la1", datatype=XSD.string)))

g.add((LA1["red_duct_heated_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["red_duct_heated_outlet_point"], RDFS.comment, Literal("Outlet point of the heated red duct", datatype=XSD.string)))

g.add((LA1["red_duct_junction"], RDF.type, S223.Junction))
g.add((LA1["red_duct_junction"], RDFS.comment, Literal("Inlet junction of the red duct", datatype=XSD.string)))

g.add((LA1["red_duct_junction_vvx_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["red_duct_junction_vvx_inlet_point"], RDFS.comment, Literal("Inlet point of the red duct from vvx", datatype=XSD.string)))

g.add((LA1["red_duct_junction_damper_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["red_duct_junction_damper_inlet_point"], RDFS.comment, Literal("Inlet point of the red duct from ST2:1 damper", datatype=XSD.string)))

g.add((LA1["red_duct_junction_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["red_duct_junction_outlet_point"], RDFS.comment, Literal("Outlet point of the red duct", datatype=XSD.string)))

g.add((LA1["GT42_temperature_sensor"], RDF.type, S223.TemperatureSensor))
g.add((LA1["GT42_temperature_sensor"], RDFS.comment, Literal("GT42 temperature sensor, measures the temperature of the inlet air", datatype=XSD.string)))
g.add((LA1["GT42_temperature_sensor"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_AI04.txt", datatype=XSD.string)))

g.add((LA1["GP11_pressure_sensor"], RDF.type, BRICK.Pressure_Sensor))
g.add((LA1["GP11_pressure_sensor"], RDFS.comment, Literal("GP11 pressure sensor, measures the pressure of the outlet air", datatype=XSD.string)))
g.add((LA1["GP11_pressure_sensor"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_UI01.txt", datatype=XSD.string)))

g.add((LA1["GT11_temperature_sensor"], RDF.type, S223.TemperatureSensor))
g.add((LA1["GT11_temperature_sensor"], RDFS.comment, Literal("GT11 temperature sensor, measures the temperature of the inlet air", datatype=XSD.string)))
g.add((LA1["GT11_temperature_sensor"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_AI01.txt", datatype=XSD.string)))

g.add((LA1["GX71_smoke_detector"], RDF.type, BRICK.Smoke_Detector))
g.add((LA1["GX71_smoke_detector"], RDFS.comment, Literal("GX71 smoke detector, measures the smoke of the outlet air", datatype=XSD.string)))

g.add((LA1["heating_battery"], RDF.type, BRICK.Heat_Exchanger))
g.add((LA1["heating_battery"], RDFS.comment, Literal("Värmebatteriet, heat exchanger in la1", datatype=XSD.string)))

g.add((LA1["heating_battery_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["heating_battery_inlet_point"], RDFS.comment, Literal("Inlet point of the heat exchanger", datatype=XSD.string)))

g.add((LA1["heating_battery_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["heating_battery_outlet_point"], RDFS.comment, Literal("Outlet point of the heat exchanger", datatype=XSD.string)))

g.add((LA1["PV01_hot_water_pump"], RDF.type, BRICK.Hot_Water_Pump))
g.add((LA1["PV01_hot_water_pump"], RDFS.comment, Literal("PV01, hot water circulationpump in la1", datatype=XSD.string)))

g.add((LA1["PV01_hot_water_pump_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["PV01_hot_water_pump_outlet_point"], RDFS.comment, Literal("Outlet point of the hot water pump", datatype=XSD.string)))

g.add((LA1["SV1_three_way_hot_water_valve"], RDF.type, BRICK.Hot_Water_Valve))
g.add((LA1["SV1_three_way_hot_water_valve"], RDFS.comment, Literal("SV1, three-way hot water valve in la1", datatype=XSD.string)))

g.add((LA1["SV1_three_way_hot_water_valve_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["SV1_three_way_hot_water_valve_outlet_point"], RDFS.comment, Literal("Outlet point of the three-way hot water valve", datatype=XSD.string)))

g.add((LA1["SV1_three_way_hot_water_valve_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["SV1_three_way_hot_water_valve_inlet_point"], RDFS.comment, Literal("Inlet point of the three-way hot water valve", datatype=XSD.string)))

g.add((LA1["DHC"], RDF.type, S223.System))
g.add((LA1["DHC"], RDFS.comment, Literal("DHC, district heating system", datatype=XSD.string)))

g.add((LA1["apartments"], RDF.type, REC.Apartment))
g.add((LA1["apartments"], RDFS.comment, Literal("Apartments in la1", datatype=XSD.string)))

"""
1.3.2 Make the connections in the red part
"""
g.add((LA1["VVX"], S223.cnx, LA1["red_duct_junction_vvx_inlet_point"]))
g.add((LA1["ST2:1_airdamper"], S223.cnx, LA1["red_duct_junction_damper_inlet_point"]))
g.add((LA1["red_duct_junction_vvx_inlet_point"], S223.cnx, LA1["red_duct_junction"]))
g.add((LA1["red_duct_junction_damper_inlet_point"], S223.cnx, LA1["red_duct_junction"]))
g.add((LA1["red_duct_junction"], S223.cnx, LA1["red_duct_junction_outlet_point"]))
g.add((LA1["red_duct_junction_outlet_point"], S223.cnx, LA1["red_duct"]))

g.add((LA1["red_duct"], S223.cnx, LA1["GT42_temperature_sensor"]))
g.add((LA1["red_duct"], S223.cnx, LA1["GP11_pressure_sensor"]))
g.add((LA1["red_duct"], S223.cnx, LA1["heating_battery_inlet_point"]))

g.add((LA1["heating_battery_inlet_point"], S223.cnx, LA1["heating_battery"]))
g.add((LA1["heating_battery"], S223.cnx, LA1["PV01_hot_water_pump_outlet_point"]))
g.add((LA1["PV01_hot_water_pump_outlet_point"], S223.cnx, LA1["PV01_hot_water_pump"]))
g.add((LA1["PV01_hot_water_pump"], S223.cnx, LA1["SV1_three_way_hot_water_valve_outlet_point"]))
g.add((LA1["SV1_three_way_hot_water_valve_outlet_point"], S223.cnx, LA1["SV1_three_way_hot_water_valve"]))
g.add((LA1["SV1_three_way_hot_water_valve"], S223.cnx, LA1["SV1_three_way_hot_water_valve_inlet_point"]))
g.add((LA1["SV1_three_way_hot_water_valve_inlet_point"], S223.cnx, LA1["DHC"]))

g.add((LA1["heating_battery"], S223.cnx, LA1["heating_battery_outlet_point"]))
g.add((LA1["heating_battery_outlet_point"], S223.cnx, LA1["red_duct_heated"]))
g.add((LA1["red_duct_heated"], S223.cnx, LA1["GT11_temperature_sensor"]))
g.add((LA1["red_duct_heated"], S223.cnx, LA1["GX71_smoke_detector"]))
g.add((LA1["red_duct_heated"], S223.cnx, LA1["red_duct_heated_outlet_point"]))
g.add((LA1["red_duct_heated_outlet_point"], S223.cnx, LA1["apartments"]))

"""
1.4.1 Yellow part declaration
"""
g.add((LA1["yellow_duct"], RDF.type, S223.Duct))
g.add((LA1["yellow_duct"], RDFS.comment, Literal("Yellow duct, exhaust air duct", datatype=XSD.string)))

g.add((LA1["yellow_duct_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["yellow_duct_inlet_point"], RDFS.comment, Literal("Yellow duct inlet from apartments", datatype=XSD.string)))

g.add((LA1["GX72_smoke_detector"], RDF.type, BRICK.Smoke_Detector))
g.add((LA1["GX72_smoke_detector"], RDFS.comment, Literal("GX72 smoke detector, measures the smoke of the exhaust air", datatype=XSD.string)))

g.add((LA1["GP12_pressure_sensor"], RDF.type, BRICK.Pressure_Sensor))
g.add((LA1["GP12_pressure_sensor"], RDFS.comment, Literal("GP12 pressure sensor, measures the pressure of the exhaust air", datatype=XSD.string)))
g.add((LA1["GP12_pressure_sensor"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_UI02.txt", datatype=XSD.string)))

g.add((LA1["GT43_temperature_sensor"], RDF.type, S223.TemperatureSensor))
g.add((LA1["GT43_temperature_sensor"], RDFS.comment, Literal("GT43 temperature sensor, measures the temperature of the exhaust air", datatype=XSD.string)))
g.add((LA1["GT43_temperature_sensor"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_UI03.txt", datatype=XSD.string)))

g.add((LA1["filter_exhaust_air"], RDF.type, BRICK.Return_Air_Filter))
g.add((LA1["filter_exhaust_air"], RDFS.comment, Literal("Filter of the exhaust air", datatype=XSD.string)))

g.add((LA1["filter_exhaust_air_inlet_point"], RDF.type, S223.InletConnectionPoint))
g.add((LA1["filter_exhaust_air_inlet_point"], RDFS.comment, Literal("Inlet point of the filter of the exhaust air", datatype=XSD.string)))

g.add((LA1["filter_exhaust_air_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["filter_exhaust_air_outlet_point"], RDFS.comment, Literal("Outlet point of the filter of the exhaust air", datatype=XSD.string)))

g.add((LA1["FF_fan"], RDF.type, BRICK.Return_Fan))
g.add((LA1["FF_fan"], RDFS.comment, Literal("FF fan, return fan", datatype=XSD.string)))

g.add((LA1["FO_return_fan_efficiency"], RDF.type, S223.Property))
g.add((LA1["FO_return_fan_efficiency"], RDFS.comment, Literal("Return fan efficiency FO", datatype=XSD.string)))
g.add((LA1["FO_return_fan_efficiency"], S223.ExternalReference, Literal("/home/zengp/Code/rio10/sensor_data_la1/FAS5706002_DUC201_AU02.txt", datatype=XSD.string)))

g.add((LA1["FF_fan_outlet_point"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["FF_fan_outlet_point"], RDFS.comment, Literal("Outlet point of the FF fan", datatype=XSD.string)))

g.add((LA1["yellow_duct_outlet_damper"], RDF.type, BRICK.OutletConnectionPoint))
g.add((LA1["yellow_duct_outlet_damper"], RDFS.comment, Literal("Yellow duct outlet to damper", datatype=XSD.string)))

g.add((LA1["yellow_duct_outlet_vvx"], RDF.type, S223.OutletConnectionPoint))
g.add((LA1["yellow_duct_outlet_vvx"], RDFS.comment, Literal("Yellow duct outlet to vvx", datatype=XSD.string)))

g.add((LA1["yellow_duct_junction"], RDF.type, S223.Junction))
g.add((LA1["yellow_duct_junction"], RDFS.comment, Literal("Yellow duct junction", datatype=XSD.string)))

"""
1.4.2 Make the connections in the yellow part
"""
g.add((LA1["apartments"], S223.cnx, LA1["yellow_duct_inlet_point"]))
g.add((LA1["yellow_duct_inlet_point"], S223.cnx, LA1["yellow_duct"]))

g.add((LA1["yellow_duct"], S223.cnx, LA1["GX72_smoke_detector"]))
g.add((LA1["yellow_duct"], S223.cnx, LA1["GP12_pressure_sensor"]))
g.add((LA1["yellow_duct"], S223.cnx, LA1["GT43_temperature_sensor"]))

g.add((LA1["yellow_duct"], S223.cnx, LA1["filter_exhaust_air_inlet_point"]))
g.add((LA1["filter_exhaust_air_inlet_point"], S223.cnx, LA1["filter_exhaust_air"]))
g.add((LA1["filter_exhaust_air"], S223.cnx, LA1["filter_exhaust_air_outlet_point"]))
g.add((LA1["filter_exhaust_air_outlet_point"], S223.cnx, LA1["FF_fan"]))
g.add((LA1["FF_fan"], S223.cnx, LA1["FO_return_fan_efficiency"]))
g.add((LA1["FF_fan"], S223.cnx, LA1["FF_fan_outlet_point"]))

g.add((LA1["FF_fan_outlet_point"], S223.cnx, LA1["yellow_duct_junction"]))
g.add((LA1["yellow_duct_junction"], S223.cnx, LA1["yellow_duct_outlet_damper"]))
g.add((LA1["yellow_duct_junction"], S223.cnx, LA1["yellow_duct_outlet_vvx"]))

g.add((LA1["yellow_duct_outlet_damper"], S223.cnx, LA1["ST2:2_airdamper"]))
g.add((LA1["yellow_duct_outlet_vvx"], S223.cnx, LA1["VVX"]))

"""
3. Build the graph
"""
with open("rio10_la1.ttl", "w") as f:
    f.write(g.serialize(format="ttl"))


# Test some queries

##################################
# Find ducts connected to VVX
# query = """
# SELECT ?duct WHERE {
#     ?duct rdf:type s223:Duct .
#     ?duct s223:cnx+ la1:VVX .
# }
# """

# # Execute the query
# ducts = g.query(query)

# # Print the results
# for row in ducts:
#     print(row)

##################################


##############################################
# Find all sensors connected to the Yellow duct
# query = """
# SELECT ?sensor WHERE {
#     la1:yellow_duct s223:cnx ?sensor .
#     ?sensor rdf:type ?sensorType .
#     FILTER regex(str(?sensorType), "(Sensor|Detector)$", "i")
# }
# """
# # Execute the query
# sensors = g.query(query)

# # Print the results
# for row in sensors:
#     print(f"Sensor: {row.sensor}")
################################################


################################################
# # Find GT42
# query1 = """
# SELECT ?sensor WHERE {
#     la1:red_duct s223:cnx ?sensor .
#     ?sensor rdf:type s223:TemperatureSensor .
# }
# """
# # Execute the first query
# sensors1 = g.query(query1)

# # Print the results
# print("Temperature Sensors Directly Connected to Red Duct:")
# for row in sensors1:
#     print(f"Sensor: {row.sensor}")
################################################


###################################
# Find GT11
# # Define the query with prefixes
# query = """
# SELECT ?sensor WHERE {
#     la1:red_duct_heated s223:cnx ?sensor .
#     ?sensor rdf:type s223:TemperatureSensor .
# }
# """

# # Execute the query
# sensors = g.query(query)

# # Print the results
# print("GT11 Temperature Sensor Connected to Red Duct Heated:")
# for row in sensors:
#     print(f"Sensor: {row.sensor}")
#####################################


#####################################
# Find the GT11 time series data path
query = """
SELECT ?sensor ?externalRef WHERE {
    la1:red_duct_heated s223:cnx ?sensor .
    ?sensor rdf:type s223:TemperatureSensor .
    ?sensor s223:ExternalReference ?externalRef .
}
"""
# Execute the query
sensors = g.query(query)

# Print the results
print("GT11 Temperature Sensor Connected to Red Duct Heated with External Reference:")
for row in sensors:
    print(f"Sensor: {row.sensor}")
    print(f"External Reference: {row.externalRef}")
#####################################