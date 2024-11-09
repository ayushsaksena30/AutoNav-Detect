## About this Project :
This project leverages the YOLOv4-Tiny algorithm to perform real-time object detection and 
classification for Unmanned Autonomous Vehicles (UAVs). It detects and saves snapshots of identified objects as the UAV navigates its environment.

It detects the following shapes:
Circle, Target, Triangle, Square
   
<div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/85ac43da-ea59-4664-a8b5-caafce8e582a" width="300" height="300" alt="Hotspot 1 -01"/>
    <img src="https://github.com/user-attachments/assets/bc58de67-4782-431e-9ca5-99e7154b96e4" width="300" height="300" alt="Target-02-01"/>
    <img src="https://github.com/user-attachments/assets/a5d0c854-4ad9-4a4c-a5bc-b874d5da1604" width="300" height="300" alt="Shape Detection-02-01"/>
</div>

## Recommended Hardware :
1. Raspberry Pi 4
2. Waveshare OV5640 USB Camera
3. Pixhawk 2.4.8
4. GPS Module

## Prerequisites :
Git clone the repository into a folder
* ```sh
  git clone https://github.com/AFC-IIITDMJ/Aerothon-24.git
  ```
  
Navigate to this folder in a new terminal
* ```sh
  cd Aerothon-24
  ```
  
It is recommended that you create a python virtual environment and install the required libraries using the requirements file
* ```sh
  pip install -r requirements.txt
  ```

## Working with repository files :
### Pulse :
Running this file will arm the UAV and take off to an altitude of 15 meters, hold position for 5 seconds, and then execute an RTL (Return to Launch) command to land.
* ```sh
  python pulse.py
  ```

### Traversal Only :
Running this file will arm the UAV, take off to an altitude of 15 meters, and navigate to each set of coordinates listed in the ground_coordinate.txt file, holding position for 1.5 seconds at each GPS point. To modify the traversal path, edit the coordinates in the ground_coordinate.txt file.
* To edit coordiantes for traversal
  
  ```sh
  sudo nano gound_coordinate.txt
  ```
* To run Traversal file
  
  ```sh
  python traversal.py
  ```

### Detection Only :
Running this file will start YoloV4-Tiny detection on /dev/ttmACM0 port.
* ```sh
  python only_detection.py
  ```

### Pulse.py :
Running this file will arm the UAV and take off to an altitude of 15 meters, hold position for 5 seconds, and then execute an RTL (Return to Launch) command to land.
* ```sh
  python pulse.py
  ```

### Pulse.py :
Running this file will arm the UAV and take off to an altitude of 15 meters, hold position for 5 seconds, and then execute an RTL (Return to Launch) command to land.
* ```sh
  python pulse.py
  ```
