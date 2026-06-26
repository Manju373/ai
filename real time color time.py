import cv2
def color_filter(img,f):
    if f == 'r':
        img[:,:,0] = 0
        img[:,:,1] = 0 
    elif f == 'g':
        img[:,:,0] = 0
        img[:,:,2] = 0
    elif f == 'b':
        img[:,:,1] = 0
        img[:,:,2] = 0 
    return img
cap=cv2.VideoCapture(0)
f="original"
print(" r for red tint")
print(" g for green tint")
print(" b for blue tint")
while True:
    ret,frame=cap.read()
    if not ret:
        break
    key=cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        f='r'
    elif key == ord('g'):
        f='g'
    elif key == ord('b'):
        f='b'
    elif key == ord('o'):
        f='original'
    elif key == ord('q'):
        break
    if f != 'original':
        frame=color_filter(frame,f)
    cv2.imshow("Video",frame)

cap.release()
cv2.destroyAllWindows()