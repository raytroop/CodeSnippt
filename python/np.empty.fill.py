import numpy as np
# we can use np.empty with np.fill to construct feature map

# py-faster-rcnn/lib/rpn/anchor_target_layer.py
def _unmap(data, count, inds, fill=0):
    """ Unmap a subset of item (data) back to the original set of items (of
    size count) """
    if len(data.shape) == 1:
        ret = np.empty((count, ), dtype=np.float32)
        ret.fill(fill)
        ret[inds] = data
    else:
        ret = np.empty((count, ) + data.shape[1:], dtype=np.float32)
        ret.fill(fill)
        ret[inds, :] = data
    return ret

if __name__ == '__main__':
	data = np.arange(6).reshape([3, 2])
	print(data)
	count = 13
	inds = np.array([0, 5, 9])
	print(inds)
	fill = 0
	ret = _unmap(data, count, inds, fill)
	print(ret)
# [[0 1]
#  [2 3]
#  [4 5]]

# [0 5 9]

# [[0. 1.]
#  [0. 0.]
#  [0. 0.]
#  [0. 0.]
#  [0. 0.]
#  [2. 3.]
#  [0. 0.]
#  [0. 0.]
#  [0. 0.]
#  [4. 5.]
#  [0. 0.]
#  [0. 0.]
#  [0. 0.]]