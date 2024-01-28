from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from supabase import create_client, Client
from datetime import datetime
import object_detection

app = Flask(__name__)

objectDetection = object_detection.Object_Detection()

SUPABASE_PROJECT_URL = "https://evttsielkxwfzhbymyfq.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV2dHRzaWVsa3h3ZnpoYnlteWZxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzODM3ODIsImV4cCI6MjAyMTk1OTc4Mn0.R08xPSjOW2_tFfBJVdhezKqorRpPq63KMu7Xs42AEPI"

supabase_client = create_client(SUPABASE_PROJECT_URL, SUPABASE_API_KEY)


@app.route('/')
def index():
    return "Hello"

@app.route('/detect_object')
def detect_object():
    output = objectDetection.process_images("./sample_photos/img_youngjin.jpeg")
    return output

if __name__ == "__main__":
    app.run(debug=True, port=8080)