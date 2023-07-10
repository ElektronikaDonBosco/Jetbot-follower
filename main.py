import argparse
import socket
import jetson_inference
import jetson_utils
import additionals.globals as gv

import urllib.request
import http
import numpy as np
import cv2
from jetbot import Robot

base = "http://192.168.1.47/" # Arduino prints the IP of the ESP8266


def transfer():   #use to send and receive data
    try:
        n = urllib.request.urlopen(base).read()
        n = n.decode("utf-8")
        return n

    except http.client.HTTPException as e:
        print(n)
        print("Error")
        return e


def detection_center(detection):
    """Computes the center x, y coordinates of the object"""
    bbox = detection['bbox']
    center_x = (bbox[0] + bbox[2]) / 2.0 - 0.5
    center_y = (bbox[1] + bbox[3]) / 2.0 - 0.5
    return (center_x, center_y)

net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson_utils.videoSource("csi://0")      # '/dev/video0' for V4L2 and 'csi://0' for csi
# display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file
# render_img = False
robot = Robot()

speed = 0.5
turn_gain = 0.8

names = ['person']

def main():

    while True:
        color = transfer()
        print(type(color))
        # check = False
        # img = camera.Capture()
        # if img != None:
        #     height, width, channels = img.shape
        #     detections = net.Detect(img)
        #     # if render_img:
        #     #     display.Render(img)
        #     #     display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        #     for detection in detections:
        #         class_id = detection.ClassID
        #         x1 = detection.Left/width 
        #         y1 = detection.Top/height
        #         x2 = detection.Right/width
        #         y2 = detection.Bottom/height
        #         if class_id == 1:
        #             color = transfer("/get_color")
        #             print(type(color))
        #             # Si la persona detectada tiene algo verde
        #             if color == "/1":
        #                 check = True
        #                 lower = np.array([0, 0, 330], np.uint8)
        #                 upper = np.array([180, 255, 30], np.uint8)
        #                 break
        #             # Si la persona detectada tiene algo rojo
        #             elif color == "/2":
        #                 check = True
        #                 lower = np.array([0, 0, 90], np.uint8)
        #                 upper = np.array([180, 255, 150], np.uint8)
        #                 break
        #             # Si la persona detectada tiene algo azul
        #             elif color == "/3":
        #                 check = True
        #                 lower = np.array([0, 0, 210], np.uint8)
        #                 upper = np.array([180, 255, 270], np.uint8)
        #                 break
        #             else:
        #                 check = False
        #     print(check)
        #     if check:
        #         cropped_img = img[y1:y2, x1:x2,:]
        #         hsv = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)
        #         mask = cv2.inRange(hsv, lower, upper)
        #         mask_on_counts = np.sum(mask==255)
        #         print("mask_on_counts: {}".format(mask_on_counts))
        #         if mask_on_counts >= 30:
        #             center = detection_center(detection)
        #             robot.set_motors(
        #                 float(speed + turn_gain * center[0]),
        #                 float(speed - turn_gain * center[0])
        #             )
        #         else:
        #             robot.set_motors(0,0)
                    
            
    
if __name__ == '__main__':
    main()
