# Developer Quick Reference

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Clone repository
git clone <repository-url>
cd ayurvedic-chatbot

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your values

# Run application
python app.py
```

### 2. Environment Variables
```bash
# Required
JWT_SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_key
DATABASE_URL=mongodb://localhost:27017/ayurvedic
DATABASE_NAME=ayurvedic

# Optional
SECRET_KEY=your_flask_secret
FLASK_ENV=development
FLASK_DEBUG=True
```

## 📚 API Endpoints

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/setContext` | POST | Optional | Set health assessment context |
| `/getBotResponse` | POST | Required | Get AI response |
| `/android_login` | POST | Optional | Android user login |
| `/firebase_login` | POST | Optional | Firebase user login |
| `/refresh_token` | POST | Required | Refresh JWT tokens |
| `/logout` | POST | Required | Logout user |

## 🔐 Authentication

### JWT Headers
```http
Authorization: Bearer <your_jwt_token>
Content-Type: application/json
```

### Token Lifecycle
- **Access Token**: 30 days
- **Refresh Token**: 30 days
- **Anonymous Users**: Limited to 1 bot interaction

## 🗄️ Database Schema

### Users Collection
```javascript
{
  "Username": "string",
  "phone_number": "string", 
  "email": "string",
  "isEmailVerified": "boolean",
  "analysis_results": {
    "Vata": "percentage%",
    "Pitta": "percentage%",
    "Kapha": "percentage%"
  },
  "context_set": "boolean",
  "question_count": "number",
  "role": "boolean",
  "conversation": [/* message objects */]
}
```

### Message Object
```javascript
{
  "role": "system|user|assistant",
  "content": "message content"
}
```

## 🤖 AI Integration

### GPT Function Parameters
```python
def gpt(user_data, question, conversation, 
        model="gpt-4",           # OpenAI model
        temperature=0.7,          # 0.0-1.0, creativity
        max_tokens=6000):         # Response length
```

### Content Classification
- **Primary**: Physical, Financial, Schemes
- **Secondary**: Pranayama, Yoga, Mudras, etc.
- **Tertiary**: Specific techniques and topics

## 🛡️ Security Features

### Message Validation
```python
# Check if message is safe
is_safe = message_check(user_message)

# Features:
# - Prompt injection detection
# - Content moderation
# - Malicious content filtering
```

### Rate Limiting
- Anonymous users: 1 bot interaction
- Authenticated users: Unlimited

## 📱 Client Integration

### Flutter Example
```dart
class AyurvedicBotService {
  static const String baseUrl = 'http://localhost:5000';
  String? accessToken;

  Future<String> getBotResponse(String message) async {
    final response = await http.post(
      Uri.parse('$baseUrl/getBotResponse'),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer $accessToken',
      },
      body: jsonEncode({'user_message': message}),
    );
    
    if (response.statusCode == 200) {
      return jsonDecode(response.body)['response'];
    }
    throw Exception('Failed to get response');
  }
}
```

### Python Example
```python
import requests

def get_bot_response(message, token):
    response = requests.post(
        "http://localhost:5000/getBotResponse",
        json={"user_message": message},
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()["response"]
```

## 🔧 Development Tools

### Testing
```bash
# Run tests
python -m pytest

# With coverage
python -m pytest --cov=.

# Specific test file
python -m pytest test.py
```

### Debug Mode
```python
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
```

### Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Processing request...")
logger.error("Error occurred: %s", str(error))
```

## 🚀 Deployment

### Docker
```bash
# Build image
docker build -t ayurvedic-chatbot .

# Run container
docker run -p 5000:5000 ayurvedic-chatbot

# With docker-compose
docker-compose up -d
```

### Production
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn --bind 0.0.0.0:5000 --worker-class gevent app:app

# With environment variables
gunicorn --bind 0.0.0.0:5000 --worker-class gevent --env-file .env app:app
```

## 📊 Monitoring

### Key Metrics
- Response time: < 2 seconds
- Error rate: < 1%
- Uptime: 99.9%
- User satisfaction: High

### Health Checks
```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected" if db else "disconnected"
    })
```

## 🐛 Common Issues

### 1. JWT Token Expired
**Error**: 401 Unauthorized
**Solution**: Use refresh token endpoint

### 2. MongoDB Connection
**Error**: Connection refused
**Solution**: Check DATABASE_URL and MongoDB service

### 3. OpenAI API
**Error**: API key invalid
**Solution**: Verify OPENAI_API_KEY environment variable

### 4. Content Classification
**Error**: Generic responses
**Solution**: Check content_categories.json file integrity

## 📝 Code Style

### Python
- Use type hints where possible
- Follow PEP 8 guidelines
- Document functions with docstrings
- Use meaningful variable names

### Example
```python
def analyze_answers(answer_dict: dict) -> dict:
    """
    Analyze quiz responses to determine dosha constitution.
    
    Args:
        answer_dict: Dictionary mapping question numbers to answers
        
    Returns:
        Dictionary with dosha percentages
    """
    # Implementation here
    pass
```

## 🔄 Update Procedures

### Content Updates
1. Edit `content_categories.json`
2. Test classification with sample queries
3. Deploy updated file
4. Monitor response quality

### System Updates
1. Update dependencies: `pip install -r requirements.txt`
2. Test functionality
3. Deploy with zero downtime
4. Monitor system health

## 📞 Support

### Documentation
- **API Reference**: `API_DOCUMENTATION.md`
- **Technical Details**: `TECHNICAL_DOCUMENTATION.md`
- **User Guide**: `README.md`

### Development Team
- Code reviews and pull requests
- Issue tracking and bug reports
- Feature requests and enhancements
- Performance optimization

---

**Quick Tip**: Use the `test.py` file for testing core functions without Flask dependencies during development.