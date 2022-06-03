import time
print("Welcome to the Quiz-O-Computer")

#If the user wants to play the game
playing = (input("Do u wish to play the Quiz-O-Computer([F]/[T]). \n >>")).lower()
if playing == "t":
    print("Welcome to Quiz-O-Computer, u shall now get your questions")
    time.sleep(0.3)
    print(".... ... ....")
if playing != "t":
    print("As u say, u shall now exit the Quiz-O-Computer")
    time.sleep(0.5)
    print(".... .... .... ....")
    time.sleep(2)
    print("Exiting")
    quit()

score = 0

Q1 = (input("The first Question - what is the name of the latest default linux filesystem? \n >>")).lower()
if Q1 == "ext4":
    score = score + 1
    print("Bravo!! That answer is absolutely correct!! your score is now up to " + (str(score)))
else:
    print("Oh oh, that answer is incorrect, your score is now " + (str(score)))

Q2 = (input("The second question - What Free(non-paid) linux distribution is sponsored by Red Hat Enterprise")).lower
if Q2 == "fedora":
    score = score + 1
    print("Excellent!! That's correct!! now your score is  \n >>" + (str(score)))
else:
    print(f"Sorry!! The answer u gave isn't correct, your score is now {score}. Better luck Next Time!!")

#u can continue adding further more questions!!!
