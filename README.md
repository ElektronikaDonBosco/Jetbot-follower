# Jetson Nano Object detection and following

Procedure to make inference in Jetson Nano.

## Set up Jetson Nano

Go to [this](https://jetbot.org/master/) step by step tutorial.

## Install dependecies and download packages

Firs of all we will have to install python dependecies. For that open a terminal an execute the followin commands.

```bash
sudo apt-get install v4l2loopback-dkms
sudo modprobe v4l2loopback
```

```bash
git clone http://github.com/NVIDIA-AI-IOT/jetbot.git
cd jetbot
./scripts/configure_jetson.sh

```

```bash
./scripts/enable_swap.sh
```

```bash
cd docker
./enable.sh $HOME   # we'll use home directory as working directory, set this as you please.
```

```bash
git clone --recursive https://github.com/NVIDIA-AI-IOT/jetbot.git
cd ~/jetbot
sudo python3 setup.py install
```

```bash
python3 -m pip install --upgrade --user pip
python3 -m pip install traitlets setuptools ipywidgets
```

```bash
sudo apt-get install libzmq3-dev
```

```bash
sudo apt-get update
sudo apt-get install git cmake libpython3-dev python3-numpy
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
cd ~/jetson-inference
mkdir build
cd build
cmake ../
make -j2
sudo make install
sudo ldconfig
```

If pytorch is not installed previously

```bash
./install-pytorch.sh
```


## Prepare the docker container

First of all we need to clone the repository of jetson inference and go to the folder jetson_inference.

```bash
cd ~/
git clone https://github.com/mikelalda/Jetbot-follower.git

```

Each time to run the container follow the next steps:

```bash
cd ~/Jetbot-follower
python3 main.py
```

## Run inference

In the file Jetbot-follower/main.py we need to change the line 13 with ESP8266 IP address.

![](assets/2023-05-03_101412.png)

Also the change the wifi of the ESP8266 in line 13 of Arduino code.

![](assets/2023-05-03_101304.png)

Once having done all the steps, run this in the docker terminal.

```bash
cd /Jetbot-follower
python3 main.py
```
