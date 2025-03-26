import cv2

face_ref = cv2.CascadeClassifier('face_ref.xml')
camera = cv2.VideoCapture(0)

def deteksi_wajah(frame):
    optimaze_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale(optimaze_frame, scaleFactor=1.3, minSize=(500, 500), minNeighbors=5)
    return faces

def kotak_deteksi(frame):
    for x, y, w, h in kotak_deteksi(frame):
        cv2.rectangle(frame, (x, y), (x+w), (y+h), (255, 0, 0), 3)

def close_camera():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = camera.read()
        kotak_deteksi(frame)
        cv2.imshow('ZarickFace AI', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_camera()    

if __name__ == '__main__':
    main()