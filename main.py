import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks= True)
screen_h, screen_w = pyautogui.size()
while 1:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    #print(landmark_points)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            print(x, y)
            if id ==1:
                screen_h = screen_w / frame_w * x * 4
                screen_w = screen_h / frame_h * y * 4
                pyautogui.moveTo(x, y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if left[0].y - left[1].y < 0.01:
            print('click')
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye controlled frame', frame)
    cv2.waitKey(1)
