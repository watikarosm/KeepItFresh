import cv2

print("Packaghe Imported")

img = cv2.imread("Resources/lena.png")

cv2.imshow("Output", img)
cv2.waitKey("3000")

