import tensorflow as tf
## tensorflow /models/ object_detection / utils/ shape_utils.py

def combined_static_and_dynamic_shape(tensor):
  """Returns a list containing static and dynamic values for the dimensions.

  Returns a list of static and dynamic values for shape dimensions. This is
  useful to preserve static shapes when available in reshape operation.

  Args:
    tensor: A tensor of any type.

  Returns:
    A list of size tensor.shape.ndims containing integers or a scalar tensor.
  """
  static_tensor_shape = tensor.shape.as_list()
  dynamic_tensor_shape = tf.shape(tensor)
  combined_shape = []
  for index, dim in enumerate(static_tensor_shape):
    if dim is not None:
      combined_shape.append(dim)
    else:
      combined_shape.append(dynamic_tensor_shape[index])
  return combined_shape

if __name__ == '__main__':
  tensor = tf.placeholder(dtype=tf.float32, shape=[None, 300, 300, 3])
  combined_shape = combined_static_and_dynamic_shape(tensor)
  print(combined_shape)
  # [<tf.Tensor 'strided_slice:0' shape=() dtype=int32>, 300, 300, 3]
  #                   ^                                    ^   ^   ^
  #                   |                                    |   |   |
  #                   dynamic                                static 

