"""A demo program to draw line chart.

Check 'examples/line_chart.png' for an example output.

"""
import os
import csv
import numpy as np
import matplotlib.pyplot as plt

from process_data import *

# Some test data
data = load_csv_data('./examples/example.csv')
# only set 1 if raw data is 1, otherwise 0
data = [1 if float(i) == 1 else 0 for i in data]

# The format of lines
line_styles = ['-', '--', '-.', ':', (0, (8, 1))]

# Different types of averaging
convolve_interval = 200
avg_from_start = average_from_start(data)[:-1 * convolve_interval]
running_avg = running_average(data, interval=50)
smoothen_running_avg_x, smoothen_running_avg_y = smoothen_line(convolve_line(running_avg, interval=convolve_interval))
running_avg = running_avg[:-1 * convolve_interval]

# Plot all lines
p = plt.plot(
    avg_from_start,
    label='Average from start',
    linestyle=line_styles[0]
)
# Add running average
p = plt.plot(
    running_avg,
    label='Running avg',
    alpha=0.5,
    linestyle=line_styles[1]
)
color = p[-1].get_color()
# Add smooth line
p = plt.plot(
    smoothen_running_avg_x,
    smoothen_running_avg_y,
    color=color,
    label='Smoothen running avg',
    # linestyle=line_styles[2]
)

plt.title('Some title')
plt.xlabel('Time', horizontalalignment='right', x=1.0)
plt.ylabel('Ratio')
# plt.legend(loc='best', fontsize='small')
plt.legend(loc='best')

plt.tight_layout()
plt.show()