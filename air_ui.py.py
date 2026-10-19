import cv2
import mediapipe as mp
import numpy as np
import math
import os   # 🔥 real file open

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# floating file boxes
files = [
    (200,150,350,250,"notepad"),     # FILE 1
    (450,150,600,250,"calc"),        # FILE 2
    (700,150,850,250,"explorer")     # FILE 3
]

cooldown = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)

    h,w,_ = img.shape

    # draw boxes
    for i,(x1,y1,x2,y2,_) in enumerate(files):
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
        cv2.putText(img,f"FILE {i+1}",(x1+20,y1+60),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:

            ix = int(handLms.landmark[8].x * w)
            iy = int(handLms.landmark[8].y * h)

            tx = int(handLms.landmark[4].x * w)
            ty = int(handLms.landmark[4].y * h)

            cv2.circle(img,(ix,iy),10,(0,255,0),-1)

            # pinch distance
            dist = math.hypot(ix-tx, iy-ty)

            for (x1,y1,x2,y2,app) in files:

                if x1 < ix < x2 and y1 < iy < y2:
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)

                    # 🤏 PINCH = OPEN REAL APP
                    if dist < 40 and cooldown == 0:
                        os.system(app)   # 🔥 opens real app
                        cooldown = 20

            mp_draw.draw_landmarks(img,handLms,
                                   mp_hands.HAND_CONNECTIONS)

    # cooldown timer
    if cooldown > 0:
        cooldown -= 1

    cv2.imshow("Movie Style Air UI",img)

    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()