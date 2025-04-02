import google.generativeai as genai
from config import Config
import json
import requests
import firebase_admin
from firebase_admin import credentials, firestore
import re

# Initialize Firebase
cred = credentials.Certificate(Config.FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()

def setup_gemini():
    """Initialize the Gemini API"""
    genai.configure(api_key=Config.GEMINI_API_KEY)
    model = genai.GenerativeModel(
        model_name=Config.MODEL_NAME,
        generation_config={
            "temperature": Config.TEMPERATURE,
            "max_output_tokens": Config.MAX_TOKENS,
        }
    )
    return model

def analyze_symptoms(symptoms):
    """Analyze symptoms using Gemini API"""
    try:
        model = setup_gemini()
        prompt = Config.SYMPTOM_ANALYSIS_PROMPT.format(symptoms=symptoms)
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        raise Exception(f"Error analyzing symptoms: {str(e)}")

def get_healthcare_tips(conditions, symptoms):
    """Get personalized healthcare tips"""
    try:
        model = setup_gemini()
        prompt = Config.HEALTHCARE_TIPS_PROMPT.format(
            conditions=conditions,
            symptoms=symptoms
        )
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        raise Exception(f"Error getting healthcare tips: {str(e)}")

def find_nearby_doctors(lat, lng, specialty=None):
    """Find nearby doctors using Google Maps API"""
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": Config.SEARCH_RADIUS,
        "type": "doctor",
        "key": Config.GOOGLE_MAPS_API_KEY
    }
    
    if specialty:
        params["keyword"] = specialty
    
    try:
        response = requests.get(base_url, params=params)
        return response.json().get("results", [])
    except Exception as e:
        raise Exception(f"Error finding nearby doctors: {str(e)}")

def save_consultation(user_id, symptoms, analysis, recommended_doctors):
    """Save consultation details to Firebase"""
    try:
        doc_ref = db.collection('consultations').document()
        doc_ref.set({
            'user_id': user_id,
            'timestamp': firestore.SERVER_TIMESTAMP,
            'symptoms': symptoms,
            'analysis': analysis,
            'recommended_doctors': recommended_doctors
        })
        return doc_ref.id
    except Exception as e:
        raise Exception(f"Error saving consultation: {str(e)}")

def validate_symptoms(symptoms):
    """Validate symptom input"""
    if not symptoms:
        raise ValueError("Symptoms cannot be empty")
    if len(symptoms) > Config.MAX_SYMPTOM_LENGTH:
        raise ValueError(f"Symptom description too long. Maximum length is {Config.MAX_SYMPTOM_LENGTH} characters.")
    return True

def sanitize_input(text):
    """Sanitize user input"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()