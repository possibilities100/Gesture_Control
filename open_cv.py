# Gesture_control

# Steps to run:
# 1. use open_cv.py (this file)
# 2. install pip3
# 3. install cv2, pyautogui and mediapipe using pip3 (command: pip3 install -name of the module-)
# 4. run the python file

import cv2 as cv
import mediapipe as mp
from pyautogui import press
from time import sleep

Hand = mp.solutions.hands.Hands(max_num_hands=1)
Draw = mp.solutions.drawing_utils

px8 = 0.0
yp = 0.0
cap = cv.VideoCapture(0)

while cap.isOpened():

    success,img = cap.read()
    if not success:
        print("Camera didnt Initialzed")
        break

    img = cv.flip(img,1)
    rgb_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result = Hand.process(rgb_img)

    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            Draw.draw_landmarks(img,hand_landmark,mp.solutions.hands.HAND_CONNECTIONS,
                                )

            cx8 = hand_landmark.landmark[8].x
            yc = hand_landmark.landmark[8].y

            delta8 = cx8-px8
            deltay = yc-yp

            if hand_landmark.landmark[8].y < hand_landmark.landmark[7].y:

                if  delta8 > 0.2 :
                    press('right')
                    print("RIGHT")
                    sleep(0.3)
            
                elif  delta8 < -0.2:
                    press('left')
                    print("LEFT")
                    sleep(0.3)

                px8 = cx8
                yp = yc

    cv.imshow("Feed",img)
    if cv.waitKey(1) & 0XFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
