#Truthy vs Falsey

password = bool(input('All inputs must result in a true boolean.Pls enter your username'))
username = bool(input('Pls enter your password'))

print(type(password))
print(type(username))

if password and username:
    print('Your are good to go!!')
    print('Click HERE to go to the dashboard')
else:
    print('U cant access')
    print('Password or username error')