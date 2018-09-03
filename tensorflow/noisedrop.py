# https://zhuanlan.zhihu.com/p/28192383
import tensorflow as tf
import numpy as np

ax = np.arange(27).reshape(1, 3, 3, 3)
print(ax[..., 0])
print(ax[..., 1])
print(ax[..., 2])

ax = tf.constant(ax, dtype=tf.float32)
print(ax)
noise_shape = (1, 1, 1, 3)
ax_drop = tf.nn.dropout(ax, keep_prob=0.1, noise_shape=noise_shape, seed=0)
# print(tf.global_variables())

config = tf.ConfigProto()
config.gpu_options.allow_growth = True  # pylint: disable=no-member
with tf.Session(config=config) as sess:
    ax_drop_ = ax_drop.eval()
    print(ax_drop_[..., 0])
    print(ax_drop_[..., 1])
    print(ax_drop_[..., 2])
