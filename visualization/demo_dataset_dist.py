"""A demo program to draw dataset distribution map (bounding boxes).

Check 'examples/dataset_dist.png' for an example output.

"""
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

height, width = [500, 500]

location_map = np.zeros((height, width))
# load labels
with open('./examples/example_bbox.txt', 'r') as ifile:
    lines = ifile.readlines()
bboxes = np.asarray([[float(j) for j in i.strip().split(' ')] for i in lines])
# print(bboxes)
for i in range(bboxes.shape[0]):
    w = int(bboxes[i, 3] * width)
    h = int(bboxes[i, 4] * height)
    x1 = min(max(int(bboxes[i, 1] * width - w/2), 0), width-1)
    x2 = min(max(int(bboxes[i, 1] * width + w/2), 0), width-1)
    y1 = min(max(int(bboxes[i, 2] * height - h/2), 0), height-1)
    y2 = min(max(int(bboxes[i, 2] * height + h/2), 0), height-1)
    location_map[y1:y2, x1:x2] += 1
location_map = location_map / np.max(location_map)

plt.figure()
ax = plt.gca()
im = ax.imshow(location_map)

# create an axes on the right side of ax. The width of cax will be 5%
# of ax and the padding between cax and ax will be fixed at 0.05 inch.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)

plt.colorbar(im, cax=cax)
plt.tight_layout()
plt.show()

    
