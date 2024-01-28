from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from supabase import create_client, Client
from datetime import datetime
import object_detection
import jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

desktop_path = os.path.expanduser('~/Desktop')
upload_subdirectory = 'handover-uploads'
UPLOAD_FOLDER = os.path.join(desktop_path, upload_subdirectory)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

objectDetection = object_detection.Object_Detection()

SUPABASE_PROJECT_URL = "https://evttsielkxwfzhbymyfq.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV2dHRzaWVsa3h3ZnpoYnlteWZxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzODM3ODIsImV4cCI6MjAyMTk1OTc4Mn0.R08xPSjOW2_tFfBJVdhezKqorRpPq63KMu7Xs42AEPI"

supabase_client = create_client(SUPABASE_PROJECT_URL, SUPABASE_API_KEY)


@app.route('/')
def index():
    return "Hello"

@app.route('/detect_object', methods=['POST'])
def detect_object():
    try:
        # Check if the 'image' file is in the request
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        image_file = request.files['image']
        # Check if the file is empty
        if image_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_path)
        
        detected_object, category = objectDetection.process_images(image_path)
        
        if category is None:
            category = "N/A"
        
        return [detected_object, category]
    except:
        return "ERROR"

if __name__ == "__main__":
    app.run(debug=True, port=8080)