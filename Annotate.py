import cv2
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\Manjunath\OneDrive\Desktop\AI\Screenshot 2026-04-28 120647.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h , w, _= img.shape
cv2.rectangle(img, (50, 50), (w-50, h-50), (255, 0, 0), 5)
cv2.circle(img, (w//2, h//2), 50, (0, 255, 0), -1)
cv2.line(img, (0, 0), (w, h), (0, 0, 255), 5)
cv2.putText(img, "Annotated Image", (50, h-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
cv2.arrowedLine(img, (w//2, h//2), (w//2 + 100, h//2), (255, 0, 255), 5)
cv2.imshow("Annotated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()