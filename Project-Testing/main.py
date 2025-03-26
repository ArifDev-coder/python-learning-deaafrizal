import cv2
import os

face_ref = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt2.xml')
eye_ref = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
camera = cv2.VideoCapture(0)

<<<<<<< HEAD
def deteksi_wajah(frame):
=======
def detect_face(frame):
>>>>>>> 928db65e05d501dce8a32187eabd5dbad28376db
    optimaze_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale(optimaze_frame, scaleFactor=1.3, minSize=(30, 30), minNeighbors=5)
    return faces

def detect_eye(frame, faces):
    optimaze_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for x, y, w, h in faces:
        roi_gray = optimaze_frame[y:y+h, x:x+w]
        eyes = eye_ref.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

def detection_box(frame):
    faces = detect_face(frame)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
    detect_eye(frame, faces)

def close_camera():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    if not os.path.exists('captured_image'):
        os.makedirs('captured_image')
    img_counter = 0
    
    while True:
        _, frame = camera.read()
        detection_box(frame)
        cv2.imshow('Copyright © 2025 Zarick Co. All rights reserved', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            close_camera()
        elif key == ord('s'):
            image_name = f"captured_image/face_{img_counter}.png"
            cv2.imwrite(image_name, frame)
            print(f"{image_name} saved!")
            image_counter += 1
           

if __name__ == '__main__':
    main()