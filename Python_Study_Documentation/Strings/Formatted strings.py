# Formatted strings

#better code(python3 only)
name = "Johnathon"
age = 55
print("hi" + " " + name + ' ' + str(age))
#or
print('Hi {},pls verify your age to be correct- {}'.format('Johnathon','55'))
print(input('enter if it is correct'))
print('thank u for verification')

#secondary method(python2/3)
print ('hi {0}. Verify your age to be {1}'.format('sally','19'))

#integrate variable in the statement
print('hi {new_name}. Verify your age to be {age}'.format(new_name='Preston',age = '21'))