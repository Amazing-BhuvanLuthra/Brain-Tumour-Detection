from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads/'
RESULT_FOLDER = 'static/results/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # Replace with your trained brain tumor model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Run YOLOv8 inference
        results = model(filepath)
        
        # Save result image
        result_img_path = os.path.join(RESULT_FOLDER, filename)
        annotated_frame = results[0].plot()
        cv2.imwrite(result_img_path, annotated_frame)
        
        # Check if a tumor is detected
        tumor_detected = len(results[0].boxes) > 0
        
        return render_template('index.html', uploaded_image=filename, result_image=filename, tumor=tumor_detected)

if __name__ == '__main__':
    app.run(debug=True)
