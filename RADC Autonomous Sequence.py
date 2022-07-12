from codrone_edu.drone import *
from codrone_edu.protocol import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


drone = Drone()
drone.pair()
drone.takeoff()
drone.reset_trim()
drone.set_throttle(-40)
drone.move(1.5)
drone.set_pitch(50)
drone.move(.6)
drone.hover(2)
time.sleep(1)
drone.set_pitch(50)
drone.move(.2)
drone.hover(1)
drone.set_pitch(-50)
drone.move(.5)
drone.land()
drone.close()