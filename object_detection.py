import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")  # auto-downloads first time

# Read image
image = cv2.imread("dataset/images/test.jpg")

# Run object detection
results = model(image)

# Draw detections
for r in results:
    for box in r.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls = int(box.cls[0])
        conf = box.conf[0]

        label = f"{model.names[cls]} {conf:.2f}"

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show output
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
