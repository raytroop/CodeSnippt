import tensorflow as tf


r"""Convert raw COCO dataset to TFRecord for object_detection.

Example usage:
    python create_coco_tf_record.py --logtostderr \
      --train_image_dir="${TRAIN_IMAGE_DIR}" \
      --val_image_dir="${VAL_IMAGE_DIR}" \
      --test_image_dir="${TEST_IMAGE_DIR}" \
      --train_annotations_file="${TRAIN_ANNOTATIONS_FILE}" \
      --val_annotations_file="${VAL_ANNOTATIONS_FILE}" \
      --testdev_annotations_file="${TESTDEV_ANNOTATIONS_FILE}" \
      --output_dir="${OUTPUT_DIR}"
"""

import tensorflow as tf


flags = tf.app.flags
tf.flags.DEFINE_boolean('include_masks', False,
                        'Whether to include instance segmentations masks '
                        '(PNG encoded) in the result. default: False.')
tf.flags.DEFINE_string('train_image_dir', '',
                       'Training image directory.')
tf.flags.DEFINE_string('val_image_dir', '',
                       'Validation image directory.')
tf.flags.DEFINE_string('test_image_dir', '',
                       'Test image directory.')
tf.flags.DEFINE_string('train_annotations_file', '',
                       'Training annotations JSON file.')
tf.flags.DEFINE_string('val_annotations_file', '',
                       'Validation annotations JSON file.')
tf.flags.DEFINE_string('testdev_annotations_file', '',
                       'Test-dev annotations JSON file.')
tf.flags.DEFINE_string('output_dir', '/tmp/', 'Output data directory.')

FLAGS = flags.FLAGS

print(FLAGS.include_masks)
if(FLAGS.include_masks == True):
	print('true')

if(FLAGS.include_masks == False):
	print('false')


# (tf) raytroop@MyServer:~/test$ python tf_flags_boolean.py --include_masks=false
# False
# false
# (tf) raytroop@MyServer:~/test$ python tf_flags_boolean.py --include_masks="false"
# False
# false
# (tf) raytroop@MyServer:~/test$ python tf_flags_boolean.py --include_masks=True
# True
# true
# (tf) raytroop@MyServer:~/test$ python tf_flags_boolean.py --include_masks="true"True
# true
