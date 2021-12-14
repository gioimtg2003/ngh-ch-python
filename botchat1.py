import getpass
import fbchat
session = fbchat.Session.login("kedasil688@elastit.com", getpass.getpass())
user = fbchat.User(session=session, id=session.user_id)
user.send_text("Test message!")