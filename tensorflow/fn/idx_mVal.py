import tensorflow as tf


def idx_mVal(arr):
	"""
	arr : [fk, fk, depth]
	"""
	amax = tf.reduce_max(arr)
	cond = tf.greater_equal(arr, amax)
	idx = tf.where(cond)[0]
	idx_0 = idx[0]
	idx_1 = idx[1]
	idx_2 = idx[2]
	#return tf.slice(arr, begin=idx, size=[1]*3)[0,0, 0]

	return arr[idx_0, idx_1, idx_2]
	
