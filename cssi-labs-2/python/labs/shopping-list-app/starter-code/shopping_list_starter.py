#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []
def add():
    item1 = raw_input('what do you want: ')
    shopping_list.append(item1)
    # print(shopping_list)
def show():
    print(shopping_list)
def remove():
    input =  raw_input(" what do you want to remove")
    shopping_list.remove(input)
def item2():
    item2 = raw_input("what do you want to check for")
    if item2 in shopping_list:
        print('true')



while choice.lower() != "e":
    print("\nPlease choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = raw_input("Enter your choice [a|b|c|d|e]:")
    if choice == "a":
        add()
    if choice == 'd':
        show()
    if choice == 'b':
        remove()
    if choice == 'c':
        item2()




    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
