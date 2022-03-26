import cv2
import cv2.aruco as aruco
import numpy as np
import time
# import Check
# from mover import receiver

vid = cv2.VideoCapture(0)


def process(id=id):

    if id==1:
        print("Forward")
    elif id==2:
        print("Back")
    elif id==3:
        print("Left")
    elif id==4:
        print("Right")

while(True):
    # Check.My_Function(' ')
    ret, frame = vid.read()

    #frame=cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if len(corners)==0:
        print("Waiting for Marker... <<BOT STOPPED>>",end="\r")
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue
    # vid.release()

    if len(corners)>1:
        print("More than one corner detected. Going with the first",end="\r")
    c = corners[0][0]
        
    y,x,_=frame.shape
    print(c[:,0].mean())
    
    print("Located at ({},{}) ARUCO_ID {} of ({},{})".format(c[:, 0].mean(),c[:, 1].mean(),ids[0],x,y))

    frame=cv2.rectangle(frame, (int(c[0][0]),int(c[0][1])), (int(c[2][0]),int(c[2][1])), (255,255,0), 2)
    # frame = cv2.putText(frame, str(ids[0]), (c[:, 0].mean(),c[:, 1].mean()), cv2.FONT_HERSHEY_SIMPLEX,
    #                1, (255,0,0), 2, cv2.LINE_AA)
    cv2.imshow("Frame",frame)
    box_area=np.abs(c[0][0]-c[0][1])*np.abs(c[2][0]-c[2][1])
    frame_area=frame.shape[1]*frame.shape[0]

######################################   
    if ids[0]==[1]:
        print("<<F>>")

        # receiver(2)
    elif ids[0]==[2]:
        print("<<B>>")
        # receiver(1)
    elif ids[0]==[3]:
        print("<<L>>")
        # receiver(3)
    elif ids[0]==[4]:
        print("<<R>>")
        # receiver(4)
    else:
        print("Pattern not detected!!")
        Check.My_Function(1)
    
    # time.sleep(0.1)
    # receiver(5)
########################################
    # if (box_area/frame_area)>=0.05:
    #     print("\nARUCO too close {:.4f}. <<Move BOT>>".format(box_area/frame_area))
    #     process(id=ids[0])
    #     time.sleep(0.3)
    # vid = cv2.VideoCapture(0)#'http://192.168.0.7:81/stream')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    # plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
vid.release()

cv2.destroyAllWindows()
