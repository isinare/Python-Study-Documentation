# import time
# startTime = time.time()

# i = 0
# while i<1000000:
#     i += 1
#     if i == 1:
#         print("Welcome To the Game!! You are level 1 now")
#     if i ==100:
#         print("U have hit level 100!! CONGRATULATIONS")
#     if i ==300:
#         print("U have hit level 300!! U have unlocked the Dusty Caverns!! Access it from the hub")
#     if i ==500:
#         print("U HAVE NEARLY COMPLETED THE GAME!!! All that remains is beating The Mad titan Thanos Now! DO IT!!")
#     if i ==100000:
#         print("OMG U HAVE GOTTEN TO THE SECRET LEVEL!! Try solving it maybe")


# executionTime = (time.time() - startTime)
# print('Execution time in seconds: ' + str(executionTime))

# while True:
#     response = input("Kindly Tell us If u are an adult (Yes/No)")
#     if response == ("No"):
#         print("srry but u are currently ineligible to play fortnite.")
#     if response == ("Yes"):
#         print("Excellent!! Create an Account on the Epic Games Store now!!!")
#     break

my_list = [1,2,3,4,5,6,7]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1 
    continue

my_list = [1,2,3,4,5,6,7]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1 
    pass #Nothing happens... it passes a line
