## About this Project :
This project leverages the YOLOv4-Tiny algorithm to perform real-time object detection and 
classification for Unmanned Autonomous Vehicles (UAVs). It detects and saves snapshots of identified objects as the UAV navigates its environment.
It detects the following shapes:
1. Circle
2. Target
3. Triangle
4. Square
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
It is recommended that you create a python virtual environment and install the required libraries using the requirements file:
* ```sh
  pip install -r requirements.txt
  ```
