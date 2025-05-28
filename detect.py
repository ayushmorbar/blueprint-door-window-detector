"""
Inference script for detecting doors and windows in new blueprints
"""

from ultralytics import YOLO
from PIL import Image, ImageDraw
import sys
import os
import numpy as np

def detect_objects(image_path, save_viz=True):
    """
    Detect doors and windows in a blueprint image
    Args:
        image_path: Path to the blueprint image
        save_viz: Whether to save visualization
    """
    # Load trained model
    model = YOLO('models/best.pt')
    
    # Check if image exists
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return
    
    # Load and process image
    try:
        image = Image.open(image_path)
        
        # Run inference
        results = model(image)[0]
        
        # Process detections
        print(f"\nDetections in {os.path.basename(image_path)}:")
        print("-" * 50)
        
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            label = 'door' if class_id == 0 else 'window'
            
            print(f"{label}: {confidence:.2f} confidence at position "
                  f"[{x1:.1f}, {y1:.1f}, {x2-x1:.1f}, {y2-y1:.1f}]")
        
        print(f"\nProcessing time: {results.speed['inference']:.1f}ms")
        
        # Save visualization
        if save_viz:
            # Get the result image with boxes drawn
            result_plot = results.plot()
            
            # Convert from BGR to RGB
            result_plot = Image.fromarray(result_plot[..., ::-1])
            
            # Save the visualization
            output_path = f"inference_results_{os.path.basename(image_path)}"
            result_plot.save(output_path)
            print(f"\nVisualization saved as: {output_path}")
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python detect.py path/to/blueprint.png")
        sys.exit(1)
    
    detect_objects(sys.argv[1], save_viz=True)
