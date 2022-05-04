import cv2 
import vlc 
from urllib.request import urlopen
import datetime
from datetime import datetime  
from datetime import timedelta 

#This will make audio instance and is need to get the audio
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new('http://192.168.29.237:8080/audio.wav')   
Media.get_mrl()   
player.set_media(Media)

img = cv2.imread("sq.jpg")
def record(filepath, stream):
    fd = open(filepath, 'wb')  
    while 1:
        if cv2.waitKey(1) & 0xFF == ord('s'):
           fd.close()       
           break      
        else:     
            cv2.imshow("Sample",img) 
            player.play()    
            data = stream.read(10000)
            fd.write(data)
                     
record('audio_test20.wav', urlopen('http://192.168.29.237:8080/audio.wav'))         
