import numpy as np


if __name__ == '__main__':
	np.random.seed(42)
	ax1 = np.arange(6)
	ax2 = np.arange(6)
	print('ax1:\n{}'.format(ax1))
	print('ax2:\n{}'.format(ax2))
	inx1 = np.random.choice(ax1, size=3, replace=False)		# sample without replacement
	inx2 = np.random.choice(ax2, size=3, replace=True)		# sample with replacement
	print('inx1:\n{}'.format(inx1))
	print('inx2:\n{}'.format(inx2))

# ax1:
# [0 1 2 3 4 5]
# ax2:
# [0 1 2 3 4 5]
# inx1:
# [0 1 5]
# inx2:
# [4 4 1]		# Due to replacement, `4` is sampled twice