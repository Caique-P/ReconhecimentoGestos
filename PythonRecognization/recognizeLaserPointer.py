import cv2
import numpy as np
cap = cv2.VideoCapture(0)

pts = []
while (1):

    # Take each frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,200,200]) #example value
    upper_red = np.array([10,255,255]) #example value
    mask = cv2.inRange(hsv, lower_red, upper_red)
        
    # remove noise
    kernel =  np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)
    print(maxLoc)
    cv2.circle(frame, maxLoc, 20, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Track Laser', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()