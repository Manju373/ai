import cv2
image= cv2.imread(r"C:\Users\Manjunath\OneDrive\Desktop\AI\Screenshot 2026-04-28 120647.png")
cv2.namedWindow(" loaded image", cv2.WINDOW_NORMAL)
cv2.imshow(" loaded image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"image dimensions: {image.shape}")
