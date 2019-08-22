#!/usr/bin/env python

import time
import os
import sys
import shutil
import picamera

def main_unit():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        while True:
            camera.capture('/home/pi/picture/picture.jpg')
            shutil.copy('/home/pi/picture/picture.jpg', '/home/pi/iot/picture.jpg')

def daemonize():
    pid = os.fork()
    if pid > 0:
        pid_file = open('/var/run/camera_daemon.pid','w')
        pid_file.write(str(pid)+"\n")
        pid_file.close()
        sys.exit()
    if pid == 0:
        main_unit()

if __name__ == '__main__':
    while True:
        daemonize()

