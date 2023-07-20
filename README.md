Before starting with the description of the project, we would like to thanks MikelAlda for the help given during the project development.

# Jetson Nano Object detection and following

In this project we will use a Jetbot (which has a Jatson nano inside) to detect different objects and to follow them. The Jetbot will detect and follow dogs, cats and people.
We will use a NodeMCU with three switched to indicate the object to follow, that way, when we activate the "people" switch it will start detecting and following people. The comunicaton between the Jetbot and the NodeMCU will be throught a WI-Fi connection.

## Material used in the project
- Jetbot

- ESP826MOD Sensor module (NodeMCU)

- Switches and resistors


Procedure to make inference in Jetson Nano.

## Set up Jetson Nano

Go to [this](https://jetbot.org/master/) step by step tutorial with [this](https://drive.google.com/file/d/1G5nw0o3Q6E08xZM99ZfzQAe7-qAXxzHN/view) image.

## Install dependecies and download packages

Firs of all we will have to go to notebooks and follow this tutorial for download the file [ssd_mobilenet_v2_coco.engine](https://drive.google.com/file/d/1RnNBHPDphIOWwHCSfeMCWQ7XN3w3tKFD/view) or copy from this repo. After that copy the notebooks and the file downloaded in the folder you copied the engine file and run the notebooks.

If anyone wants to see the labels, check [this](https://github.com/tensorflow/models/blob/master/research/object_detection/data/mscoco_complete_label_map.pbtxt) site.

## Run inference

In the file Jetbot-follower/main.py we need to change the line 13 with ESP8266 IP address.

![](assets/2023-05-03_101412.png)

Also the change the wifi of the ESP8266 in line 13 of Arduino code.

![](assets/2023-05-03_101304.png)
