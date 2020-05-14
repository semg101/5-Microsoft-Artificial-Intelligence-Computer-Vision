#import av
#container = av.open('sakvideo.mp4')

#from matplotlib.pyplot import imshow
#from PIL import Image, ImageDraw

#for frame in container.decode(video=0):
#	if (frame.index == 25):
#		img = frame.to_image()
#		imshow(img)
#frameCount = frame.index - 1
#print(str(frameCount) + "frames")


# Importing all necessary libraries 
import cv2 
import os 
  
# Read the video from specified path 
cam = cv2.VideoCapture("C:\\Users\\saker\\Desktop\\fraud\\5-computer_vision\\2-working-with-images-and-videos\\4_video_basics\\sakvideo.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
