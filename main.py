from ultralytics import YOLO

# Load your model
model = YOLO('weed.pt')

# Run detection on the live feed from ESP32-CAM
results = model(source=0, show=True, conf=0.2, save=True)

# Visualize the detections (uncomment if you want to show)
results.show()