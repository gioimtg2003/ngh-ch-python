import fbchat
from fbchat import Client
from getpass import getpass

from fbchat import client
email = "kedasil688@elastit.com"
client = fbchat.Client(email, getpass())
no_of_friend = int(input("Number of friends: "))
for i in range(no_of_friend):
    name = str(input("Name: "))
    friends = client.searchForMessages(name)
    friend = friends[0]
    msg = str(input("Messenger: "))
    sent = client.send(fbchat.models.Message(msg),friend.uid)
    if sent:
        print (" gửi thành công ")
