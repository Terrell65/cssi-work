# first step
# firstname = raw_input("firstname?")
# lastname = raw_input("lastname?")
# print(firstname + " briscoe " + lastname)
#
# agestring = raw_input("how old are?")
# age = int(agestring)
# print(type(age))
# if age < 18:
#     print("you cant vote")
# else:
#     print("you can vote")
# task1
# num1string = raw_input ("whats the first number")
# num1 = int(num1string)
# num2string = raw_input ("whats the second number")
# num2 = int(num2string)
#
# if num1 == num2:
#     print("equal number")
# else:
#     print("unequal number")
# task2
# num1string = raw_input(" enter 1st num: ")
# num1 = int(num1string)
# num2string = raw_input("enter 2nd num: ")
# num2 = int(num2string)
# num3string = raw_input("enter 3rd num: ")
# num3 = int(num3string)
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)

userstring1 = raw_input("rock, paper, scissor: ")

userstring2 = raw_input("rock, paper, scissor: ")

# if userstring1 == "paper" and userstring2 == "rock" or userstring1 == "rock" and userstring2 == "paper":
#     print("paper wins")
if userstring1 == "paper":
    if userstring2 == "rock":
      print("paper wins")
elif userstring2 == "paper":
    print("tie")
else:
    print("scissors win")
elif userstring1 == ""
