import cv2 #for using computervision
import mediapipe as mp #for using dataset
import pyautogui #for using automation

face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()

#capturing video
cap=cv2.VideoCapture(0)

while True:
    #read the image
    _,img=cap.read()

    #flip the image
    img=cv2.flip(img,1)

    #changing bgr image into rgb
    rgb_frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #process the face image
    output=face_mesh.process(rgb_frame)

    #extract all the landmarks in th face
    landmark_points=output.multi_face_landmarksq

    #check the landmarks
    if landmark_points:

        #extract the shape of the frames
        frame_h,frame_w,num_channels=img.shape
        
        landmarks=landmark_points[0].landmark
        for landmark in landmarks[474:478]:
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(img,(x,y),3,(0,255,0))
            if id==1:
                screen_x=screen_w/frame_w*x
                screen_y=screen_h/frame_w*y
                pyautogui.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]

        #Tracking the eyes
        for landmark in left:
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(img,(x,y),3,(0,255,255))

        #control the mouse
        if (left[0].y,left[1].y):
            pyautogui.click()
            pyautogui.sleep(1)

    #show the frames
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

