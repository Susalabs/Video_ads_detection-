import cv2 as cv, os, numpy as np
from datetime import datetime, timedelta

base_dir = "E:\\Intern Projects\\OpenCV\\Add Detection\\"

addNames, initialFrames, lastFrames, timings = [], [], [], []
totalTimeAdd = (datetime.now()-datetime.now())

def CaptureFrames():
   i = 1
   while True:

      if not os.path.exists(base_dir+"data\\initial-frames\\First-Frame"+str(i)+".jpg"):
         break

      initialFrame = cv.imread(base_dir+"data\\initial-frames\\First-Frame"+str(i)+".jpg")
      lastFrame = cv.imread(base_dir+"data\\last-frames\\Last-Frame"+str(i)+".jpg")
      
      initialFrame = cv.cvtColor(initialFrame, cv.COLOR_BGR2GRAY)
      lastFrame = cv.cvtColor(lastFrame, cv.COLOR_BGR2GRAY)
      
      initialFrames.append(initialFrame)
      lastFrames.append(lastFrame)
         
      i += 1

   print("initialFrames loaded Successfully")
   print("lastFrames loaded Successfully")
         
def CaptureTimingsNames():
   f = open(base_dir+"data\\timings.txt", "r")
   data = f.readlines()
   f.close()
   for line in data:
      subData = line.split(" -> ")
      addNames.append(subData[0])
      timings.append(subData[1][:-1])
   print("timings loaded Successfully : ", timings)
   print("addNames : ", addNames)

def Compare(img1, img2):
   h, w = img1.shape
   diff = cv.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

def startLiveStream():
   app = cv.VideoCapture(base_dir+"livestream\\LiveStream.mp4")
   flag, totalTimeAdd, startTime = False, 0, 0
   while app.isOpened():
      ret, frame = app.read()
      frames = app.get(cv.CAP_PROP_FRAME_COUNT)
      timestamps = app.get(cv.CAP_PROP_POS_MSEC)
      fps = app.get(cv.CAP_PROP_FPS)

      if ret:
         cv.imshow('Output', frame)
         currentFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
         if not flag:
            min_error, mindiff, ind = float('inf'), float('inf'), 0
            for i in range(len(initialFrames)):
               error, diff = Compare(initialFrames[i], currentFrame)
               if min_error > error:
                  min_error = error
                  mindiff = diff
                  ind = i
            if min_error <= 1:
               flag = True
               startTime = app.get(cv.CAP_PROP_POS_MSEC)
               print(addNames[ind] + " Ad Started at : " + str(timedelta(seconds=startTime/1000)))
         else:
            min_error, mindiff, ind = float('inf'), float('inf'), 0
            for i in range(len(lastFrames)):
               error, diff = Compare(lastFrames[i], currentFrame)
               if min_error > error:
                  min_error = error
                  mindiff = diff
                  ind = i
            if min_error <= 1:
               flag = False
               print(addNames[ind] + " Ad Ended at : " + str(timedelta(seconds=(app.get(cv.CAP_PROP_POS_MSEC)+100)/1000)))
               print(addNames[ind] + " Ad took : ", timedelta(seconds=(app.get(cv.CAP_PROP_POS_MSEC)-startTime)/1000)+timedelta(seconds=0.1))
               totalTimeAdd += app.get(cv.CAP_PROP_POS_MSEC)-startTime + 100
               print("\nTotal Ad Time :", timedelta(seconds=totalTimeAdd/1000),"\n")
         
         if cv.waitKey(1) & 0xFF == ord('q'):
            break
      else: 
         break
  
   print("--> Live Stream Ended....\n")
   print("Final Total Ad Time In Live Stream : ", timedelta(seconds=totalTimeAdd/1000))
   print ("\n### PROGRAM EXITED ###\n");

   app.release()
   cv.destroyAllWindows()

print("\n### AD DETECTION USING MSE ERROR BETWEEN FRAMES ###")
print("--> Capturing Ad Frames... ")
CaptureFrames()
print("All Ad Frames Captured Successfully")

print('\n--> Capturing Timings and Names of AD... ')
CaptureTimingsNames()
print("All Ad Timings and Captured Successfully")
print("\n### ALL REQUIRED DATA LOADED UP :-) ###\n")

print("Starting Live Stream....")
print("--> Started...\n")
startLiveStream()
