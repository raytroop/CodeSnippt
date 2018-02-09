import tensorflow as tf


def parser(example, istraining):
    features = {'label': tf.FixedLenFeature([6], tf.int64),
                'image_raw': tf.FixedLenFeature([], tf.string),
                'name': tf.FixedLenFeature([], tf.int64)}
    feats = tf.parse_single_example(example, features)
    label = tf.cast(feats['label'], tf.int32)
    image = tf.decode_raw(feats['image_raw'], tf.uint8)
    image = tf.reshape(image, [64, 64, 3])
    image = tf.random_crop(image, [54, 54, 3])
    image = tf.cast(image, tf.float32)
    name = tf.cast(feats['name'], tf.int32)
    return image, label, name


def input_pipeline(tfrecord, batch_size, istraining=False):
    dt = tf.data.TFRecordDataset(tfrecord)
    dt = dt.map(lambda example: parser(example, istraining), num_parallel_calls=4)
    if istraining:
        dt = dt.shuffle(10*batch_size)
    dt = dt.prefetch(batch_size)
    dt = dt.batch(batch_size)
    return dt
