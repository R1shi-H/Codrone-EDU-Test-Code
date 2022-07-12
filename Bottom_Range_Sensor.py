from time import sleep
from codrone_edu.drone import *
from codrone_edu.protocol import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

samples = 100
failed_cnt = 0
time_delay_seconds = 0.1


def data_gen(t=0):
    global failed_cnt
    for i in range(samples):
        t = t + time_delay_seconds
        y = drone.get_bottom_range() # get the  height
        if y > 999: # check if the range returns the error value of 999
            failed_cnt = failed_cnt + 1 # add to the count
        print(y, " ,", drone.get_state_data(), " pos ", drone.get_position_data())
        time.sleep(time_delay_seconds)
        yield t, y
    drone.land()
    time.sleep(5)
    plt.close()


def init():
    ax.set_ylim(0, 120.0)
    ax.set_xlim(0, samples*time_delay_seconds)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2 * xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line


try:
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.grid()
    xdata, ydata = [], []

    init_time = time.time()
    drone = Drone()
    drone.pair()
    drone.takeoff()
    ani = animation.FuncAnimation(fig, run, data_gen, blit=False, repeat=False, init_func=init)
    plt.show()
    print("done")

finally:
    drone.close()
    print("failed counter ", failed_cnt / samples * 100, " %")
    print("A perfect floor will have 0% drops")
    print("Anything greater than 10% is not great.")