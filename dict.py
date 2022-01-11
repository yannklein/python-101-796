student = {
    'name': 'Paul',
    'age': 21,
}

# print(len(student))
# print('name' in student)
# print('Paul' in student)

# print(student.values())
# print(student.keys())
# print(student.items())

# print('Paul' in student.values())

# C
student['hobby'] = 'Basketball'
print(student)

# R
print(student['name'])
# print(student['job']) #will raise an Error!!
print(student.get('job', 'not found'))
print(student.get('job'))
print(student.get('name'))

# U
student['hobby'] = 'Drinking'
print(student)

# D
del student['hobby'] 
print(student)

for key, value in student.items():
    print(f'{key} - {value}')