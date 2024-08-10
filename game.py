import cv2 as cv
import mediapipe as mp
import package.mechanics as mechanics
import numpy as np
import cvzone
cap=cv.VideoCapture(0)

player_ping=cv.imread('img/ping.png',cv.IMREAD_UNCHANGED)
computer_ping=cv.imread('img/ping.png',cv.IMREAD_UNCHANGED)
ball_img=cv.imread('img/pong.png',cv.IMREAD_UNCHANGED)

ping_height,ping_width=player_ping.shape[:2]
pong_height,pong_width=ball_img.shape[:2]

player=mechanics.player()
computer=mechanics.computer()
ball=mechanics.pong(x=400,y=400)

mp_drawing=mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

game_over=False
x,y=player.x,player.y
with mp_hands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5
                    ) as hand:
    while True:
        if not game_over:
            ball.move()
            computer.move(ball)
            game_over=ball.isGameOver(player,computer)
            ret,frame=cap.read()
            resized_frame=cv.resize(frame,(800,700))
            blank_img=np.zeros_like(resized_frame)
            results=hand.process(resized_frame)
            if results.multi_hand_landmarks:
                
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(resized_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    index_tip = hand_landmarks.landmark[8]  
                    h, w, _ = resized_frame.shape
                    x, y = int(index_tip.x * w), int(index_tip.y * h)
                    player.y=y
                    cv.circle(resized_frame, (x, y), 10, (255, 0, 0), -1)
                    
                    
            

            faded_img=cv.addWeighted(resized_frame,0.3,blank_img,0.7,0)
            flipped_resized_frame=cv.flip(faded_img,1)
            img=cvzone.overlayPNG(flipped_resized_frame,player_ping,(player.x,player.y-30))
            img=cvzone.overlayPNG(img,computer_ping,(int(computer.x),int(computer.y)))
            img=cvzone.overlayPNG(img,ball_img,(int(ball.x),int(ball.y)))
        else:
            if game_over==-1:
                win_lose_text="YOU WON !!"
                text_colour=(0,225,0)
            else:
                win_lose_text="YOU LOST !!"
                text_colour=(0,0,225)
            cv.putText(img,"GAME OVER", (200,200), cv.FONT_HERSHEY_SIMPLEX, 1, (225,225,0), 2, cv.LINE_AA)
            cv.putText(img,win_lose_text, (200,300), cv.FONT_HERSHEY_SIMPLEX, 0.8, text_colour, 2, cv.LINE_AA)
            cv.putText(img,"press SPACEBAR to again or ESC to exit", (200,400), cv.FONT_HERSHEY_SIMPLEX, 0.5, (225,225,0), 1, cv.LINE_AA)
            
        cv.imshow("feed",img)
        key=cv.waitKey(1) & 0xff
        if key==32:
            game_over=False
            computer.y=10
            ball.x=200
            ball.y=400
        if key==27:
            break
    
cap.release()
cv.destroyAllWindows()