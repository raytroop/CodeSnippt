import tensorflow as tf


label_map = {'aeroplane': 1,
 			'bicycle': 2,
 			'bird': 3,
 			'boat': 4,
 			'bottle': 5,
 			'bus': 6,
 			'car': 7,
 			'cat': 8,
 			'chair': 9,
 			'cow': 10,
 			'diningtable': 11,
			'dog': 12,
			'horse': 13,
			'motorbike': 14,
			'person': 15,
			'pottedplant': 16,
			'sheep': 17,
			'sofa': 18,
			'train': 19,
			'tvmonitor': 20}
table = tf.contrib.lookup.HashTable(
          initializer=tf.contrib.lookup.KeyValueTensorInitializer(
              keys=tf.constant(list(label_map.keys())), # keys type is tf.string
              values=tf.constant(list(label_map.values()), dtype=tf.int64)),
          default_value=-1)		# default_value: The value to use if a key is missing in the table.
# tf.constant(list(label_map.values())) is tf.int32
input_tensor = tf.cast(['cat', 'person'], tf.string)	# Tensor("Cast/x:0", shape=(2,), dtype=string)
out = table.lookup(input_tensor)	# Tensor("hash_table_Lookup:0", shape=(2,), dtype=int64)
with tf.Session() as sess:
	table.init.run()	# initialize the table	
	print(out.eval())
	# [ 8 15]
