# age = 20
#
# if age > 18:
#     print('you can vote !')
#     if age > 25:
#         print('you can vote!')
#     print('you can also get a car')
# print('you can also get a credit card')
# for i in range(10):
#     print(i)
# x = 1
# while x <= 5:
# #     print(x)
# #     print('no')
class pokemon(object):
    #constuctor
    def __init__(self,name,type,sex):
        self.name = name
        self.type = type
        self.sex = 'female'
    def attack(self,move):
        print('my name is ' + self.name + 'and i chose' + move)
class pikachu(pokemon):
    def __init__(self,name,type,sex,voltage,current):
        pokemon.__init__(self,name,type,sex)
        self.voltage = voltage
        self.current = current

class charizard(pokemon):
    #constuctor
    def __init__(self,tail_size,name,type,sex):
        pokemon.__init__(self,name,type,sex)
        self.tail_size = tail_size

charizard = charizard('charry',' large', ' f ', ' flame-fly')
print(charizard.name + charizard.type + charizard.sex )

# my_pokemon = pokemon('pikachu','electric','male')
