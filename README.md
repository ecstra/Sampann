

# Updated API Documentation

---

## 1. Set Context API

### API Endpoint

- **URL**: `/setContext`
- **Method**: `POST`

### Description:

This API is used to establish the initial context for the chatbot based on user responses to a quiz. It performs an analysis of the answers and stores this information for future interactions with the chatbot.

### Request Format

- **Header**:

  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Body**:

  ```json
  {
    "QandA": {
      "1": "a",
      "2": "b",
      "3": "c",
      // ... other quiz answers
    }
  }
  ```

### Response Format

- **Status Code**: `201 CREATED`
- **Body**:
  ```json
  {
    "analysis_results": {...},
    "status": 201,
    "access_token": "..."
  }
  ```

### Example Usage in Flutter

```dart
final response = await http.post(
  Uri.parse('http://backend_url/setContext'),
  body: jsonEncode({
    "QandA": {
      "1": "a",
      "2": "b",
      // ... other quiz answers
    }
  }),
  headers: {"Content-Type": "application/json"},
);
```

---

## 2. Get Bot Response API

### API Endpoint

- **URL**: `/getBotResponse`
- **Method**: `POST`

### Description:

This API facilitates the core chat functionality. It takes a user message as input and returns the chatbot’s response.

### Request Format

- **Header**:

  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Body**:

  ```json
  {
    "user_message": "Tell me about diabetes"
  }
  ```

### Response Format

- **Status Code**: `200 OK`
- **Body**:
  ```json
  {
    "response": "Here is information about diabetes...",
    "status": 200
  }
  ```

### Example Usage in Flutter

```dart
final response = await http.post(
  Uri.parse('http://backend_url/getBotResponse'),
  body: jsonEncode({"user_message": "Tell me about diabetes"}),
  headers: {"Content-Type": "application/json"},
);
```

---

## 3. Logout API

### API Endpoint

- **URL**: `/logout`
- **Method**: `GET`

### Description:

This API logs out the user and clears the session.

### Response Format

- **Status Code**: `200 OK`
- **Body**: "Logged out"

### Example Usage in Flutter

```dart
final response = await http.get(Uri.parse('http://backend_url/logout'));
```

---

## 4. Refresh Token API

### API Endpoint

- **URL**: `/refresh_token`
- **Method**: `POST`

### Description:

This API refreshes the JWT token for the user.

### Response Format

- **Status Code**: `200 OK`
- **Body**:

  ```json
  {
    "access_token": "...",
    "refresh_token": "..."
  }
  ```

### Example Usage in Flutter

```dart
// Check Usage of the App section
```

---

## 5. Android Login API

### API Endpoint

- **URL**: `/android_login`
- **Method**: `POST`

### Description:

This API enables login functionality specifically for Android applications.

### Request Format

- **Header**:

  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Body**:

  ```json
  {
    "username": "JohnDoe",
    "phonenumber": "1234567890",
    "email": "john.doe@example.com",
    "isEmailVerified": true
  }
  ```

### Response Format

- **Status Code**: `200 OK`
- **Body**:

  ```json
  {
    "status": "success",
    "message": "Logged in as: JohnDoe",
    "new_access_token": "..."
  }
  ```

### Example Usage in Flutter

```dart
final response = await http.post(
  Uri.parse('http://backend_url/android_login'),
  body: jsonEncode({
    "username": "JohnDoe",
    "phonenumber": "1234567890",
    "email": "john.doe@example.com",
    "isEmailVerified": true
  }),
  headers: {"Content-Type": "application/json"},
);
```

---

## 6. Firebase Login API

### API Endpoint

- **URL**: `/firebase_login`
- **Method**: `POST`

### Description:

This API enables Firebase-based login functionality.

### Request Format

- **Header**:

  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Body**:

  ```json
  {
    "uid": "FirebaseUID"
  }
  ```

### Response Format

- **Status Code**: `200 OK`
- **Body**:

  ```json
  {
    "status": "success",
    "message": "Logged in as: FirebaseUsername",
    "new_access_token": "..."
  }
  ```

### Example Usage in Flutter

```dart
final response = await http.post(
  Uri.parse('http://backend_url/firebase_login'),
  body: jsonEncode({
    "uid": "FirebaseUID"
  }),
  headers: {"Content-Type": "application/json"},
);
```

---

These general formats should help guide the frontend developer in making API requests to the backend.
-----------------------------------------------------------------------------------------------------

---

## Usage of the App

### Coordinating APIs and Managing Tokens

1. **Setting Initial Context**: The first step is to set the initial context for random users using the `/setContext` API. Send the quiz answers in the request body. This will return a temporary `access_token` for the random user.

   ```dart
   headers: {"Authorization": "Bearer TEMPORARY_ACCESS_TOKEN"}
   ```
2. **Single Bot Interaction for Random Users**: After setting the context, you can use the `/getBotResponse` API to interact with the bot once. This API now requires the temporary `access_token` received from the `/setContext` API for authentication.
3. **User Login**: After the initial bot interaction, you can prompt the user to log in using either the `/android_login` or `/firebase_login` API. These will return a personal `access_token` that should replace the temporary one.

   - **Personal Access Tokens**: These are more permanent JWT tokens generated upon successful login. They are required to access the bot indefinitely.
4. **Automatic Re-login and Token Refresh in Android**:

   - **Caching Tokens**: Use Android's secure storage to cache the personal `access_token`. This way, the user will be auto-logged in whenever the app is opened.
   - **Token Refresh**: If the `access_token` is near expiry, use the `/refresh_token` API to get a new `access_token` and `refresh_token`. Replace the old tokens with the new ones in secure storage.

     ```dart
     final response = await http.post(
       Uri.parse('http://backend_url/refresh_token'),
       headers: {"Authorization": "Bearer YOUR_OLD_REFRESH_TOKEN"},
     );
     ```
5. **Subsequent Bot Interactions**: Continue to use the `/getBotResponse` API for further interactions with the bot. Always use the personal `access_token` for authentication.

   ```dart
   headers: {"Authorization": "Bearer YOUR_PERSONAL_ACCESS_TOKEN"}
   ```
6. **Logging Out**: Use the `/logout` API to log out and invalidate the session. Remove all stored tokens on the client side.
7. **Token Refresh**: If the `access_token` is near expiry or has expired, use the `/refresh_token` API to get a new `access_token`. Replace the old `access_token` with the new one in secure storage. Here's how you can implement this in Flutter:

   ```dart
   Future<void> refreshToken() async {
     try {
       final response = await http.post(
         Uri.parse('http://backend_url/refresh_token'),
         headers: {"Authorization": "Bearer YOUR_OLD_REFRESH_TOKEN"},
       );

       if (response.statusCode == 200) {
         final Map<String, dynamic> data = jsonDecode(response.body);
         final String newAccessToken = data['access_token'];
         final String newRefreshToken = data['refresh_token'];

         // Store the new tokens securely
         await secureStorage.write(key: 'access_token', value: newAccessToken);
         await secureStorage.write(key: 'refresh_token', value: newRefreshToken);
       } else {
         // Handle the error according to your needs
       }
     } catch (e) {
       // Handle the exception
     }
   }
   ```

   In this example, `secureStorage` refers to an instance of `FlutterSecureStorage`, which is a Flutter plugin for securely storing data. Make sure to add this to your `pubspec.yaml` if you haven't:

   ```yaml
   dependencies:
     flutter_secure_storage: ^4.0.0
   ```

   You can then call `refreshToken()` whenever you detect that the `access_token` is about to expire or has already expired. This will ensure that the user remains authenticated and can continue to interact with the app without interruptions.

---

### Important Notes:

- Utilize Flutter's `flutter_secure_storage` or Android's secure storage to securely store the JWT tokens.
- Always use HTTPS in production to ensure the secure transmission of tokens and data.
- Implement a global error handling mechanism. If an API call fails due to token expiration or any other reason, prompt the user to log in again.

---

## Flutter Considerations

### For Set Context API:

1. **Error Handling**: Since this API sets up the initial context for the user, it's crucial to handle any errors gracefully. Display appropriate error messages or fallback options to the user.
2. **Loading State**: Show a loading spinner or animation while the request is being processed to indicate that something is happening in the background.

### For Get Bot Response API:

1. **Latency**: This API may take some time to return, so implement a timeout mechanism. Show a timeout message if the API takes too long to respond.
2. **Loading State**: Given the latency, consider showing an animated chat bubble or a similar indicator to inform the user that the bot is 'typing'.
3. **Retry Mechanism**: Offer a 'Retry' button or similar UI element in case the API call fails.

### General:

1. **Asynchronous Programming**: Make sure to use asynchronous programming constructs like `async` and `await` to handle API requests and responses smoothly.
2. **State Management**: Use state management solutions like `Provider` or `Riverpod` to manage the application state effectively.

---

## Figma Considerations

1. **User Feedback**: Include designs for loading states, error messages, and other feedback mechanisms.
2. **Consistent UI**: Ensure that the UI remains consistent between the login, quiz, and chatbot pages.
3. **Responsive Design**: Design layouts that work well on different screen sizes and orientations.
4. **Micro-Interactions**: Add subtle animations or transitions for button clicks, page transitions, etc., to enhance user experience.

---
