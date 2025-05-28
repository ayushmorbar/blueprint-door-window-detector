# Blueprint Door and Window Detection

AI model to detect doors and windows in architectural blueprints using YOLOv8. This project implements manual labeling of blueprint images, trains a YOLOv8 model, and provides an API endpoint for detection.

## Classes
Two classes were labeled in the dataset:
1. `door` - Door symbols in architectural blueprints
2. `window` - Window symbols in architectural blueprints

## Evidence
The `screenshots/` directory contains:
1. `training_results.png` - Training metrics and loss graph
2. `confusion_matrix.png` - Model performance matrix
3. `validation_predictions.jpg` - Example predictions
4. `api_test_detection.png` - API test results

## Project Structure

```
├── images/            # Blueprint images
│   ├── train/        # Training set (16 images)
│   └── val/          # Validation set (5 images)
├── labels/           # YOLO format annotations
│   ├── train/        # Training labels
│   └── val/          # Validation labels
├── models/           # Trained models
│   └── best.pt       # Best performing model
├── screenshots/      # Evidence of work
├── app.py           # API server
├── classes.txt      # Class definitions
└── requirements.txt # Dependencies
```

## Setup and Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage Options

### 1. Using the API Server

Start the API server:
```bash
python app.py
```

Then make requests:
```bash
curl -X POST -F "image=@path/to/blueprint.png" http://localhost:5000/detect
```

### 2. Direct Inference

For quick testing on new blueprints:
```bash
python detect.py path/to/blueprint.png
```

### 3. Training (Optional)

If you want to retrain the model:
```bash
# Train the model
python train.py

# Validate the model
python validate.py
```

## API Usage

The API exposes a single endpoint that accepts blueprint images and returns detected doors and windows:

```bash
# Example API call
curl -X POST -F "image=@images/val/3.png" http://localhost:5000/detect
```

Example Response:
```json
{
  "detections": [
    {"label": "door", "confidence": 0.602, "bbox": [49.2, 191.7, 51.6, 55.1]},
    {"label": "window", "confidence": 0.379, "bbox": [328.8, 48.3, 20.0, 96.0]}
  ],
  "image_size": {"width": 441, "height": 432},
  "processing_time_ms": 109.4
}
```

## Classes

Two classes were labeled in the dataset:
1. `door` - Door symbols in blueprints
2. `window` - Window symbols in blueprints

## Evidence

See the `screenshots/` directory for:
- Manual labeling process
- Training metrics and loss graphs
- Example detections and API output
