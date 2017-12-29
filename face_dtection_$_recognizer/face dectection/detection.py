import cv2
#for capturing images through webcam
import numpy as np
#for complex calculations

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
#cascadeclassifier is a class use to classify the image through the algorithm haarcascade_frontalface_default.xml
cam=cv2.VideoCapture(0);
#setting the webcam control in cam variable .0 is for selecting our web cam . most cases 0 will work if it doesnot u can try 1,2,3 

while(True):
    ret,img=cam.read();
    #reading the frames through webcam by cam.read and storing in ret,img where ret is The methods/functions grab the next frame from video file or camera and return
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #changing the coloured image to a gray color image so that face detector has to detect face from a selected color 
    faces = facedetect.detectMultiScale(gray, 1.3, 5);
    #the gray color which it is going to detect is in the range between 1.3 to 5 and store detected faces in faces
    for (x,y,w,h) in faces:
        #loop selecting all faces noy just a single one
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2);
        #drawing a rectangle on object i.e the face through some of its funn it include x,y are cordinates and w,h is width and height 
        cv2.imshow('frame',img)
        #show output throught imshow named as frame and passes it the image which is it comming from cam which controls or operating the webcam of hardware
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #frame waits for pressing just only one key and that key is q 
        break
        #if that happen it will goes out from loop
    
cam.release()
#release the web cam
cv2.destroyAllWindows()
#destroy that frame
