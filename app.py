from flask import Flask, request, jsonify, render_template
from utils import (
    analyze_symptoms,
    get_healthcare_tips,
    find_nearby_doctors,
    save_consultation,
    validate_symptoms,
    sanitize_input
)
from config import Config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        symptoms = sanitize_input(data.get('symptoms', ''))
        
        # Validate input
        validate_symptoms(symptoms)
        
        # Analyze symptoms
        analysis = analyze_symptoms(symptoms)
        
        # Get healthcare tips
        conditions = [condition['name'] for condition in analysis['conditions']]
        tips = get_healthcare_tips(conditions, symptoms)
        
        # Find nearby doctors if location provided
        doctors = []
        if 'location' in data:
            lat = data['location']['lat']
            lng = data['location']['lng']
            # Get doctors based on top condition
            if analysis['conditions']:
                specialty = analysis['conditions'][0]['name']
                doctors = find_nearby_doctors(lat, lng, specialty)
        
        # Save consultation if user is authenticated
        consultation_id = None
        if 'user_id' in data:
            consultation_id = save_consultation(
                data['user_id'],
                symptoms,
                analysis,
                doctors
            )
        
        return jsonify({
            'success': True,
            'analysis': analysis,
            'healthcare_tips': tips,
            'doctors': doctors,
            'consultation_id': consultation_id
        })
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred'
        }), 500

@app.route('/api/doctors', methods=['GET'])
def get_nearby_doctors():
    try:
        lat = float(request.args.get('lat'))
        lng = float(request.args.get('lng'))
        specialty = request.args.get('specialty')
        
        doctors = find_nearby_doctors(lat, lng, specialty)
        return jsonify({
            'success': True,
            'doctors': doctors
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)