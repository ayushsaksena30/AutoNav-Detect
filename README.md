## About this Project :
This project leverages the YOLOv4-Tiny algorithm to perform real-time object detection and 
classification for Unmanned Autonomous Vehicles (UAVs). It detects and saves snapshots of identified objects as the UAV navigates its environment.

It detects the following shapes:
Circle, Target, Triangle, Square
   
<div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/85ac43da-ea59-4664-a8b5-caafce8e582a" width="200" height="200" alt="Hotspot 1 -01"/>
    <img src="https://github.com/user-attachments/assets/4d24b317-bdb7-4923-97bd-ef2647719b62" width="200" height="200" alt="Target-02-01"/>
    <img src="https://github.com/user-attachments/assets/a5d0c854-4ad9-4a4c-a5bc-b874d5da1604" width="200" height="200" alt="Shape Detection-02-01"/>
</div>

## Features :
* Runs completely on on-board computer of UAV
* Yolo-V4 Tiny model is optimised to give 20 fps on used hardware.
* On detecting objects of interest, the model automatically saves the snapshot of the frame in local directory along with time stamp and GPS coordiantes.
* Provides full control over Traversal of the drone both Manually (using keyboard) and Autonomously.

## Recommended Hardware :
* Raspberry Pi 5
* Waveshare OV5640 USB Camera
* Pixhawk 2.4.8
* GPS Module

## Prerequisites :
Git clone the repository into a folder
* ```sh
  git clone https://github.com/AFC-IIITDMJ/Aerothon-24.git
  ```
  
Navigate to this folder in a new terminal
* ```sh
  cd Aerothon-24
  ```
  
**It is recommended that you create a python virtual environment and install the required libraries using the requirements file**
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
Running this file will start YoloV4-Tiny detection on /dev/ttmACM0 port. You can also enter custom Connection String in Drone class.
* ```sh
  python only_detection.py
  ```

### Detection and Traversal Both :
Running this file will arm the UAV and take off to an altitude of 15 meters, hold position for 5 seconds, and then execute an RTL (Return to Launch) command to land.
* ```sh
  python detection_traversal.py
  ```

### Navigation using Keyboard :
Running this file will arm the UAV and take off to an altitude of 15 meters, hold position for 5 seconds, and then use commands from keyboard to run traverse.
Up arrow key moves it forward and so on. All commands are executed for duration of 1 second.
* ```sh
  python keyboard.py
  ```

Made with ❤️ by [Ayush](https://github.com/ayushsaksena30), [Shashank](), [Sumit](), [Siddharth]()
