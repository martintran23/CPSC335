# To implement Array based example - Create a list

students = ["Ava", "Ben", "Cleo", "Dev"]

# Direct indexing
first_student = students[0]
third_student = students[2]
print(first_student, third_student)

# Update an element
students[1] = "Bo"
print(students)

# Append vs Insert
students.append("Ellie")
students.insert(2, "Kai")
print(students)

# Remove from the end vs middle
last_removed = students.pop()
middle_removed = students.pop(2)
print(last_removed, middle_removed)
print(students)

# Iterate over the list
for name in students:
    print("Hi, ", name)