import csv
from time import time

import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Your serial port might be different!
ser = serial.Serial('/dev/ttyACM0', timeout=1)

f = open("df.csv", "a+")
writer = csv.writer(f, delimiter=',')

def init():
    line.set_data(x[:2],y[:2])
    return line,

def animate(i):
    i = min(i, x.size)
    xdata = x[:i]
    ydata = y[:i]
    line.set_data(xdata, ydata)
    ax.relim()
    ax.autoscale()
    return line,


while True:
    s = ser.readline().decode()
    if s != "" and s != " ":
        rows = [float(x) for x in s.split(',')]
        # Insert local time to list's first position
        rows.insert(0, int(time())-1645337038)
        print(rows)
        writer.writerow(rows)
        
        y = np.array(rows[1])
        x = np.arange(rows[0])

        fig, ax = plt.subplots()
        line, = ax.plot([], [], '.')
        ax.margins(0.05)


        anim = animation.FuncAnimation(fig, animate, init_func=init, interval=25)

        plt.show()


        f.flush()

