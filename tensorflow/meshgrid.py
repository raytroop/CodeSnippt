import tensorflow as tf
import numpy as np
scales = 32
ratios = [0.5, 1, 2]
scales, ratios = np.meshgrid(np.array(scales), np.array(ratios))    # scales: 32, ratios: 0.5, 1, 2
# print(scales)
# [[32]
#  [32]
#  [32]]
# print(ratios)
# [[0.5]
#  [1. ]
#  [2. ]]
scales = scales.flatten()   # (32, 32, 32) or (64, 64, 64), ...
ratios = ratios.flatten()   # (0.5, 1, 2)

# Enumerate heights and widths from scales and ratios
heights = scales / np.sqrt(ratios)  # (32/sqrt(0.5), 32/sqrt(1), 32/sqrt(2))
widths = scales * np.sqrt(ratios)   # (32*sqrt(0.5), 32*sqrt(1), 32*sqrt(2))

# Enumerate shifts in feature space
shifts_y = np.arange(0, shape[0], anchor_stride) * feature_stride   # [0, 256) * 4--> (0, 4, 8, ... 1020)
shifts_x = np.arange(0, shape[1], anchor_stride) * feature_stride   # [0, 256) * 4--> (0, 4, 8, ... 1020)
shifts_x, shifts_y = np.meshgrid(shifts_x, shifts_y)        # (256, 256), or (128, 128), ...

# Enumerate combinations of shifts, widths, and heights
box_widths, box_centers_x = np.meshgrid(widths, shifts_x)       # (shape[0]*shape[1], 3), first **flatten**
box_heights, box_centers_y = np.meshgrid(heights, shifts_y)     # (shape[0]*shape[1], 3)

# Reshape to get a list of (y, x) and a list of (h, w)
box_centers = np.stack(
    [box_centers_y, box_centers_x], axis=2).reshape([-1, 2])                # (shape[0]*shape[1]*3, 2)
box_sizes = np.stack([box_heights, box_widths], axis=2).reshape([-1, 2])    # (shape[0]*shape[1]*3, 2)

# Convert to corner coordinates (y1, x1, y2, x2)
boxes = np.concatenate([box_centers - 0.5 * box_sizes,
                        box_centers + 0.5 * box_sizes], axis=1)     # (shape[0]*shape[1]*3, 4)


# same with tf.meshgrid 