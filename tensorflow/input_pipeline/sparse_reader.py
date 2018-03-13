import tensorflow as tf
import matplotlib.pyplot as plt

def _parser(exmaple):
	keys_to_features = {
      	'image/encoded':
          	tf.FixedLenFeature((), tf.string, default_value=''),
      	'image/format':
          	tf.FixedLenFeature((), tf.string, default_value='jpeg'),
      	'image/object/bbox/xmin':
          tf.VarLenFeature(dtype=tf.float32),
      	'image/object/bbox/ymin':
          	tf.VarLenFeature(dtype=tf.float32),
      	'image/object/bbox/xmax':
          	tf.VarLenFeature(dtype=tf.float32),
      	'image/object/bbox/ymax':
          	tf.VarLenFeature(dtype=tf.float32),
      	'image/object/bbox/label':
          	tf.VarLenFeature(dtype=tf.int64),
  		}
	feats = tf.parse_single_example(exmaple, keys_to_features)
	img = tf.image.decode_png(feats['image/encoded'], channels=3)
	xmin = tf.sparse_tensor_to_dense(feats['image/object/bbox/xmin'])
	return img, xmin

def data_gen(tfrecords):
	dt = tf.data.TFRecordDataset(tfrecords)
	dt = dt.map(_parser)
	iterator = dt.make_one_shot_iterator()
	img, xmin = iterator.get_next()
	return img, xmin

if __name__ == '__main__':
	img, xmin = data_gen('voc_2007_train_000.tfrecord')
	sess = tf.Session()
	img_, xmin_ = sess.run([img, xmin])
	print('img_.dtype'.format(img_.dtype))
	print('img_.shape: {}'.format(img_.shape))
	print('img_.max(): {}'.format(img_.max()))
	print('img_.min(): {}'.format(img_.min()))
	print('xmin_.dtype'.format(xmin_.dtype))
	print('xmin_.shape: {}'.format(xmin_.shape))
	print('xmin_.max(): {}'.format(xmin_.max()))
	print('xmin_.min(): {}'.format(xmin_.min()))
	plt.imshow(img_)
	plt.show()