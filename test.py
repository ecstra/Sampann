from google.oauth2 import id_token
from google.auth.transport import requests

def validate_google_token(token, client_id):
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        return userid, idinfo
    except ValueError:
        # Invalid token
        return None, None

# This is your Google client ID
CLIENT_ID = "728781754591-pqdffgcuql5q0o4d1270frs8cu80sfov.apps.googleusercontent.com"

# This is your received Google ID token
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgzOGMwNmM2MjA0NmMyZDk0OGFmZmUxMzdkZDUzMTAxMjlmNGQ1ZDEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3Mjg3ODE3NTQ1OTEtbjlsM3BlZXI2MGprdmxqYnRsazZkMjYwN2JwMTVidnIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI3Mjg3ODE3NTQ1OTEtcHFkZmZnY3VxbDVxMG80ZDEyNzBmcnM4Y3U4MHNmb3YuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTM4MDcyMzc5NzkwNzI1NDYwODEiLCJlbWFpbCI6Imthc2hpZm5lemFtMTIzQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiTWQgS2FzaGlmIE5lemFtIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lQZ0UyWVJLQUJQVDFtczFuY192TVQzeUFoV1duQWpKdHFmMFhoR281Nj1zOTYtYyIsImdpdmVuX25hbWUiOiJNZCBLYXNoaWYgTmV6YW0iLCJsb2NhbGUiOiJlbi1HQiIsImlhdCI6MTY5NDUwNTcxOCwiZXhwIjoxNjk0NTA5MzE4fQ.JKV-cXsMJU9AsNuZZaIQtGUAiS2QnHJoSgoIsDvb8KvNQZw4Ewe9yWv8SV55Tj5qRYyv78kar0FtTEPHqM5_GV9nxeyvjh50QSiT1e6kagOap7c11Q_A360OCoINDWg60Iu_xoPH6WoYTO5UNVmDgcjvknSDr3VWg9ug4_WbYAL7eVVN9MVNKHrZeWQ7v9jCaZYyNW1WY9b4YSI_6DwHxzo7QF906Zh7RFhAfQ-neRd-67JZ"

user_id, user_info = validate_google_token(token, CLIENT_ID)
if user_id:
    print(f"Token is valid for user ID: {user_id}")
    print(f"User info: {user_info}")
else:
    print("Invalid token.")
