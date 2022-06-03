# #passCheck
username = input("what is your username")
password = input("what is your password")
pass_characters = '*' * len(password)
pass_str = str(len(pass_characters))

print(f'Welcome Back, {username}, please enter your password, your password is {pass_characters}, is {pass_str} characters long')