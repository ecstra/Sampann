import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize the default app
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "sampann-398206",
  "private_key_id": "e3581b62163be99faf5006cbca386c69357ec294",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC6PpU51Z4fgMYb\nzDUeYqktH7KdiX/hp2+LxbUzL1oXBGKaaI3kua5m/X8WvM4ff+skA/5LNi/HwhT7\nay0Ebo2BFN3tJG73YOlcUTXgbI8w9XrHTmKPfrv3Ew5M8b85E3dW9ppBRHvqXeH6\nBXu3IluqILm3y1n0rlWSfYPWZyEt519JdF3CmB2uLazFFAhN7cEteXKXWsKKa/OC\n6JIFO60+CdSQEyc9mR71Oo0S+Hz3czIW4krK817Njw2GzH08Iua9lXZvc53u0YGa\nEDGIyj/xNtmc6Vlj1FK8MiTYJHeEb2J5eis9I0bs0xyOZqbVGys98DAivqd01IRf\nTETZpq9vAgMBAAECggEABJbsOHuiJOaYezDiEjieMKV6UlWEGDx3DDu4BmXhU3Xh\nNCrlbECDIriWfCn07mPJmJ6ckp/oN4T53WQ7vMM4q3inK2PddC0oMwUxTbF/Kday\nytyMozqdSS5oCM9gRfjL1RHIpVkZsKHVosKl1NJ87clWqkfRlK0DINQE/rCV6bqi\nHD3DKvuxBRMgWO9C1ON0v5RH+N5KQu951shtE+Gkn6HulLw/lgeBaE+xLCQ9/rDc\noJ/IklkhyRJYqSL6nH9NNJUtVWGgtH8gTM1tt4kZuYjKT4kBM/eehTZ+Zyyt32+d\ndXhjLKlKAUKKD1EJY0zcwELOTEzj9gyVm/4mZhwksQKBgQDr5yJJTX5EhpG1hZJv\nwVxpxKIOtyymTRoIOPtkkkoDfxqpzc0gEpI217o3UIe30Fz8uA9HLtq7Prds+Wrt\nMr8raUXPdH3wMIYEh8xXfjWPwJblRPeMH6GGM0U4mrZcE02Qvxi/YeSfGGej0oHy\n0ASYJ0lDCdtk12KRH2w66dCL5wKBgQDKHG+oO5Ur76FyZ1r0nzoOzff05GseGx9j\nj1BFVfrvcsJup9Qp/0M7NKDphVjQGctW5fi1mZtkR1TlRVB7q+FSaVU2qfcXc9Hw\nzD6yayUNnM7mLygOGmEB+w2jN7XoEK2lLA81enpPSr5S3zoH0gHNFcVuROy6xzTR\nZQFsVTMPOQKBgHjHZASHyognJd78Plc9dqUoaZiDLDcQ7q0bD4sUYxSbNPmPRuCO\n4ZF2rf64GmSAJ7u0OQ5G7PJFUABZSueavcnqIjXu/LPHBDa5mGOLWLz668cCooN5\nhmeBRIWQoKFPuLzNOkxyQG08P4PeuW2qF1AXfSj3mP5uUCbhIbagE4gtAoGACmoW\nstOHJ0Fsz0lWHX7K7hJc8YiHoICDSI0M9NWuXYJLVIpfW16k5zsaA450ehyqJqso\n+qqUoEEwtbOxpv2/WZDF7FArxFCag87yeB0fRqlK2/+YD8n6L7DxDfUD8ZZSbE1t\n5zKNdOKEFh8cjWSb5SZ3CuyQSjuTlCqhPSTSwbkCgYBTCWJI36eGq2V2KLT8l0d3\ndq0yVhhInufASUojnVUbKOXso8VrpaZHEEnoWbRC3KUqKkUt5Apffnsk0gmWsSGD\n4l8Tn+qLhoAy7nG64ssFW/xhSPO+kCNAk/WSoB+mUVJvbSmEhiF457n8EJJUt1K9\nHuRJw2TlPzj8cfFlwsuaHQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-f4u9c@sampann-398206.iam.gserviceaccount.com",
  "client_id": "113408687994834473431",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-f4u9c%40sampann-398206.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
)
default_app = firebase_admin.initialize_app(cred)

# Fetch the user by UID
uid = 'ZZc3eyhmKNQlMjliMcSgYcNLW612'
user = auth.get_user(uid)

# Print all attributes
print(user.__dict__)

print("Username: ", user.display_name)
print("isEmailVerified: ", user.email_verified)

print("Phone Number: ", user.phone_number)
print('Email:', user.email)