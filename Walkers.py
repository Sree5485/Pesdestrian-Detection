import cv2

body_classifier=cv2.CascadeClassifier("haarcascade_fullbody.xml")

vid=cv2.VideoCapture('walking.avi')

while True:
    
    ret,frame= vid.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=body_classifier.detectMultiScale(grey,1.1,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 32: 
        break

vid.release()
cv2.destroyAllWindows()
