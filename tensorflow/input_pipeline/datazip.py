
## /models/official/mnist/dataset.py

images = tf.data.FixedLengthRecordDataset(
    images_file, 28 * 28, header_bytes=16).map(decode_image)
labels = tf.data.FixedLengthRecordDataset(
    labels_file, 1, header_bytes=8).map(one_hot_label)
return tf.data.Dataset.zip((images, labels))
