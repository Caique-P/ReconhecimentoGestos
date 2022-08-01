from cvzone.HandTrackingModule import HandDetector
import cv2
import socket
import pyautogui
import time
import ctypes
user32 = ctypes.windll.user32

cap = cv2.VideoCapture(0)
cap.set(3, 1)
cap.set(4, 1)
success, img = cap.read()
h, w, _ = img.shape
detector = HandDetector(detectionCon=0.1, maxHands=1)

##sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##serverAddressPort = ("127.0.0.1", 5052)

screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    #hands, img = detector.findHands(img)  # with draw
    img = cv2.flip(img, 1)
    hands = detector.findHands(img, draw=False)  # without draw
    data = ["state", "width", "height"]

    if hands:
        # Width and Height of Webcam
    #h, w, c = img.shape
       # print('width:  ', w)
       # print('height: ', h)


        # Hand 1
        hand = hands[0]
        #lmList = hand["lmList"]  # List of 21 Landmark points

        mousefactor = [screensize[0]/width, screensize[1]/height]

        centerpoint = hand['center']
        movemouse = [hand['center'][0] * mousefactor[0], hand['center'][1]* mousefactor[1]]
        print(movemouse)
        pyautogui.moveTo(movemouse)
#        pyautogui.moveTo(movemouse,duration= 0.05)

#        time.sleep(0.05)
        fingers = detector.fingersUp(hand)
        # print(fingers) [1, 0, 0, 0, 0]
        #Detect Gestures
        if fingers == [0,0,0,0,0] or fingers == [1,0,0,0,0]:
           #print("hand closed")
           data[0] = "closed"
           pyautogui.mouseDown(button='left')
        elif fingers == [0,1,0,0,0] or fingers == [1,1,0,0]:
            #print("pointing")
            data[0] = "pointing"
            pyautogui.click(button='left')
        else:

            pyautogui.mouseUp(button='left')
            #print("hand opened")
            data[0] = "opened"
            data[1] = h
            data[2] = w

        #for lm in lmList:

            #data.extend([lm[0], h - lm[1], lm[2]])

        #hand2
        if len(hands) == 2:
            hand2 = hands[1]
            lmList = hand2["lmList"]  # List of 21 Landmark points
            for lm in lmList:
                data.extend([lm[0], h - lm[1], lm[2]])
        #print(data)
        #sock.sendto(str.encode(str(data)), serverAddressPort)

    # Display
    cv2.imshow("Reconhecimento", img)
    cv2.waitKey(1)
