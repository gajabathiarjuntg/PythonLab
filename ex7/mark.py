students = {'Ravi': 75, 'Priya': 95, 'Kiran': 88}

topper = max(students, key=students.get)

print(f"The class topper is {topper} with {students[topper]} marks.")