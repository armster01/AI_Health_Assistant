from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Config:
    # API Keys
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH')
    
    # Gemini API settings
    MODEL_NAME = "gemini-pro"
    TEMPERATURE = 0.7
    MAX_TOKENS = 1024
    
    # Application settings
    MAX_SYMPTOM_LENGTH = 1000
    SEARCH_RADIUS = 5000  # meters for nearby doctors search
    
    # Prompt templates
    SYMPTOM_ANALYSIS_PROMPT = """
    As a medical AI assistant, analyze the following symptoms and provide:
    1. Possible conditions (from most to least likely)
    2. Severity level (Low/Medium/High)
    3. First-aid advice and home remedies
    4. Whether immediate medical attention is needed
    5. Preventive measures
    
    Symptoms: {symptoms}
    
    Format the response as JSON with the following structure:
    {
        "conditions": [{"name": "", "likelihood": ""}],
        "severity": "",
        "immediate_attention": true/false,
        "first_aid": [],
        "home_remedies": [],
        "preventive_measures": []
    }
    """
    
    HEALTHCARE_TIPS_PROMPT = """
    Provide personalized healthcare tips based on the following conditions and symptoms:
    
    Conditions: {conditions}
    Symptoms: {symptoms}
    
    Focus on:
    1. Lifestyle modifications
    2. Diet recommendations
    3. Exercise suggestions
    4. Warning signs to watch for
    
    Format as a JSON list of tips.
    """