
Below are detailed instructions on how each API works in our backend and how the frontend developer can use them.

---

### 1. Login Page API

**Endpoint**: `/login`

**Method**: `GET`

**Description**: This API initiates the OAuth login with Google.

**Input**: None

**Output**: Redirects to Google OAuth login page.

#### Example Usage in Flutter:

```dart
final response = await http.get(Uri.parse('http://backend_url/login'));
```

---

### 2. Logout Page API

**Endpoint**: `/logout`

**Method**: `GET`

**Description**: This API logs out the user and clears the session.

**Input**: None

**Output**: Returns a message saying "Logged out".

#### Example Usage in Flutter:

```dart
final response = await http.get(Uri.parse('http://backend_url/logout'));
```

---

### 3. Set Context API

#### API Endpoint

- **URL**: `/setContext`
- **Method**: `POST`

#### Description:

This API is used to establish the initial context for the chatbot based on user responses to a quiz. It performs an analysis of the answers and stores this information for future interactions with the chatbot.

#### How It Works:

1. The frontend sends a POST request with the quiz answers.
2. The backend processes these answers to establish the user's profile in various categories.
3. The profile is then stored in the database.
4. A summary analysis is returned to the frontend.

#### Request Format

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

#### Response Format

- **Status Code**: `201 CREATED`
- **Body**:
  ```json
  {
    "Physical": {
      "You are": "Mostly Vata",
      "Distribution": {
        "Vata": "60.00%",
        "Pitta": "20.00%",
        "Kapha": "20.00%"
      }
    },
    // ... other topics for 4 more categories
  }
  ```

#### Example Usage in Flutter (Set Context API)

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

### 4. Get Bot Response API

#### API Endpoint

- **URL**: `/getBotResponse`
- **Method**: `POST`

#### Description:

This API facilitates the core chat functionality. It takes a user message as input and returns the chatbot’s response.

#### How It Works:

1. The frontend sends the user’s message via a POST request.
2. The backend processes this message using the GPT-4 model. Note that this step may take some time.
3. Once the model generates a response, it is sent back to the frontend.

#### Request Format

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

#### Response Format

- **Status Code**: `200 OK`
- **Body**:
  ```json
  {
    "response": "Here is information about diabetes..."
  }
  ```

#### Example Usage in Flutter (Get Bot Response API)

```dart
final response = await http.post(
  Uri.parse('http://backend_url/getBotResponse'),
  body: jsonEncode({"user_message": "Tell me about diabetes"}),
  headers: {"Content-Type": "application/json"},
);
```

---

### 5. Android Login API

#### API Endpoint

- **URL**: `/android_login`
- **Method**: `POST`

#### Description:

This API enables login functionality specifically for Android applications. It takes the user's username, phone number, email, and email verification status as input and updates or creates a record in the database. It also updates the user session with the same details.

#### How It Works:

1. The frontend sends a POST request containing the user's login information such as username, phone number, email, and email verification status.
2. The backend checks if the username exists in the session and has a prefix of 'randomlyGenerated'.
3. If so, it fetches the existing user data from the MongoDB database and merges it with the new data provided.
4. If the username doesn't exist or doesn't have the said prefix, a new user record is created.
5. The session details are updated, and the previous conversation and question count are reset.

#### Request Format

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

#### Response Format

- **Status Code**: `200 OK`
- **Body**:
  ```text
  "Logged in as: JohnDoe"
  ```

#### Example Usage in Flutter (Android Login API)

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

These general formats should help guide the frontend developer in making API requests to the backend.
-----------------------------------------------------------------------------------------------------

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
