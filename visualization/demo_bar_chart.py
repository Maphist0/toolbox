"""A demo program to draw bar chart.

Check 'examples/bar_chart.png' for an example output.

"""
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
n_groups    = 4
means_a     = (10, 10, 1, 1.5)
std_a       = (0.2, 0.2, 0.4, 0.8)
means_b     = (14, 6, 0.5, 0.25)
std_b       = (0.1, 0.6, 0.1, 0.1)

# create plot
fig, ax     = plt.subplots()
index       = np.arange(n_groups)
bar_width   = 0.35
opacity     = 0.8

# draw the first set of bars
rects1 = plt.bar(
    index,
    means_a,
    bar_width,
    alpha=opacity,
    color='b',
    label='Case a',
    yerr=std_a
)

# draw the second set of bars
rects2 = plt.bar(
    index + bar_width,  # Pad by bar_width
    means_b,
    bar_width,
    alpha=opacity,
    color='g',
    label='Case b',
    yerr=std_b
)

# put labels
plt.xlabel('Runs')
plt.ylabel('Value')
plt.xticks(index + bar_width/2, ('Run a', 'Run b', 'Run c', 'Run d'))
plt.legend()

# draw std small line
for rect, means, std in [(rects1, means_a, std_a), (rects2, means_b, std_b)]:
    for i, rectangle in enumerate(rect):
        height = rectangle.get_height()
        plt.text(
            rectangle.get_x() + rectangle.get_width()/2,
            height + std[i],
            '$\mu$=%.3f \n $\sigma$=%.3f' % (means[i], std[i]),
            size='smaller',
            ha='center',
            va='bottom'
        )

# set y and x limit
plt.ylim(top=16)
# plt.xlim()

# set layout
plt.tight_layout()
plt.show()
