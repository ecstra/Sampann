from xml.dom import ValidationErr
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
import os
from dotenv import load_dotenv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv('DATABASE_NAME'),
    'host': os.getenv('DATABASE_URL'),
    'tls': True
}

db = MongoEngine(app)

class Dosha(db.EmbeddedDocument):
    you_are = db.StringField(choices=['Mostly Vata', 'Mostly Pitta', 'Mostly Kapha', 'All-rounded'])
    distribution = db.DictField()
    def validate_you_are(you_are):
        if you_are not in ['Mostly Vata', 'Mostly Pitta', 'Mostly Kapha', 'All-rounded']:
            raise ValidationErr("Invalid 'you_are' value. Must be one of 'Mostly Vata', 'Mostly Pitta', 'Mostly Kapha', 'All-rounded'")

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    hashedPW = db.StringField(required=True)
    
    physical = db.EmbeddedDocumentField('Dosha')
    mental = db.EmbeddedDocumentField('Dosha')
    emotional = db.EmbeddedDocumentField('Dosha')
    digestive = db.EmbeddedDocumentField('Dosha')

# Route to create a new user
@app.route('/', methods=['POST'])
def create_user():
    try:
        data = request.json
        new_user = User(
            username=data['username'],
            name=data['name'],
            email=data['email'],
            hashedPW=data['password'],
            physical=Dosha(**data['physical']),
            mental=Dosha(**data['mental']),
            social=Dosha(**data['social']),
            emotional=Dosha(**data['emotional']),
            digestive=Dosha(**data['digestive'])
        )
        new_user.save()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to get all fields for one user by their username
@app.route('/<username>', methods=['GET'])
def get_user(username):
    user = User.objects(username=username).first()
    if user:
        user_data = {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'hashedPW': user.hashedPW,
            'physical': user.physical.to_mongo(),
            'mental': user.mental.to_mongo(),
            'social': user.social.to_mongo(),
            'emotional': user.emotional.to_mongo(),
            'digestive': user.digestive.to_mongo(),
        }
        return jsonify(user_data), 200
    else:
        return jsonify({'message': 'User not found'}), 404