import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Updated to Free Model (2.5 Flash)
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message")
    try:
        response = model.generate_content(user_msg)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

# ✅ Serve sitemap.xml from static folder
@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')

if __name__ == "__main__":
    app.run(debug=True)
