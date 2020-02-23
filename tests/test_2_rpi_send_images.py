"""test_2_rpi_send_images.py -- send PiCamera image stream.

A Raspberry Pi test program that uses imagezmq to send image frames from the
PiCamera continuously to a receiving program on a Mac that will display the
images as a video stream.

This program requires that the image receiving program be running first. Brief
test instructions are in that program: test_2_mac_receive_images.py.
"""

import sys

import socket
import time
import cv2
from imutils.video import VideoStream
import imagezmq

# use either of the formats below to specifiy address of display computer
# sender = imagezmq.ImageSender(connect_to='tcp://jeff-macbook:5555')
# Alden's MacBook
sender = imagezmq.ImageSender(connect_to='tcp://10.10.65.247:5555')

rpi_name = socket.gethostname()  # send RPi hostname with each image
cam = cv2.VideoCapture(0)
time.sleep(2.0)  # allow camera sensor to warm up

while True:  # send images as stream until Ctrl-C
    retval, image = cam.read()
    sender.send_image(rpi_name, image)
