import cv2 
import vlc 
from urllib.request import urlopen
import datetime
from datetime import datetime
from datetime import timedelta 

def video_record():
    url =  "http://192.168.29.159:8080/video"         
    video = cv2.VideoCapture(url)   
    
    if(video.isOpened() == False):
        print("Error reading video file")

    frame_width = int(video.get(3))                   
    frame_height = int(video.get(4)) 

    size = (frame_width,frame_height)    
    result = cv2.VideoWriter('testforvideo20.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (frame_width,frame_height))

    while(True):       
        ret, frame = video.read()

        if ret == True: 
            result.write(frame)  
            cv2.imshow("Frame",frame)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                break    
        else:  
            break    
    
    video.release()          
    result.release() 
    cv2.destroyAllWindows() 

video_record() 