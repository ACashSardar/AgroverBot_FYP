# import the necessary packages
from imutils import build_montages
from datetime import datetime
import numpy as np
import imagezmq
import argparse
import imutils
import cv2
# construct the argument parser and parse the arguments

imageHub = imagezmq.ImageHub()

while True:
    (rpiName, frame) = imageHub.recv_image()
    imageHub.send_reply(b'OK')
    
    frame = imutils.resize(frame, width=400)
    
    
    cv2.imshow("Frame",frame)

    i=cv2.waitKey(1)
    if i==ord("q"):
        break