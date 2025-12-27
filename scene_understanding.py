from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Load image
image = cv2.imread("dataset/images/test.jpg")

# Run detection
results = model(image)

# Count objects
object_count = {}

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        object_count[label] = object_count.get(label, 0) + 1

# Scene understanding logic
if object_count.get("car", 0) > 5:
    scene = "Urban Traffic Road"
    conclusion = "Heavy traffic detected"
elif object_count.get("person", 0) > 5:
    scene = "Crowded Public Area"
    conclusion = "Crowd detected"
else:
    scene = "Normal Outdoor Scene"
    conclusion = "Normal activity"

# Output
print("\n--- SCENE UNDERSTANDING RESULT ---")
print("Objects Detected:")
for obj, count in object_count.items():
    print(f"{obj}: {count}")

print("\nScene Type:", scene)
print("Conclusion:", conclusion)
