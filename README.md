# Brain Tumor Detection using YOLOv8

## Overview
This Flask-based web application allows users to upload MRI scan images and detect the presence of a brain tumor using a **YOLOv8** object detection model. The model processes the uploaded image and provides an annotated output indicating whether a tumor is detected.

## Features
- Upload MRI scan images for analysis
- Uses **YOLOv8** for brain tumor detection
- Displays the uploaded and processed images
- Provides real-time results on tumor detection
- Built with Flask and Bootstrap for a clean and professional UI

## Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/brain-tumor-detection.git
cd brain-tumor-detection
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```
By default, the app runs on **http://127.0.0.1:5000/**

## File Structure
```
brain-tumor-detection/
│── app.py             # Flask backend
│── requirements.txt   # Dependencies
│── static/
│   ├── uploads/       # Stores uploaded images
│   ├── results/       # Stores processed images
│── templates/
│   ├── index.html     # Frontend HTML
```

## Usage
1. Open the web application in your browser.
2. Click **Choose File** and upload an MRI scan.
3. Click **Upload & Detect** to start the detection.
4. The result will display the uploaded image and the detected tumor (if any).

## Dependencies
- **Flask** - Web framework
- **Werkzeug** - Secure file handling
- **Ultralytics** - YOLOv8 model
- **OpenCV** - Image processing
- **NumPy** - Array operations
- **Torch** - Deep learning framework

## Model
The detection model is based on **YOLOv8**, which is pre-trained and can be fine-tuned on MRI datasets for improved accuracy.

## Contributing
Feel free to fork this repository, improve the model, or enhance the UI. Contributions are welcome! 🚀

## License
This project is licensed under the **MIT License**.

