#!/bin/python
# number insight standard (ni-standard.py) ads more insight to HLR
# https://developer.nexmo.com/number-insight/code-snippets/number-insight-standard

import getpass, nexmo
from pprint import pprint

user  = input('enter your username: ')
password = getpass.getpass('enter your password: ')
phoneNumber = input("enter your phone number: ")
# print(phoneNumber, password, user)


client = nexmo.Client(key=user, secret=password)

insight_json = client.get_standard_number_insight(number=phoneNumber)
pprint(insight_json)

