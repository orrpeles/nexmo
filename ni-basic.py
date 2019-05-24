#!/bin/python
# number insight basic (ni-basic.py) features the basics of HLR request
# ref: https://developer.nexmo.com/number-insight/code-snippets/number-insight-basic

import getpass, nexmo
from pprint import pprint

user  = input('enter your username: ')
password = getpass.getpass('enter your password: ')
phoneNumber = input("enter your phone number: ")
# print(phoneNumber, password, user)


client = nexmo.Client(key=user, secret=password)

insight_json = client.get_basic_number_insight(number=phoneNumber)
pprint(insight_json)

