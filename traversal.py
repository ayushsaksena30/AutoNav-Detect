# Code to Traverse ground using GPS coordiantes from txt file
from DroneTerminal import Drone
from time import sleep

drone = Drone()

drone.arm_and_takeoff(15)

with open('ground_coordinate.txt', 'r') as file:
    for line in file:
        data_list = [float(x.strip()) for x in line.split()]
        coord = tuple(data_list)
        
        drone.hover_gps(coord)
        print("Reached location : ", coord)
        sleep(1.5)

print("RTL!")
drone.rtl()
drone.close_vehicle()