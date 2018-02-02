import numpy as np
import tensorflow as tf

## write tfrecords file
ax = np.arange(18).reshape([9, 2]).astype(np.uint8)

def _bytes_feature(value):
	return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

with tf.python_io.TFRecordWriter('test.tfrecords') as writer:
	for ix1, ix2 in zip([0, 2, 5], [2, 5, 9]):
		raw_data = ax[ix1:ix2].tostring()
		example = tf.train.Example(
              			features=tf.train.Features(
                          		feature={'raw_data': _bytes_feature(raw_data)}))
		writer.write(example.SerializeToString())


## read tfrecords file
def parser(record):
	keys_to_features={'raw_data': tf.FixedLenFeature((), tf.string)}
	parsed = tf.parse_single_example(record, keys_to_features)
	image = tf.decode_raw(parsed['raw_data'], tf.uint8)
	image = tf.reshape(image, [-1, 2])
	return image


dt = tf.data.TFRecordDataset('test.tfrecords')
dt = dt.map(parser)
iterator = dt.make_one_shot_iterator()
next_item = iterator.get_next()

try:                                                
	while True:                                                  
		print(sess.run(next_item))
		print('\n')                         
	except tf.errors.OutOfRangeError:                    
		print('Done') 


## [[0 1]
## 	[2 3]]


## [[4 5]
##  [6 7]
##  [8 9]]


## [[10 11]
##  [12 13]
##  [14 15]
##  [16 17]]


# Done
