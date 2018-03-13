import numpy as np

xmin = []
ymin = []
xmax = []
ymax = []
bboxes = np.reshape(np.arange(12), [-1, 4]).tolist()
for b in bboxes:
	assert len(b) == 4
	[l.append(point) for l, point in zip([ymin, xmin, ymax, xmax], b)]
	# here [ymin, xmin, ymax, xmax] shape is same with b == 4
	
# In [34]: xmax
# Out[34]: [3, 7, 11]

# In [35]: xmin
# Out[35]: [1, 5, 9]

# In [36]: xmin
# Out[36]: [1, 5, 9]

# In [37]: ymin
# Out[37]: [0, 4, 8]

# In [38]: xmax
# Out[38]: [3, 7, 11]

# In [39]: ymax
# Out[39]: [2, 6, 10]
