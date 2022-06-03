# #Type Conversion
# name = 'Ishan Sinare'
# age = 14
# relationship_status = 'single'
# relationship_status = 'it\'s complicated'

#ageComputer
current_year = (int(input('Which year is it?')))
birth_year = (int(input('what year were u born?')))

# int_birth = int(birth_year)
# int_current = int(current_year)

# print(type(int_birth))
# print(type(int_current))

age = current_year-birth_year
# str_age = str(age)

print(f'your age is {age}')