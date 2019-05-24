#!/bin/python
# send sms - send SMS via Nexmo API, prompt for username and password
# ref: https://developer.nexmo.com/messaging/sms/code-snippets/send-an-sms
# ref: https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/
# ref: use input for username: https://stackoverflow.com/questions/19661956/python-prompt-for-user-with-echo-and-password-without-echo

import getpass, nexmo
user  = input('enter your username: ')
password = getpass.getpass('enter your password: ')
phoneNumber = input("enter your phone number: ")
print(phoneNumber, password, user)


client = nexmo.Client(key=user, secret=password)

responseData = client.send_message(
    {
        "from": "Acme Inc",
        "to": phoneNumber,
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

