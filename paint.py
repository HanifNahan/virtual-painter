import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.9)
xp, yp = 0, 0
x1, y1 = 0, 0
imgCanvas = np.zeros((720,1280,3), np.uint8)
drawing = False

pink1 = (255,0,255)
pink2 = (255,0,255)
pink3 = (255,0,255)
pink4 = (255,0,255)
pink5 = (255,0,255)
pink6 = (255,0,255)
pink7 = (255,0,255)
pink8 = (255,0,255)
pink9 = (255,0,255)
pink10 = (255,0,255)
pink11 = (255,0,255)
red = (0,0,255)

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

    # img, box1 = cvzone.putTextRect(img, 'sk batu 16', (100,500), 2, 2, offset=20, border=5, colorR=pink1)
    # if box1[0]<x1<box1[2] and box1[1]<y1<box1[3] and drawing == True:
    #     pink1 = red

    # img, box2 = cvzone.putTextRect(img, 'NIAT', (550,350), 2, 2, offset=20, border=5, colorR=pink2)
    # if box2[0]<x1<box2[2] and box2[1]<y1<box2[3] and drawing == True:
    #     pink2 = red

    # img, box3 = cvzone.putTextRect(img, 'MERENGGANGKAN JARI', (600,50), 2, 2, offset=20, border=5, colorR=pink3)
    # if box3[0]<x1<box3[2] and box3[1]<y1<box3[3] and drawing == True:
    #     pink3 = red

    # img, box4 = cvzone.putTextRect(img, 'MENIPISKAN DEBU', (100,200), 2, 2, offset=20, border=5, colorR=pink4)
    # if box4[0]<x1<box4[2] and box4[1]<y1<box4[3] and drawing == True:
    #     pink4 = red

    # img, box5 = cvzone.putTextRect(img, 'MENYAPU DEBU KE MUKA', (600,200), 2, 2, offset=20, border=5, colorR=pink5)
    # if box5[0]<x1<box5[2] and box5[1]<y1<box5[3] and drawing == True:
    #     pink5 = red

    # img, box6 = cvzone.putTextRect(img, 'MERENGGANGKAN JARI', (850,500), 2, 2, offset=20, border=5, colorR=pink6)
    # if box6[0]<x1<box6[2] and box6[1]<y1<box6[3] and drawing == True:
    #     pink6 = red

    # img, box7 = cvzone.putTextRect(img, 'MENIPISKAN DEBU', (100,350), 2, 2, offset=20, border=5, colorR=pink7)
    # if box7[0]<x1<box7[2] and box7[1]<y1<box7[3] and drawing == True:
    #     pink7 = red

    # img, box8 = cvzone.putTextRect(img, 'MENYAPU DEBU KE TANGAN', (800,350), 2, 2, offset=20, border=5, colorR=pink8)
    # if box8[0]<x1<box8[2] and box8[1]<y1<box8[3] and drawing == True:
    #     pink8 = red

    # img, box9 = cvzone.putTextRect(img, 'BERTURUT-TURUT', (400,500), 2, 2, offset=20, border=5, colorR=pink9)
    # if box9[0]<x1<box9[2] and box9[1]<y1<box9[3] and drawing == True:
    #     pink9 = red

    # img, box10 = cvzone.putTextRect(img, 'BERDOA', (100,500), 2, 2, offset=20, border=5, colorR=pink10)
    # if box10[0]<x1<box10[2] and box10[1]<y1<box10[3] and drawing == True:
    #     pink10 = red

    # img, box11 = cvzone.putTextRect(img, 'TERTIB', (1100,120), 2, 2, offset=20, border=5, colorR=pink11)
    # if box11[0]<x1<box11[2] and box11[1]<y1<box11[3] and drawing == True:
    #     pink11 = red


    # img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)

    cv2.namedWindow("Tayammum", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Tayammum",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    cv2.imshow('Tayammum', img)
    # cv2.imshow('Canvas', imgCanvas)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()