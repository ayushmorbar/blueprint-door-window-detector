---
title: Blueprint Door Window Detector
emoji: 🏗️
colorFrom: blue
colorTo: green
sdk: docker
app_port: 5000
pinned: false
---

Check out the REST API documentation below to detect doors and windows in your blueprints!

## API Usage

Send a POST request to `/detect` with your blueprint image:

```bash
curl -X POST -F "image=@blueprint.png" https://ayushmorbar-blueprint-detector.hf.space/detect
```

Response format:
```json
{
  "detections": [
    {"label": "door", "confidence": 0.91, "bbox": [x, y, width, height]},
    {"label": "window", "confidence": 0.84, "bbox": [x, y, width, height]}
  ],
  "image_size": {"width": 640, "height": 480},
  "processing_time_ms": 150.5
}
```
