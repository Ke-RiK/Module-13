# Kirill Kaminskyi M13P2.py 11/16/2026

#dictionary
students = {
    "Smith": [85, 90, 73],
    "Brown": [92, 65, 88],
    "Johnson": [78, 89, 70],
    "Kam": [95, 90, 98],
    "Davis": [88, 81, 79]
}

grade_averages = []

#function
def calculate_averages():
    for name, grades in students.items():
        total = 0
        for grade in grades:
            total += grade
        average = total / 3
        grade_averages.append([name, average])

calculate_averages()

#output
print(f"{'Name':<20} {'Average':<20}")
for name, average in grade_averages:
    print(f"{name:<20} {average:<20,.2f}")

#function
def calculate_class_averages():
    exam1_total = 0
    exam2_total = 0
    exam3_total = 0
    for name, grades in students.items():
        exam1_total += grades[0]
        exam2_total += grades[1]
        exam3_total += grades[2]
    exam1_average = exam1_total / len(students)
    exam2_average = exam2_total / len(students)
    exam3_average = exam3_total / len(students)

    class_averages = [exam1_average, exam2_average, exam3_average]
    return class_averages

class_averages = calculate_class_averages()
exam1 = class_averages[0]
exam2 = class_averages[1]
exam3 = class_averages[2]

#final outputs
print()
print("Class averages:")
print(f"Exam 1: {exam1:.2f}")
print(f"Exam 2: {exam2:.2f}")
print(f"Exam 3: {exam3:.2f}")
