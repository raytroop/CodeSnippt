import tensorflow as tf


def num_boxes(tensor):
  """Returns number of boxes held in collection.

  This number is inferred at `run-time`.

  Returns:
    a tensor representing the number of boxes held in the collection.
  """
  return tf.shape(tensor)[0]  # tensor

def num_boxes_static(tensor):
  """Returns number of boxes held in collection.

  This number is inferred at `graph construction time` rather than run-time.

  Returns:
    Number of boxes held in collection (integer) or None if this is not
      inferrable at graph construction time.
  """
  return tensor.get_shape()[0].value  # int

if __name__ == '__main__':
  # TensorShape
  ax =  tf.placeholder(dtype=tf.float32, shape=[None, 300, 300, 3])
  print(ax.shape.is_fully_defined())
  # False

  # In [4]: ax.shape[0]
  # Out[4]: Dimension(None)

  # In [5]: type(ax.shape[0])
  # Out[5]: tensorflow.python.framework.tensor_shape.Dimension

  # In [6]: ax.shape
  # Out[6]: TensorShape([Dimension(None), Dimension(300), Dimension(300), Dimension(3)])

  # In [8]: ax.shape[1].value   # Dimension to int
  # Out[8]: 300

  # In [10]: ax.shape.as_list()   # TensorShape to list
  # Out[10]: [None, 300, 300, 3]