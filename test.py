import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize the default app
cred = credentials.Certificate(r"C:\Users\themy\Downloads\sampann-398206-firebase-adminsdk-f4u9c-e3581b6216.json")
default_app = firebase_admin.initialize_app(cred)

# Fetch the user by UID
uid = 'ZZc3eyhmKNQlMjliMcSgYcNLW612'
user = auth.get_user(uid)
user = auth.get_user(uid)
# Access user attributes
print('UID:', user.uid)
print('Email:', user.email)