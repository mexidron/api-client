#!/bin/python

import sys
import cv2

width = 160
png_file = sys.argv[1] if len(sys.argv) == 2 else "img.jpeg"
CV_PI = 3.1415926535897932384626433832795
step_width = 20
occupancy_threshold = 5 #we allow some noisy pixels in the scanned area
image = cv2.imread(png_file)

#GRAY
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imwrite("1_image_gray.png", image_gray)

#EDGES
image_edges = cv2.Canny(image_gray, 80, 150)
cv2.imwrite("2_image_edges.png", image_edges)

#CLEAN
kernel = np.ones((12,12),np.uint8)
opening = cv2.morphologyEx(bordes, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite("3_image_clean.jpg", opening)


