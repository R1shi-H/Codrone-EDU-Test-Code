#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()
try:
    drone.takeoff()
    drone.reset_trim()
    drone.sendControl(0, 30, 0, 0)
    time.sleep(2)
    if drone.detect_wall(500):
        drone.reset_trim()
        drone.set_throttle (40)
        drone.move(.6)
        drone.hover(.6)
        drone.reset_trim()
        drone.set_pitch(30)
        drone.move(.7)
        drone.land()
finally:
    drone.land()
    drone.close()