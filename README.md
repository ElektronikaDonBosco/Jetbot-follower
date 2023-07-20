Before starting with the description of the project, we would like to thanks MikelAlda for the help given during the project development.

# Jetson Nano Object detection and following

In this project we will use a Jetbot (which has a Jatson nano inside) to detect different objects and to follow them. The Jetbot will detect and follow dogs, cats and people.
We will use a NodeMCU with three switched to indicate the object to follow, that way, when we activate the "people" switch it will start detecting and following people. The comunicaton between the Jetbot and the NodeMCU will be throught a WI-Fi connection.

## Material used in the project
- Jetbot

- ESP826MOD Sensor module (NodeMCU)

- Switches and resistors

## -ESP826MOD (NodeMCU) Sensor Module Schematic Pinout
<img src="https://github.com/ElektronikaDonBosco/Blind-eye/blob/master/60893535def1e6e04c6f55b835bcd917.jpg" width=50% height=50%>

## Set up Jetson Nano

Go to [this](https://jetbot.org/master/) step by step tutorial to understand the Jetbot.

We used this image of the Operating System to make [this](https://drive.google.com/file/d/1G5nw0o3Q6E08xZM99ZfzQAe7-qAXxzHN/view) project. The owner of this image is the manufacturer of the Jetbot.

## Install dependecies and download packages

Turn on the Jetbot and it will show its IP in the display. Write that IP followed by ":8888" in a web browser. That way you will be able to see the folders of the Jetbot.

Download the files of this repository to a folder of the Jetbot. Coco file was copied from [ssd_mobilenet_v2_coco.engine](https://drive.google.com/file/d/1RnNBHPDphIOWwHCSfeMCWQ7XN3w3tKFD/view) 

If anyone wants to see the labels of the detected objetcs, check [this](https://github.com/tensorflow/models/blob/master/research/object_detection/data/mscoco_complete_label_map.pbtxt) site.

## Run inference

1 - The NodeMCU must connect to the Wi-Fi to get information from the jetson nano. We must set the Wi-Fi network and the password of the network in the NodeMCU code. It will be necessary to change the Wi-Fi of the ESP8266 (NodeMCU) in line 13 of the code. You have that code inside the folder "Arduino". When you transfer the program to the NodeMCU device it will send the IP in the serie port, if you open the SerialMonitor you will see the IP. It is neccessary to know the IP in the next point.

![](assets/2023-05-03_101304.png)

2 - Turn on the Jetbot and it will show its IP in the display. Write that IP followed by ":8888" in a web browser. It will ask for the password, the default password is "jetbot".

3 - In the file "live_demo_labels.ipynb", we need to set the ESP8266 (NodeMCU) IP address. The jetson nano must know the IP address of the NodeMCU, and it is set in the function named "transfer".
In that function there is code to enter the IP of the NodeMCU.

![irudia](https://github.com/ElektronikaDonBosco/Jetbot-follower/assets/45638976/da58e3e2-133a-4bb8-9ce2-c05ddb0003f0)


In the file Jetbot-follower/main.py we need to change the line 13 with ESP8266 IP address.

![](assets/2023-05-03_101412.png)

Also the change the wifi of the ESP8266 in line 13 of Arduino code.

![](assets/2023-05-03_101304.png)
