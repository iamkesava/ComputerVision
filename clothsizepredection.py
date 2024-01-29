
import cv2
import mediapipe as mp
import time

mppose=mp.solutions.pose
pose=mppose.Pose()
mpdraw=mp.solutions.drawing_utils

pTime=0
cTime=0
cap=cv2.VideoCapture(1)

while cap.isOpened():
    _,img=cap.read()
    if img is None:
        print("Error: Unable to read frame from the camera.")
        break
    img2=img.copy()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=pose.process(imgRGB)
    if result.pose_landmarks:
        mpdraw.draw_landmarks(img,result.pose_landmarks,mppose.POSE_CONNECTIONS)

        right_hand_ankle_x=0
        right_hand_ankle_y=0
        right_hand_ankle=0
        
        left_hand_ankle_x=0
        left_hand_ankle_y=0
        left_hand_ankle=0
        
        right_shoulder_x=0
        right_shoulder_y=0
        right_shoulder=0
        
        left_shoulder_x=0
        left_shoulder_y=0
        left_shoulder=0
        
        right_leg_anckle_x=0
        right_leg_anckle_y=0
        right_leg_anckle=0
        
        right_leg_knee_x=0
        right_leg_knee_y=0
        right_leg_knee=0
        
        left_leg_anckle_x=0
        left_leg_anckle_y=0
        left_leg_anckle=0
        
        right_shoulder_x=0
        right_shoulder_y=0
        right_shoulder=0
        
        left_shoulder_x=0
        left_shoulder_y=0
        left_shoulder=0
        
        right_hand_knee_x=0
        right_hand_knee_y=0
        right_hand_knee=0
        
        left_hand_knee_x=0
        left_hand_knee_y=0
        left_hand_knee=0
        
        left_leg_knee_x=0
        left_leg_knee_y=0
        left_leg_knee=0
        
        right_hip_x=0
        right_hip_y=0
        right_hip=0

        left_hip_x=0
        left_hip_y=0
        left_hip=0
        
        alt_img=0
    
        for id,lm in enumerate((result.pose_landmarks.landmark)):     
            h,w,c=img.shape
            #print(id,lm)
            cx,cy=int(lm.x*w),int(lm.y*h)
            cv2.putText(img,str(id),(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),1)
            #cv2.circle(img,(cx,cy),10,(255,0,0),-1)
            if id==11:
                left_shoulder_x=cx
                left_shoulder_y=cy
                left_shoulder=(cx,cy)
                
               
            #right shoulder
            elif id==12:
                #y=cy-h
                right_shoulder_x=cx
                right_shoulder_y=cy
                right_shoulder=(cx,cy)
                
            #right hand anckle
            elif id==16:
                right_hand_ankle_x=cx
                right_hand_ankle_y=cy
                right_hand_ankle=(cx,cy)
                
            #left hand anckle
            elif id==15:
                left_hand_ankle_x=cx
                left_hand_ankle_y=cy
                left_hand_ankle=(cx,cy)
                               
            #left hip
            elif id==23:
                left_hip_x=cx
                left_hip_y=cy
                left_hip=(cx,cy)
                
            #right hip
            elif id==24:
                right_hip_x=cx
                right_hip_y=cy
                right_hip=(cx,cy)
                
            #left leg anckle
            elif id==27:
                left_leg_anckle_x=cx
                left_leg_anckle_y=cy
                left_leg_anckle=(cx,cy)
              
            #right leg anckle
            elif id==28:
                right_leg_anckle_x=cx
                right_leg_anckle_y=cy
                right_leg_anckle=(cx,cy)
                
            #right leg knee
            elif id==26:
                right_leg_knee_x=cx
                right_leg_knee_y=cy
                right_leg_knee=(cx,cy)
                
            #left leg knee
            elif id==25:
                left_leg_knee_x=cx
                left_leg_knee_y=cy
                left_leg_knee=(cx,cy)
                
            #right hand knee
            elif id==14:
                right_hand_knee_x=cx
                right_hand_knee_y=cy
                right_hand_knee=(cx,cy)
                
            #left hand knee
            elif id==13:
                left_hand_knee_x=cx
                left_hand_knee_y=cy
                left_hand_knee=(cx,cy)
         
            if left_shoulder and right_hip:
                cv2.line(img2,(right_shoulder),(left_shoulder),(0,255,0),2)
                cv2.line(img2,(left_shoulder),(left_hip),(0,255,0),2)
                cv2.line(img2,(left_hip),(right_hip),(0,255,0),2)
                cv2.line(img2,(right_hip),(right_shoulder),(0,255,0),2)
                
            if right_shoulder and right_hand_knee:
                x = min(right_shoulder[0], right_hand_knee[0])
                y = min(right_shoulder[1], right_hand_knee[1])
                w = abs(right_shoulder[0] - right_hand_knee[0])
                h = abs(right_shoulder[1] - right_hand_knee[1])
                #cv2.putText(img2,str(h),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2,cv2.LINE_AA)
                #cv2.circle(img,(int(x),int(y),5,(0,0,255,-1))
                cv2.rectangle(img2,right_shoulder,right_hand_knee,(255,0,0),2)
                
            if right_hand_knee and right_hand_ankle:
                cv2.rectangle(img2,right_hand_knee,right_hand_ankle,(255,0,0),2)
                x = min(right_shoulder[0], right_hand_knee[0])
                y = min(right_shoulder[1], right_hand_knee[1])
                w = abs(right_shoulder[0] - right_hand_knee[0])
                h = abs(right_shoulder[1] - right_hand_knee[1])
                cv2.putText(img2,str(h),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2,cv2.LINE_AA)
            
            if left_shoulder and left_hand_knee:
                cv2.rectangle(img2,left_shoulder,left_hand_knee,(255,0,0),2)
                
            if left_hand_knee and left_hand_ankle:
                cv2.rectangle(img2,left_hand_knee,left_hand_ankle,(255,0,0),2)
                
            if right_hip and right_leg_knee:
                cv2.rectangle(img2,right_hip,right_leg_knee,(255,0,0),2)
                
            if right_leg_knee and right_leg_anckle:
                cv2.rectangle(img2,right_leg_knee,right_leg_anckle,(255,0,0),2)
                
            if left_hip and left_leg_knee:
                cv2.rectangle(img2,left_hip,left_leg_knee,(255,0,0),2)
                
            if left_leg_knee and left_leg_anckle:
                cv2.rectangle(img2,left_hip,left_leg_anckle,(255,0,0),2)
        
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime    
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
 