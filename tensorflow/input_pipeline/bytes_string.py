import tensorflow as tf


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))

def gen_tfrecords():
	'''
	str need to be converted to bytes
	
	'''
	#label_str = 'this is string'	#TypeError: 'this is string' has type str, but expected one of: bytes
	label_bytes = b'this is bytes'
	label_encoded = 'this is bytes'.encode('utf8')
	with tf.python_io.TFRecordWriter('bytes_string.tfrecords') as writer:
		example = tf.train.Example(
            	features=tf.train.Features(
            	feature={
             			#'label_str': _bytes_feature([label_str]),
                    	'label_bytes': _bytes_feature([label_bytes]),
                    	'label_encoded': _bytes_feature([label_encoded])
                    	}))
		writer.write(example.SerializeToString())

def _parser(example):
    features = {
                'label_bytes': tf.FixedLenFeature([], tf.string),
                'label_encoded': tf.FixedLenFeature([], tf.string)
                }
    feats = tf.parse_single_example(example, features)
    return feats['label_bytes'], feats['label_encoded']

def read_tfrecords():
	dt = tf.data.TFRecordDataset('bytes_string.tfrecords')
    dt = dt.map(_parser)
    iteratror = dt.make_one_shot_iterator()
    label_bytes, label_encoded = iteratror.get_next()
    return label_bytes, label_encoded

if __name__ == '__main__':
	gen_tfrecords()
	label_bytes, label_encoded = read_tfrecords()
	sess =  tf.Session()
	label_bytes_, label_encoded_ = sess.run([label_bytes, label_encoded])

	##############################
	# In [25]: label_bytes_
	# Out[25]: b'this is bytes'

	# In [26]: label_encoded_
	# Out[26]: b'this is bytes


	# by the way, python str to bytes via encode('utf8')
	# python bytes to string via decode('utf8')

	# In [23]: a = 'abc'

	# In [24]: a.encode('utf8')
	# Out[24]: b'abc'

	# In [25]: b = _

	# In [26]: b
	# Out[26]: b'abc'

	# In [27]: b.decode('utf8')
	# Out[27]: 'abc'






