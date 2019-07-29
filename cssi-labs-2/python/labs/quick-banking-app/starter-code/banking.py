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

# Replace "pass" with your code



class BankAccount(object):
    def __init__(self,label,balance,):
        self.label = label
        self.balance = balance
    # def transfer(self,dest_account,amount):
    # def tansaction(self,deposit,withdraw):
    #     self.balance = balance
    def deposit(self,amount):
        money2 = amount + self.balance
        if money2 < 0 or amount <0:
            print('cannot put in')
        else:
            self.balance = amount + self.balance
    def withdraw(self,amount):
        money = self.balance - amount
        if money < 0 or amount<0:
            print("cannot take out ")
        else:
            self.balance = self.balance - amount








    def __str__(self):
        return 'the customer '+ self.label+ " has the amount of " + str(self.balance)


my_bank = BankAccount('terrell', 100000000)
my_bank.deposit (200000000)
kale_bank = BankAccount('kale',200000000)
kale_bank.deposit(-30000000000000)

bleek_bank = BankAccount('bleek', 20000000)
bleek_bank.withdraw(-30000000)
print(my_bank)
print(kale_bank)
print(bleek_bank)
