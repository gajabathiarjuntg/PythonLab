temperatures = {
    'Chennai': 38,
    'Bangalore': 30,
    'Madurai': 40,
    'Coimbatore': 32
}

hottest_city = max(temperatures, key=temperatures.get)

print(f"The hottest city today is {hottest_city} at {temperatures[hottest_city]}°C.")
