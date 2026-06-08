import cv2

new_img=cv2.imread (r"C:\Users\Manjunath\OneDrive\Desktop\AI\Screenshot 2026-04-28 120647.png") 

if new_img is None:
    print("error")
else: 
    print(" r for red tint")
    print(" g for green tint")
    print(" b for blue tint")
    print(" q for quit")
    print("i for increase red tint")
    print("d for decrease blue tint")

    while True:
        key=cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            new_img[:,:,0] = 0
            new_img[:,:,1] = 0 

        elif key == ord('g'):
            new_img[:,:,0] = 0
            new_img[:,:,2] = 0
        
        elif key == ord('b'):
            new_img[:,:,1] = 0
            new_img[:,:,2] = 0 
        
        elif key == ord('i'):
            new_img[:,:,2] = cv2.add(new_img[:,:,2], 50)

        elif key == ord('d'):
            new_img[:,:,0] = cv2.subtract(new_img[:,:,0], 50)
        
        elif key == ord('q'):
            break

        cv2.imshow("Image", new_img)

