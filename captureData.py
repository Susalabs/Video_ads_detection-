import os, time, cv2 as cv, math
from datetime import datetime, timedelta

base_dir = "E:\\Intern Projects\\OpenCV\\Add Detection\\"
open(base_dir+"data\\timings.txt",'w').close()
            
def Capture():
        i = 1
        while True:

            if not os.path.exists(base_dir+"ads\\ad"+str(i)+".mp4"):
                break
            
            app = cv.VideoCapture(base_dir+"ads\\ad"+str(i)+".mp4")
            frames = app.get(cv.CAP_PROP_FRAME_COUNT)
            fps = app.get(cv.CAP_PROP_FPS)
            flag,Frame = True,0
            start = datetime.now()

            while( app.isOpened() ):
                ret, frame = app.read()

                if ret:
                    cv.imshow('Output', frame)
                    
                    if flag:
                        cv.imwrite(base_dir+"data\\initial-frames\\First-Frame"+str(i)+".jpg", frame)
                        print("Ad "+ str(i) + " INITIAL FRAME Captured Successfully")
                        flag = False
                    if cv.waitKey(2) & 0xFF == ord('q'):
                        break
                    Frame = frame
                else:
                    cv.imwrite(base_dir+"data\\last-frames\\Last-Frame"+str(i)+".jpg", Frame)
                    break

            second = frames/fps
            f = open(base_dir+"data\\timings.txt",'a')
            f.write("Add"+str(i)+"_Name -> " + str((timedelta(seconds=second))) + "\n")
            f.close()

            app.release()
            cv.destroyAllWindows()

            print("Ad "+ str(i) + " LAST FRAME Captured Successfully")

            i += 1

print("\n### ADS INITIAL-LAST FRAMES CAPTURING STARTED ###\n--> Starting now....")
Capture()
print("--> Ending Process...\n### ALL ADS FRAMES WERE CAPTURED SUCCESSFULLY ###\n")
