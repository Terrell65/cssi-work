# name = raw_input("give name")
# name = raw_input("give name")
# while name != "stop":
#     print("still in loop")
#     name = raw_input("give name")

# import random
# randnum = random.randint(1,10)
# numstring = raw_input("guess");
# num = int(numstring)
#
# while num != randnum:
#     numstring = raw_input("guess");
#     num = int(numstring)
#
# print("good guess")
# import random
# answer = random.randint(1,10)
# while True:
#     guessString = raw_input("give a guess:")
#     guess = int(guessString)
#     if guess == answer:
#         print("you got it!")
#         break
#     elif guess > answer:
#         print("too high try again")
#     else:
#         print("too low try again")
import random

def drawcard():
    randnum = random.randint(2,11)
    print("you draw a " + str(randnum))
    return randnum
cardcount = 0

while True:
    guessString = raw_input("continue to draw:")
    if guessString == "no":
        break

    tm = drawcard()
    cardcount = tm + cardcount
    print("your total is" + str(cardcount))
    if cardcount == 21:
        print("you won!")
        break
    if cardcount > 21:
        print("you lose")
