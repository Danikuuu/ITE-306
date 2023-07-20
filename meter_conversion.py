print("METER CONVERSION")

meter = float(input("Enter the meter to convert : "))

ml = meter * 1000
cm = meter * 100
dm = meter * 10
km = meter / 1000
inch = meter * 39.37
foot = meter * 3.28
mile = meter / 1609.344

print(meter, "meter to Millimeter", ml)
print(meter, "meter to Centimeter", cm)
print(meter, "meter to Decimeter", dm)
print(meter, "meter to Kilometer", km)
print(meter, "meter to Inch", inch)
print(meter, "meter to Foot", foot)
print(meter, "meter to Mile", mile)