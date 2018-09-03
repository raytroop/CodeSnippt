# https://stackoverflow.com/a/41917296/8037585
import tensorflow as tf
from tensorflow.python import pywrap_tensorflow  # pylint: disable-msg=E0611

checkpoint_path = tf.train.latest_checkpoint('saved_models')
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()

for key in var_to_shape_map:
    print("tensor_name: ", key)
    print(reader.get_tensor(key))

# output:
# tensor_name:  batch_normalization/moving_mean
# [0. 0. 0.]
# tensor_name:  batch_normalization/moving_variance
# [1. 1. 1.]
# tensor_name:  batch_normalization/gamma
# [1. 1. 1.]
# tensor_name:  batch_normalization/beta
# [0. 0. 0.]
