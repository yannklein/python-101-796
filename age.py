# ask the user about her/his age and display the age next year

# defining the variable age and assigning the user input to it
age = int(input('What\'s you age? '))

# re-assignment
# age = age + 1
age += 1

# concatenation
print("Your age will be " + str(age) + " next year.")

# interpolation
print(f'Your age will be {age} next year.')
