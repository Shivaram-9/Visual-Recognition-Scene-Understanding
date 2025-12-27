import cv2

# Read image
image = cv2.imread("dataset/images/test.jpg")

# Check if image loaded
if image is None:
    print("Image not found!")
    exit()

# Resize image
image = cv2.resize(image, (640, 480))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(1)
cv2.destroyAllWindows()


