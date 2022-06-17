from cvzone.HandTrackingModule import HandDetector
import cv2
import socket
 
cap = cv2.VideoCapture(0)
cap.set(3, 300)
cap.set(4, 100)
success, img = cap.read()
h, w, _ = img.shape
detector = HandDetector(detectionCon=0.8, maxHands=2)
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)
 
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw
    data = ["state", "width", "height"]
 
    if hands:
        # Width and Height of Webcam
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
        h, w, c = img.shape
       # print('width:  ', w)
       # print('height: ', h)


        # Hand 1
        hand = hands[0]
        lmList = hand["lmList"]  # List of 21 Landmark points
        
        fingers = detector.fingersUp(hand)
        # print(fingers) [1, 0, 0, 0, 0]
        #Detect Gestures
        if fingers == [0,0,0,0,0] or fingers == [1,0,0,0,0]:
           #print("hand closed") 
           data[0] = "closed"
        elif fingers == [0,1,0,0,0] or fingers == [1,1,0,0]:
            #print("pointing")
            data[0] = "pointing"
        else:
            #print("hand opened")
            data[0] = "opened"
            data[1] = h
            data[2] = w
        
        for lm in lmList:
            
            data.extend([lm[0], h - lm[1], lm[2]])
        
        #hand2
        if len(hands) == 2:
            hand2 = hands[1]
            lmList = hand2["lmList"]  # List of 21 Landmark points
            for lm in lmList:
                data.extend([lm[0], h - lm[1], lm[2]])
        #print(data)
        sock.sendto(str.encode(str(data)), serverAddressPort)
 
    # Display
    cv2.imshow("Reconhecimento", img)
    cv2.waitKey(1)