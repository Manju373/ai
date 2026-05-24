import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\Manjunath\OneDrive\Desktop\AI\Screenshot 2026-04-28 120647.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('RGB Image')
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()

cropped_image = image[50:200, 50:200]
cropped_image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image_rgb)
plt.title('Cropped Image')
plt.show()