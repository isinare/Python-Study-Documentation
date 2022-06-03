import random
randint = random.randint(0,9)
print(randint)
i = 3


while i > 0:
    intguess = input(f"Guess the digit between 0 and 9!! u have total {i} tries \n>>")
    intguesscheck = intguess.isdigit()
    if intguesscheck == False:
        print(f"please enter an integer, u have {i} tries remaining \n>>")
    if intguesscheck == True:
        guess = int(intguess)
        random = int(randint)
        i = i - 1
        if guess == random:
            print("That\'s absolutely correct!!")
            print("Congratulations!!!")
            exit()
        else:
            print(f"That\'s wrong have another try, u have {i} tries remaining \n>>")
if i == 0:
    print("Oh Oh, u couldnt guess the number, better luck next time!!")
