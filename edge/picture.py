#!/usr/bin/env python

import shutil
import time
import picamera
 
with picamera.PiCamera() as camera:
 camera.resolution = (1024, 768)
 camera.start_preview()
 # Camera warm-up time
 time.sleep(2)
 while True:
  camera.capture('./picture/picture.jpg')
  shutil.copy('./picture/picture.jpg', './iot/picture.jpg')
