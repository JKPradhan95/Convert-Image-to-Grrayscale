import cv2

color = cv2.imread('DSC_0383-01.jpeg', 0)
cv2.imwrite('DSC_0383-01-gray.jpeg', color)
