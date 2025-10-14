# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:20:09 2024

@author: pyx
"""

import numpy as np
import tifffile as tiff
from scipy.ndimage import binary_fill_holes

# Load the 3D binary image stack
image_path = r"C:\Users\pyx\Downloads\particles with holes_97997.tif"
image_stack = tiff.imread(image_path)

# Ensure the image stack is 3D
assert image_stack.ndim == 3, "The image stack should be 3D!"

# Get the shape of the image stack (z, y, x)
z, y, x = image_stack.shape

# Step 1: Fill holes in X-Y cross-section (one slice per Z)
filled_xy_stack = np.copy(image_stack)
for z_idx in range(z):
    # Extract the X-Y slice at the current Z slice
    xy_slice = filled_xy_stack[z_idx, :, :]

    # Apply hole filling on the X-Y slice
    filled_xy_slice = binary_fill_holes(xy_slice)

    # Place the filled slice back into the stack
    filled_xy_stack[z_idx, :, :] = filled_xy_slice

# Step 2: Fill holes in X-Z cross-section (one slice per Y)
filled_xz_stack = np.copy(image_stack)
for y_idx in range(y):
    # Extract the X-Z slice at the current Y slice
    xz_slice = filled_xz_stack[:, y_idx, :]

    # Apply hole filling on the X-Z slice
    filled_xz_slice = binary_fill_holes(xz_slice)

    # Place the filled slice back into the stack
    filled_xz_stack[:, y_idx, :] = filled_xz_slice

# Step 3: Fill holes in Y-Z cross-section (one slice per X)
filled_yz_stack = np.copy(image_stack)
for x_idx in range(x):
    # Extract the Y-Z slice at the current X slice
    yz_slice = filled_yz_stack[:, :, x_idx]

    # Apply hole filling on the Y-Z slice
    filled_yz_slice = binary_fill_holes(yz_slice)

    # Place the filled slice back into the stack
    filled_yz_stack[:, :, x_idx] = filled_yz_slice

# Step 4: Combine the results using "OR" operation
combined_stack = np.logical_or(filled_xy_stack, filled_xz_stack)
combined_stack = np.logical_or(combined_stack, filled_yz_stack)

# Convert the result back to a binary image (0 and 1)
final_stack = combined_stack.astype(np.uint8)

# Step 5: Save the final image stack (combined result)
output_path = r"C:\Users\pyx\Downloads\particles with filled_holes_97997.tif"
tiff.imwrite(output_path, final_stack, photometric='minisblack')

# Optional: Visualize one slice of the final stack
import matplotlib.pyplot as plt
plt.imshow(final_stack[0, :, :], cmap='gray')  # Show first slice
plt.title('Final Filled Image Stack (Z=0)')
plt.show()
