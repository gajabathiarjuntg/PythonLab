print("NEGATIVE RADIUS EXCEPTION")
try:
    r = int(input("Enter a Radius : "))

    if r < 0:
        raise ValueError("Radius cannot be negative")

    area = r * r * 3.14
    print("Area of the circle:", area)

except ValueError as e:
    print("Error",e)