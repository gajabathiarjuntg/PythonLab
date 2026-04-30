try:
    temp = float(input("Enter temperature in Celsius: "))

    if temp < -273.15:
        raise ValueError("Temperature is below absolute minimum (-273.15°C)!")

    print("The temperature is:", temp)

except ValueError as e:
    print("Invalid Temperature:", e)
