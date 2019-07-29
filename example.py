# state1 = " new york"
# abbr = "ny"
# state2 = "california"
# abbr2 = "ca"
# print(abbr2 + "is short for " + state2)
# states  = ["ca = california", "ny = new york"]
# for state in states:
#     print(state)
#
# state_abbr = ['ca','ny']
# states = ['CALI', 'NEW YORK']
# states = {
#     'ny': 'new york',
#     'mi': 'michigan',
#     'fl': 'florida'
# }
# print(states['mi'])
#
# phonebook = {
#     'kale': '3132465789',
#     'bleek': '3132838520',
#     'bray': '3139912760'
# }
# print(phonebook['bleek'])
# for name in phonebook:
#     print('name is ' + name)
#     print('number is ' + phonebook[name])
# pet = {
#     'name': 'skeemer',
#     'animal': 'dog',
#     'breed': 'beagal',
#     'age': 17
# }
# print(pet['name'] + 'left the family')
# pet['name'] = 'simba'
# print('and shall be known as ' + pet['name'])
#
#
# pet.pop('age')
# print(pet)

# rells_life = {
# 'name': 'robert',
# 'age': 17,
# 'movies': {
#     'name': 'avenger end game',
#     'rating': 'PG-13',
#     }
# }
# for key in rells_life:
#     print("key is " + key)
#     print("value is " + str(rells_life[key]))

class Pet(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print ('rudd tuff ruff')

my_pet = Pet('blu',14)
my_pet.bark()
# print('my new pet is ' + my_pet.name +' and he is ' + str(my_pet.age))
