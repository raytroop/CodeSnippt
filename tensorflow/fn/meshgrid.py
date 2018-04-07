import tensorflow as tf
## /home/raytroop/PycharmProjects/models-master/research/object_detection/utils/ops.py

def expanded_shape(orig_shape, start_dim, num_dims):
  """Inserts multiple ones into a shape vector.

  Inserts an all-1 vector of length num_dims at position start_dim into a shape.
  Can be combined with tf.reshape to generalize tf.expand_dims.

  Args:
    orig_shape: the shape into which the all-1 vector is added (int32 vector)
    start_dim: insertion position (int scalar)
    num_dims: length of the inserted all-1 vector (int scalar)
  Returns:
    An int32 vector of length tf.size(orig_shape) + num_dims.
  """
  with tf.name_scope('ExpandedShape'):
    start_dim = tf.expand_dims(start_dim, 0)  # scalar to rank-1
    before = tf.slice(orig_shape, [0], start_dim)
    add_shape = tf.ones(tf.reshape(num_dims, [1]), dtype=tf.int32)
    after = tf.slice(orig_shape, start_dim, [-1])
    new_shape = tf.concat([before, add_shape, after], 0)
    return new_shape

def meshgrid(x, y):
  """Tiles the contents of x and y into a pair of grids.

  Multidimensional analog of numpy.meshgrid, giving the same behavior if x and y
  are vectors. Generally, this will give:

  xgrid(i1, ..., i_m, j_1, ..., j_n) = x(j_1, ..., j_n)
  ygrid(i1, ..., i_m, j_1, ..., j_n) = y(i_1, ..., i_m)

  Keep in mind that the order of the arguments and outputs is reverse relative
  to the order of the indices they go into, done for compatibility with numpy.
  The output tensors have the same shapes.  Specifically:

  xgrid.get_shape() = y.get_shape().concatenate(x.get_shape())
  ygrid.get_shape() = y.get_shape().concatenate(x.get_shape())

  Args:
    x: A tensor of arbitrary shape and rank. xgrid will contain these values
       varying in its last dimensions.
    y: A tensor of arbitrary shape and rank. ygrid will contain these values
       varying in its first dimensions.
  Returns:
    A tuple of tensors (xgrid, ygrid).
  """
  with tf.name_scope('Meshgrid'):
    x = tf.convert_to_tensor(x)
    y = tf.convert_to_tensor(y)
    x_exp_shape = expanded_shape(tf.shape(x), 0, tf.rank(y))
    y_exp_shape = expanded_shape(tf.shape(y), tf.rank(y), tf.rank(x))

    xgrid = tf.tile(tf.reshape(x, x_exp_shape), y_exp_shape)
    ygrid = tf.tile(tf.reshape(y, y_exp_shape), x_exp_shape)
    new_shape = y.get_shape().concatenate(x.get_shape())    # TensorShape concatenate
    xgrid.set_shape(new_shape)
    ygrid.set_shape(new_shape)

    return xgrid, ygrid

if __name__ == '__main__':
  x = tf.constant([1, 2, 3])
  y = tf.constant([1, 2])
  xgrid, ygrid = meshgrid(x, y)
  sess = tf.Session()
  xgrid_, ygrid_ = sess.run([xgrid, ygrid])
  print(xgrid_)
  print(ygrid_)
  # [[1 2 3]
  #  [1 2 3]]
  #
  # [[1 1 1]
  #  [2 2 2]]

  # ref. /home/raytroop/PycharmProjects/models-master/research/object_detection/anchor_generators/grid_anchor_generator.py
  widths_grid, x_centers_grid = meshgrid([0.1, 0.2, 0.5], [[1, 2], [3, 4]])
  widths_grid_, x_centers_grid_ = sess.run([widths_grid, x_centers_grid])
  print(widths_grid_)
  print(x_centers_grid_)
#   [[[ 0.1  0.2  0.5]
#                     [ 0.1  0.2  0.5]]
#
#    [[ 0.1  0.2  0.5]
#                     [ 0.1  0.2  0.5]]]
# 
#
#   [[[1 1 1]
#           [2 2 2]]
#
#    [[3 3 3]
#           [4 4 4]]]