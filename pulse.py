# Code to Takeoff and hold altitude at 15 metres for 5 seconds
from DroneTerminal import Drone
from time import sleep

drone = Drone()

print("Takeoff!")
drone.arm_and_takeoff(15)
sleep(5)
print("RTL!")
drone.rtl()

drone.close_vehicle()

print("Closed!")
