#              0       1      2        3 
students = ['norty', 'ben', 'lam', 'stephen']

# print(len(students))
# print('lee' in students)
# print('norty' in students)
# print(students[1])
# print(students[1:3]) # every element from index 1 to 3 excluded
# print(students[:3]) # every element from start to 3 excluded
# print(students[-2]) # give the secnd before last element
# print(students[2:]) # every element from index 2 to the end

# CRUD operations

# Create
students.append('tony')
students.insert(1, 'mizuki')
print(students)

# Read
print(students[1])

# Update
students[1] = 'Super Mizuki'
print(students)

# Delete
del students[1]
print(students)

# for loop
# for student in students:
#     print(f'{student.capitalize()} is amazing!')

[ print(f'{student.capitalize()} is amazing!') for student in students ]
capitalizedStudents = [ student.capitalize() for student in students ]
print(capitalizedStudents)

print(list(enumerate(students)))

for index, student in enumerate(students):
    print(f'{index + 1} - {student}')