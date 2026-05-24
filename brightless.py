import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\Manjunath\OneDrive\Desktop\AI\Screenshot 2026-04-28 120647.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h , w) = image_rgb.shape[:2]
center= (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0) 
rotated=cv2.warpAffine(image_rgb, M, (w, h))
plt.imshow(rotated)
plt.title('Rotated Image')
plt.show()

brightness_matrix = np.ones(image_rgb.shape, dtype="uint8") * 100
brightr=cv2.add(image_rgb, brightness_matrix)
plt.imshow(brightr)
plt.title('Brightened Image')
plt.show()