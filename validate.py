"""
Validate trained model on validation set
"""

from ultralytics import YOLO

# Load trained model
model = YOLO('models/best.pt')

# Validate on validation set
metrics = model.val(data='dataset.yaml')
print(f"\nValidation Results:")
print(f"mAP50: {metrics.box.map50:.3f}")
print(f"mAP50-95: {metrics.box.map:.3f}")

# Per-class results
for i, ap50 in enumerate(metrics.box.ap50):
    class_name = 'door' if i == 0 else 'window'
    print(f"{class_name}: {ap50:.3f} mAP50")