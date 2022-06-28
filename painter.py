import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.9)
xp, yp = 0, 0
x1, y1 = 0, 0
imgCanvas = np.zeros((720,1280,3), np.uint8)
drawing = False

while True:
    ret, img = cap.read(2)
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        # xp, yp = 0, 0
        hand1 = hands[0]
        lmlist1 = hand1['lmList']
        x1, y1 = lmlist1[8][0], lmlist1[8][1]
        x2, y2 = lmlist1[12][0], lmlist1[12][1]

        fingers = detector.fingersUp(hand1)
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
        #     cv2.circle(img, (x1,y1), 20, (255,0,0), cv2.FILLED)
        #     print("Selection Mode")
        
        if fingers[1] and fingers[2]==False:
            drawing = True
            cv2.circle(img, (x1,y1), 10, (0,255,0), cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            cv2.line(img, (xp,yp), (x1,y1), (0,255,0), thickness=10)
            cv2.line(imgCanvas, (xp,yp), (x1,y1), (0,255,0), thickness=10)
            xp, yp = x1, y1
        elif fingers[1] and fingers[2] and fingers[3]==False:
            drawing = False
            cx, cy = (x1+x2)//2, (y1+y2)//2
            cv2.circle(img, (cx,cy), 50, (0,0,0), cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = cx, cy
            cv2.line(img, (xp,yp), (cx,cy), (0,0,0), thickness=100)
            cv2.line(imgCanvas, (xp,yp), (cx,cy), (0,0,0), thickness=100)
            xp, yp = cx, cy
        else:
            drawing = False

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)

    cv2.namedWindow("Paint", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Tayammum",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    cv2.imshow('Paint', img)
    # cv2.imshow('Canvas', imgCanvas)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()