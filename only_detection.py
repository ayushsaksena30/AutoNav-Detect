# Code to run detection by YoloV4-tiny to detect Hotspots and Target
import numpy as np
import cv2
from DroneTerminal import Drone
from time import sleep
import threading
from datetime import datetime
import os

drone = Drone()
drone.speed(3)
altitude = 15
hotspot=0

net = cv2.dnn.readNet("v4 tiny custom/yolov4-tiny-custom_best.weights", "v4 tiny custom/yolov4-tiny-custom.cfg")
with open("v4 tiny custom/obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

def take_snapshot(frame, coords):
    snapshot_dir = 'snapshots'
    x, y = coords
    text_coords = f"Coords: {x},{y}"
    cv2.putText(frame, text_coords, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
    
    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S:%f")[:-3]

    text_time = f"Time: {timestamp}"
    cv2.putText(frame, text_time, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    os.makedirs(snapshot_dir, exist_ok=True)
    snapshot_path = os.path.join(snapshot_dir, f'snapshot_{timestamp}.png')
    cv2.imwrite(snapshot_path, frame)
    print(f"Snapshot taken and saved at: {snapshot_path}")

def camera(args=None):
    global hotspot
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break
        
        frame = cv2.resize(frame, (320, 320))
        height, width, channels = frame.shape

        center_frame_x = width // 2
        center_frame_y = height // 2

        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (320, 320), (0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)

        detections = net.forward(output_layers)
        
        class_ids = []
        confidences = []
        boxes = []

        for output in detections:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > 0.3:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        # Apply Non-Maximum Suppression to filter the boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.3, nms_threshold=0.4)  # Adjusted Thresholds

        if len(indices) > 0:
            for i in indices.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = confidences[i]
                color = (0, 255, 0)

                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

                if center_y >= center_frame_y - 10 and center_y <= center_frame_y + 10:
                    if(label == 'hotspot'):
                        hotspot+=1
                        print('Hotspot detected. Count : ',hotspot)
                    
                    coords = drone.get_gps_coords()
                    take_snapshot(frame,coords)
                    sleep(1.5)

        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

t1 = threading.Thread(target=camera)

t1.start()
t1.join()