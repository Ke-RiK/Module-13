# Kirill Kaminskyi M13P1.py 11/16/2026

total = 0

#dictionary
students = {
    "Smith": 85,
    "Brown": 92,
    "Johnson": 78,
    "Kam": 95,
    "Davis": 88
}

print(f"{"Name:":<20} {"score:":<20}")

for name, grade in students.items():
    print(f"{name:<20} {grade:<20,.2f}")
    total += grade

average = total /len(students)
print()
print (f"Average score: {average:<20,.2f}")
