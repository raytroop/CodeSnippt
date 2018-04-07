import tensorflow as tf
import numpy as np


elems = np.array([1, 2, 3, 4, 5, 6])
squares = tf.map_fn(lambda x: x * x, elems)
# In [8]: squares
# Out[8]: <tf.Tensor 'map_2/TensorArrayStack/TensorArrayGatherV3:0' shape=(6,) dtype=int64>
# squares == [1, 4, 9, 16, 25, 36]

elems = (np.array([1, 2, 3]), np.array([-1, 1, -1]))
alternate = tf.map_fn(lambda x: x[0] * x[1], elems, dtype=tf.int64)
# In [10]: alternate
# Out[10]: <tf.Tensor 'map_3/TensorArrayStack/TensorArrayGatherV3:0' shape=(3,) dtype=int64>
# # alternate == [-1, 2, -3]

elems = np.array([1, 2, 3])
alternates = tf.map_fn(lambda x: (x, -x), elems, dtype=(tf.int64, tf.int64)) # alternates is a tuple consisting of 2 item
# In [12]: alternates
# Out[12]: 
# (<tf.Tensor 'map_4/TensorArrayStack/TensorArrayGatherV3:0' shape=(3,) dtype=int64>,
#  <tf.Tensor 'map_4/TensorArrayStack_1/TensorArrayGatherV3:0' shape=(3,) dtype=int64>)
# alternates[0] == [1, 2, 3]
# alternates[1] == [-1, -2, -3]