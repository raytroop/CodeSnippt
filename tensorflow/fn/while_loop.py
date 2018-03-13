import tensorflow as tf
"""
Note that while_loop calls cond and body exactly once 
(inside the call to while_loop, and not at all during Session.run()). 
while_loop stitches together the graph fragments created during the cond 
and body calls with some additional graph nodes to create the graph flow 
that repeats body until cond returns false.

cond and body both take as many arguments as there are loop_vars.
Returns:
The output tensors for the loop variables after the loop. 
"""
n1 = tf.constant(2)
n2 = tf.constant(3)
n3 = tf.constant(4)

def cond1(i, a, b):
    return i < n1

def cond2(i, a, b):
    return i < n2

def cond3(i, a, b):
    return i < n3

def body(i, a, b):
    return i + 1, b, a + b

i1, a1, b1 = tf.while_loop(cond1, body, (2, 1, 1))	# cond1 return False, do not invoke body
i2, a2, b2 = tf.while_loop(cond2, body, (2, 1, 1))
i3, a3, b3 = tf.while_loop(cond3, body, (2, 1, 1))
sess = tf.Session()

print(sess.run(i1))
print(sess.run(a1))
print(sess.run(b1))
print("-")
print(sess.run(i2))
print(sess.run(a2))
print(sess.run(b2))
print("-")
print(sess.run(i3))
print(sess.run(a3))
print(sess.run(b3))



""" ssd_common.py
    def condition(i,
                  feat_labels, feat_scores, feat_ymin, feat_xmin, feat_ymax, feat_xmax):
        """Condition: check label index.
        """
        # print('-------------------------')
        # print('-------------------------')
        # print(i)
        # print(tf.shape(labels))
        # print('-------------------------')
        # print('-------------------------')
        # -------------------------
        # -------------------------
        # Tensor("bboxes_encode_block_0/while/Merge:0", shape=(), dtype=int32, device= / device: CPU:0)
        # Tensor("bboxes_encode_block_0/while/Shape:0", shape=(1,), dtype=int32, device= / device: CPU:0)
        # -------------------------
        # or
        # -------------------------
        # Tensor("bboxes_encode_block_1/while/Merge:0", shape=(), dtype=int32, device= / device: CPU:0)
        # Tensor("bboxes_encode_block_1/while/Shape:0", shape=(1,), dtype=int32, device= / device: CPU:0)
        # -------------------------
        # or
        # -------------------------
        # Tensor("bboxes_encode_block_2/while/Merge:0", shape=(), dtype=int32, device= / device: CPU:0)
        # Tensor("bboxes_encode_block_2/while/Shape:0", shape=(1,), dtype=int32, device= / device: CPU:0)
        # -------------------------
        # or
        # -------------------------
        # Tensor("bboxes_encode_block_3/while/Merge:0", shape=(), dtype=int32, device= / device: CPU:0)
        # Tensor("bboxes_encode_block_3/while/Shape:0", shape=(1,), dtype=int32, device= / device: CPU:0)
        # -------------------------
        # or
        # -------------------------
        # Tensor("bboxes_encode_block_4/while/Merge:0", shape=(), dtype=int32, device= / device: CPU:0)
        # Tensor("bboxes_encode_block_4/while/Shape:0", shape=(1,), dtype=int32, device= / device: CPU:0)
        # -------------------------
        # or
        # -------------------------
        # Tensor("bboxes_encode_block_5/while/Merge:0", shape=(), dtype=int32, device= / device: CPU:0)
        # Tensor("bboxes_encode_block_5/while/Shape:0", shape=(1,), dtype=int32, device= / device: CPU:0)
        # -------------------------
        # -------------------------
        r = tf.less(i, tf.shape(labels))
        return r[0]     # scalar tensor

    def body(i, feat_labels, feat_scores,
             feat_ymin, feat_xmin, feat_ymax, feat_xmax):
        """Body: update feature labels, scores and bboxes.
        Follow the original SSD paper for that purpose:
          - assign values when jaccard > 0.5;
          - only update if beat the score of other bboxes.
          feat_scores = tf.zeros(shape, dtype=dtype)
                        (38, 38, 4) or (19, 19, 6) ....
        """
        # feat_scores = tf.zeros(shape, dtype=dtype):
        # feat_scores is used to log jaccard between anchors and previous bbox and update feat_scores
        # every bbox computing in tf.while_loop

        # Jaccard score.
        label = labels[i]
        bbox = bboxes[i]
        jaccard = jaccard_with_anchors(bbox)    # (38, 38, 4)
        # Mask: check threshold + scores + no annotations + num_classes.
        mask = tf.greater(jaccard, feat_scores)     # (38, 38, 4)
        mask = tf.logical_and(mask, feat_scores > -0.5)
        # https://github.com/balancap/SSD-Tensorflow/issues/10#issuecomment-283694447
        # Exactly, the negative values are used to mark the anchors with no annotations.
        # The idea comes from the KITTI dataset where some part of the dataset images are signaled as being not labelled
        # : there may be a car/person/... in these parts, but it has not been segmented.
        # If you don't keep track of these parts, you may end up with the SSD model detecting objects not annotated,
        # and the loss function thinking it is False positive, and pushing for not detecting it.
        # Which is not really what we want ! So basically, I set up a mask
        # such that the loss function ignores the anchors which overlap too much with parts of images no-annotated.

        # I think the -0.5 here doesn't infer the jaccard overlap threshold to get the default boxes,
        # it's just a protecting process. And the jaccard overlap threshold is in the ssd_losses function
        # which on "ssd_vgg_300.py", and you would see it before the pmask present.

        mask = tf.logical_and(mask, label < num_classes)
        imask = tf.cast(mask, tf.int64)
        fmask = tf.cast(mask, dtype)
        # Update values using mask.
        feat_labels = imask * label + (1 - imask) * feat_labels     # feat_labels = tf.zeros(shape, dtype=tf.int64)
        feat_scores = tf.where(mask, jaccard, feat_scores)      # update fea_scores

        feat_ymin = fmask * bbox[0] + (1 - fmask) * feat_ymin       # feat_ymin = tf.zeros(shape, dtype=dtype)
        feat_xmin = fmask * bbox[1] + (1 - fmask) * feat_xmin       # feat_xmin = tf.zeros(shape, dtype=dtype)
        feat_ymax = fmask * bbox[2] + (1 - fmask) * feat_ymax       # feat_ymax = tf.ones(shape, dtype=dtype)
        feat_xmax = fmask * bbox[3] + (1 - fmask) * feat_xmax       # feat_xmax = tf.ones(shape, dtype=dtype)

        # Check no annotation label: ignore these anchors...
        # interscts = intersection_with_anchors(bbox)
        # mask = tf.logical_and(interscts > ignore_threshold,
        #                       label == no_annotation_label)
        # # Replace scores by -1.
        # feat_scores = tf.where(mask, -tf.cast(mask, dtype), feat_scores)

        return [i+1, feat_labels, feat_scores,
                feat_ymin, feat_xmin, feat_ymax, feat_xmax]

    # Main loop definition.
    i = 0
    [i, feat_labels, feat_scores,
     feat_ymin, feat_xmin,
     feat_ymax, feat_xmax] = tf.while_loop(condition, body,
                                           [i, feat_labels, feat_scores,
                                            feat_ymin, feat_xmin,
                                            feat_ymax, feat_xmax])

                                            
     """
