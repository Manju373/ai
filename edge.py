import cv2 
import numpy as np
import matplotlib.pyplot as plt

def show (title, image):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.show()

def edge_detection(image_path):
    image=cv2.imread(image_path)
    if image is None:
        print("image not found")
        return 
    else:
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        while True:
            print("1, Sobel Edge Detection")
            print("2, Canny Edge Detection")
            print("3, Gaussian Blur")
            print("4, exit")

            choice= input("Enter your choice: ")
            if choice == '1':
                sobelx=cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
                sobely=cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
                sobel_combined=cv2.magnitude(sobelx, sobely)
                show("Sobel Edge Detection", sobel_combined)
            elif choice == '2':
                low=100
                high=200
                edges=cv2.Canny(gray, low, high)
                show("Canny Edge Detection", edges)
            elif choice == '3':
                k=11
                blur = cv2.GaussianBlur(gray, (k, k), 0)
                show("Gaussian Blur", blur)
            elif choice == '4':
                print("Exiting...")
                break
edge_detection(r"C:\Users\Manjunath\OneDrive\Desktop\AI\Screenshot 2026-04-28 120647.png")