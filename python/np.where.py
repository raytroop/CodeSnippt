import numpy as np


if __name__ == '__main__':
	np.random.seed(365)
	ax = np.random.randint(low=0, high=2, size=[6, 4])
	idx = np.where(ax==1)
	print(ax)
	print(idx)

# [[0 0 1 1]
#  [0 1 0 0]
#  [1 0 0 0]
#  [0 0 1 1]
#  [0 1 1 1]
#  [1 0 0 1]]
# (array([0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 5]), 
#  array([2, 3, 1, 0, 2, 3, 1, 2, 3, 0, 3]))
# np.where throw inx first through row by row