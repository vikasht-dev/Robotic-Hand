from traceback import print_tb
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
mySerial = SerialObject("COM14")
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
          
        
        fingers = detector.fingersUp(hand1)
        mySerial.sendData(fingers)


            # Find Distance between two Landmarks. Could be same hand or different hands
              # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
    # Display
    cv2.imshow("Image", img)
    k=cv2.waitKey(1)
    if k==27:
      print("escaping...")
      cv2.destroyAllWindows()
    elif k==ord("q"):
      print("quiting...")
      cv2.destroyAllWindows()
      break
     
