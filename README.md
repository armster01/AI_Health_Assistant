# AI-Powered Patient Symptom Checker & Doctor Recommendation

## 📌 Project Overview
An **AI-powered healthcare web application** that helps users analyze their symptoms, get first-aid advice, and find nearby doctors/hospitals. The system leverages **Gemini API** for medical NLP-based analysis and **Google Maps API** for doctor recommendations.

## 🚀 Features
✅ **Symptom Checker:** Users enter symptoms, and AI predicts possible medical conditions.
✅ **First-Aid & Home Remedies:** Provides self-care tips for mild conditions.
✅ **Doctor & Hospital Recommendations:** Finds nearby healthcare providers based on location.
✅ **Preventive Healthcare Insights:** AI-based suggestions to maintain good health.
✅ **User-Friendly Interface:** Built using **Streamlit** for an interactive UI.
✅ **Secure & Scalable:** Firebase authentication and real-time database integration.

## 🔧 Tech Stack
- **Frontend:** Streamlit (for UI)
- **Backend:** Flask/Django (for API handling)
- **AI Model:** Google Gemini API (for medical NLP & symptom analysis)
- **Database:** Firebase (for user history & recommendations)
- **Maps & Location:** Google Maps API (to fetch nearby doctors/hospitals)
- **Deployment:** Streamlit Cloud / Heroku / AWS

## 📜 Installation Guide
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-symptom-checker.git
cd ai-symptom-checker
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Set Up Firebase Credentials
- Download the **Firebase service account key**.
- Store it in a secure folder, e.g., `config/serviceAccountKey.json`.
- Load it in Python:
```python
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
```

### 4️⃣ Set Up API Keys
Create a **.env** file and add:
```env
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
FIREBASE_CREDENTIALS=config/serviceAccountKey.json
```

### 5️⃣ Run the Application
```bash
streamlit run app.py
```

## 🛠 API Integration
### **1️⃣ Gemini API (For Medical NLP & AI-Based Analysis)**
- Used to analyze symptoms and provide AI-driven recommendations.
- Example request:
```python
import requests
headers = {"Authorization": "Bearer YOUR_GEMINI_API_KEY"}
data = {"symptoms": "fever, headache, cough"}
response = requests.post("https://api.gemini.com/analyze", headers=headers, json=data)
print(response.json())
```

### **2️⃣ Google Maps API (For Nearby Doctor/Hospital Search)**
- Used to fetch real-time locations of healthcare providers.
- Example request:
```python
import requests
params = {
    "location": "28.7041,77.1025",  # Example: Latitude, Longitude
    "radius": "5000",  # 5km radius
    "type": "hospital",
    "key": "YOUR_GOOGLE_MAPS_API_KEY"
}
response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params)
print(response.json())
```

## 📌 Future Enhancements
🔹 **AI-Powered Chatbot:** Provide instant medical advice using conversational AI.
🔹 **Doctor Appointment Booking:** Integrate with hospitals' booking systems.
🔹 **Health Record Storage:** Securely store users' medical histories.
🔹 **Voice Assistant Feature:** Users can interact via voice input.

## 📜 License
This project is **open-source** under the **MIT License**.

## 👨‍💻 Contributing
Contributions are welcome! Feel free to **fork** this repo and submit a PR.

## 📩 Contact
For any queries, reach out to me at **your-email@example.com**

---
🚀 **Let's build a smarter, AI-powered healthcare system!** 🔥

