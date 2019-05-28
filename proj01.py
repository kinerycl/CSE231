####################################################
# Computer Project #1
#
# Algorithm
#    prompt for an integer
#    input an integer
#    convert integer convert into 5 different units
#  print different units 
####################################################

rods_str = input("Input rods: ")
rods_float = float(rods_str)
print("You input", rods_float, "rods.")

#conversions
meter_float = rods_float * 5.0292
furlong_float = rods_float / 40
mile_float = meter_float / 1609.34
feet_float = meter_float / 0.3048
mins_float = (mile_float * (60/3.1))

#rounding to 3 decimal places
meter_float = float(round(meter_float, 3))
furlong_float = float(round(furlong_float, 3))
mile_float = float(round(mile_float, 3))
feet_float = float(round(feet_float, 3))
mins_float = float(round(mins_float, 3))

#output
print("Conversions")
print("Meters:", meter_float)
print("Feet:", feet_float)
print("Miles:", mile_float)
print("Furlongs:", furlong_float)
print("Minutes to walk", rods_float, "rods:", mins_float)