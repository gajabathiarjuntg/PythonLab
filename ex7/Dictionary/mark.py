marks = {}
n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    score = float(input(f"Enter marks for {name}: "))
    marks[name] = score

average = sum(marks.values()) / len(marks)
print("Average marks:", average)
