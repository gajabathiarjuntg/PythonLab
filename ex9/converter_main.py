import converter

# Perform Kilometers to Meters conversion
km_val = float(input("Enter distance in kilometers (km): "))
meters_from_km = converter.km_to_meters(km_val)
print(km_val, "km =", meters_from_km, "meters")

# Perform Centimeters to Meters conversion
cm_val = float(input("\nEnter length in centimeters (cm): "))
meters_from_cm = converter.cm_to_meters(cm_val)
print(cm_val, "cm =", meters_from_cm, "meters")


