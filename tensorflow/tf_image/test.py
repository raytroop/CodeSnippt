import matplotlib.pyplot as plt
import tensorflow as tf

img_raw = tf.gfile.FastGFile('bladerrunner.jpg', 'rb').read()
img_jpg_org = tf.image.decode_jpeg(img_raw)		# [0, 255]	<dtype: 'uint8'>
img_jpg = tf.image.convert_image_dtype(img_jpg_org, dtype=tf.float32)	# [0, 1] <dtype: 'float32'>
crop = tf.image.resize_image_with_crop_or_pad(img_jpg, 500, 500)
pad = tf.image.resize_image_with_crop_or_pad(img_jpg, 2000, 2000)
sat = tf.image.random_saturation(img_jpg, lower=0.5, upper=1.5, seed=42)	# ValueError: lower must be non-negative.
flip_rnd = tf.image.random_flip_left_right(img_jpg, seed=365)
flip = tf.image.flip_left_right(img_jpg)
brightness = tf.image.random_brightness(img_jpg, max_delta=32./255.)
contrast = tf.image.random_contrast(img_jpg, lower=0.5, upper=1.5)
hue = tf.image.random_hue(img_jpg, max_delta=0.2)	# max_delta must be in the interval [0, 0.5]
rnd = tf.less(tf.random_uniform(shape=[], minval=0, maxval=2), 1)
flip_not = tf.cond(rnd, lambda: tf.identity(img_jpg), lambda: tf.image.flip_left_right(img_jpg))

def flip_udlr(img):
	return tf.image.flip_left_right(img), tf.image.flip_up_down(img)

flip1, flip2 = tf.cond(rnd, lambda: (tf.identity(img_jpg), tf.identity(img_jpg)), lambda: flip_udlr(img_jpg))
with tf.Session() as sess:
# 	plt.figure(1)
# 	plt.imshow(crop.eval())
# 	plt.figure(2)
# 	plt.imshow(pad.eval())
	flip1_, flip2_ = sess.run([flip1, flip2])
	plt.figure()
	plt.imshow(flip1_)
	plt.figure()
	plt.imshow(flip2_)
	flip1_, flip2_ = sess.run([flip1, flip2])
	plt.figure()
	plt.imshow(flip1_)
	plt.figure()
	plt.imshow(flip2_)
	flip1_, flip2_ = sess.run([flip1, flip2])
	plt.figure()
	plt.imshow(flip1_)
	plt.figure()
	plt.imshow(flip2_)
	flip1_, flip2_ = sess.run([flip1, flip2])
	plt.figure()
	plt.imshow(flip1_)
	plt.figure()
	plt.imshow(flip2_)
	flip1_, flip2_ = sess.run([flip1, flip2])
	plt.figure()
	plt.imshow(flip1_)
	plt.figure()
	plt.imshow(flip2_)
	flip1_, flip2_ = sess.run([flip1, flip2])
	plt.figure()
	plt.imshow(flip1_)
	plt.figure()
	plt.imshow(flip2_)
	flip1_, flip2_ = sess.run([flip1, flip2])
	plt.figure()
	plt.imshow(flip1_)
	plt.figure()
	plt.imshow(flip2_)
	plt.show()
	# idx = 0
	# N = 10000
	# for i in range(N):
	# 	idx += int(rnd.eval())
	# print(idx/float(N))	
