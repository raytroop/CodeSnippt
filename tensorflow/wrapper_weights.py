import tensorflow as tf
# wrapper graph to share weights for many times

class my_add:
	def __init__(self):
		self.coeff = tf.Variable(1.0, name='coeff')
	def __call__(self, mul):
		return mul * self.coeff

# In [3]: from add import my_add

# In [4]: model = my_add()

# In [5]: tf.global_variables()
# Out[5]: [<tf.Variable 'coeff:0' shape=() dtype=float32_ref>]

# In [6]: mul1 = tf.placeholder(dtype=tf.float32, shape=[])

# In [7]: mul2 = tf.placeholder(dtype=tf.float32, shape=[])

# In [8]: o1 = model(mul1)

# In [9]: o2 = model(mul2)

# In [10]: tf.global_variables()
# Out[10]: [<tf.Variable 'coeff:0' shape=() dtype=float32_ref>]

# In [11]: sess = tf.Session()

# In [12]: sess.run(tf.global_variables_initializer())

# In [13]: sess.run([o1, o2], feed_dict={mul1:1, mul2:2})
# Out[13]: [1.0, 2.0]

# In [14]: tf.global_variables()
# Out[14]: [<tf.Variable 'coeff:0' shape=() dtype=float32_ref>]
