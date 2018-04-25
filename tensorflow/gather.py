import keras as K
import tensorflow as tf

def mrcnn_mask_loss_graph(target_masks, target_class_ids, pred_masks):
    """Mask binary cross-entropy loss for the masks head.

    target_masks: [batch, num_rois, height, width].
        A float32 tensor of values 0 or 1. Uses zero padding to fill array.
    target_class_ids: [batch, num_rois]. Integer class IDs. Zero padded.
    pred_masks: [batch, proposals, height, width, num_classes] float32 tensor
                with values from 0 to 1.
    """
    # Reshape for simplicity. Merge first two dimensions into one.
    target_class_ids = K.reshape(target_class_ids, (-1,))   # (batch * num_rois, )
    mask_shape = tf.shape(target_masks)
    target_masks = K.reshape(target_masks, (-1, mask_shape[2], mask_shape[3]))  # (batch * num_rois, height, width)
    pred_shape = tf.shape(pred_masks)
    pred_masks = K.reshape(pred_masks,
                           (-1, pred_shape[2], pred_shape[3], pred_shape[4]))   # (batch * proposals, height, width, num_classes)
    # Permute predicted masks to [N, num_classes, height, width]
    pred_masks = tf.transpose(pred_masks, [0, 3, 1, 2])     # (batch * proposals, num_classes, height, width)

    # Only positive ROIs contribute to the loss. And only
    # the class specific mask of each ROI.
    positive_ix = tf.where(target_class_ids > 0)[:, 0]          # (?, )
    positive_class_ids = tf.cast(
        tf.gather(target_class_ids, positive_ix), tf.int64)     # (?, )
    indices = tf.stack([positive_ix, positive_class_ids], axis=1)   # (?, 2)

    # Gather the masks (predicted and true) that contribute to loss
    y_true = tf.gather(target_masks,    # (batch * num_rois, height, width)
                       positive_ix)     # (?, )
    y_pred = tf.gather_nd(pred_masks,   # (batch * proposals, num_classes, height, width)
                          indices)      # (?, 2)

    # Compute binary cross entropy. If no positive ROIs, then return 0.
    # shape: [batch, roi, num_classes]
    loss = K.switch(tf.size(y_true) > 0,
                    K.binary_crossentropy(target=y_true,    # (?, height, width)
                                          output=y_pred),   # (?, height, width)
                    tf.constant(0.0))
    loss = K.mean(loss)
    return loss


# rel = tf.gather(target, idx)
# rank(rel) = rank(target)

# rel = tf.gather_nd(target, idx)
# rank(rel) = rank(target) - rank(idx) + 1

