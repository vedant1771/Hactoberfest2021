# install and import opencv
import cv2

# Load an image
read_img = cv2.imread("Python/grey_opencv_Stark.webp")

# Convert image in greyscale
# cvtColor() converts img into different color spaces
imgGray = cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

# Display Image
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)
