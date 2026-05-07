from Student.mark import calculate_total
from Student.grade import assign_grade

# Collect mock subject data
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

marks_list = [m1, m2, m3]
total_possible_marks = 300

# Compute results using package functions
grand_total = calculate_total(marks_list)
final_grade = assign_grade(grand_total, total_possible_marks)

print("\n--- Student Result Summary ---")
print("Total Marks Obtained:", grand_total, "/", total_possible_marks)
print("Final Grade Assigned:", final_grade)

