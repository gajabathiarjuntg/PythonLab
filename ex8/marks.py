try:
    marks = float(input("Enter student marks: "))

    if marks < 0:
        raise ValueError("Marks cannot be negative.")
    if marks > 100:
        raise ValueError("Marks cannot be greater than 100.")

    print("Marks:", marks)

except ValueError as e:
    print("Invalid Marks:", e)


