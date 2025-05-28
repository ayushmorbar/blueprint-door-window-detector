"""
Blueprint Door and Window Detection - API Server
"""

from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import io
import os

app = Flask(__name__)

# Initialize model variable
model = None

def load_model():
    """Load the trained YOLOv8 model"""
    global model
    model_path = 'models/best.pt'
    
    if os.path.exists(model_path):
        print(f"📦 Loading trained model from: {model_path}")
        model = YOLO(model_path)
        print("✅ Model loaded successfully!")
    else:
        print("⚠️  Trained model not found. Using pre-trained YOLOv8n for testing.")
        model = YOLO('yolov8n.pt')
        print("🔄 Using default model - train your custom model first!")

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        "message": "Blueprint Door and Window Detection API",
        "status": "running",
        "version": "1.0.0",
        "model_loaded": model is not None
    })

@app.route('/detect', methods=['POST'])
def detect_objects():
    """Detection endpoint that accepts image and returns bounding boxes"""
    if model is None:
        load_model()
    
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
        
    file = request.files['image']
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return jsonify({'error': 'Invalid file format. Only PNG/JPG allowed'}), 400
    
    try:
        # Read and process image
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Run inference
        results = model(image)[0]
        
        # Process detections
        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            label = 'door' if class_id == 0 else 'window'
            
            detections.append({
                'label': label,
                'confidence': round(confidence, 3),
                'bbox': [round(x1, 1), round(y1, 1), 
                        round(x2-x1, 1), round(y2-y1, 1)]  # [x, y, width, height]
            })
        
        return jsonify({
            'detections': detections,
            'image_size': {'width': image.width, 'height': image.height},
            'processing_time_ms': round(results.speed['inference'], 1)
        })
        
    except Exception as e:
        return jsonify({'error': f'Error processing image: {str(e)}'}), 500

if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=5000)
