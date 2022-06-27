import cv2
import numpy as np
import socket


cap = cv2.VideoCapture(0)

pts = []

 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)
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
    if(maxLoc[0] != 0 and maxLoc[1] != 0):
        data = [0,0]
        data[0] = maxLoc[0]   
        print(maxLoc, end="\r")
        cv2.circle(frame, maxLoc, 20, (0, 0, 255), 2, cv2.LINE_AA)
        data[1] = maxLoc[1]
        sock.sendto(str.encode(str(data)), serverAddressPort)
    else:
        print("..........", end='\r')

    cv2.imshow('Track Laser', frame)
        
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
