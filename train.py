"""
Train YOLOv8 model on blueprint dataset
"""

from ultralytics import YOLO
import yaml

# Create dataset config
dataset_config = {
    'path': '.',
    'train': 'images/train',
    'val': 'images/val',
    'names': {
        0: 'door',
        1: 'window'
    }
}

# Save dataset config
with open('dataset.yaml', 'w') as f:
    yaml.dump(dataset_config, f)

# Load YOLOv8 model
model = YOLO('yolo11m.pt')

# Train the model
results = model.train(
    data='dataset.yaml', # Path to dataset config
    epochs=100, # Number of epochs
    imgsz=640, # Image size
    batch=16, # Batch size
    device="cpu",  # Change to "cuda" for GPU training
    name='blueprint_detector', # Model name
    patience=20, # Early stopping patience
    project='models', # Project directory
    save=True # Save the model after training
)
