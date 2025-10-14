# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:59:25 2024

@author: pyx
"""

import numpy as np
from skimage.morphology import convex_hull_image
import matplotlib.pyplot as plt
from skimage.io import imread, imsave

# Load the 3D image stack from the specified path
image_stack = imread(r"C:\Users\pyx\Desktop\documents\SBU WORK\DEGREE\Co3O4_June_FXI\porosity_definition\Result of 97960_LP.tif")

# Threshold the entire stack to create a binary image (assuming 0 is background and 1 is foreground)
thresholded_stack = image_stack > 0  # Adjust the threshold value if necessary

# Initialize a 3D volume to store the filled result
filled_stack = np.zeros_like(thresholded_stack, dtype=bool)

# Apply the convex hull in 3D
# For each slice, we apply the convex hull method considering the full stack
for z in range(thresholded_stack.shape[0]):  # Iterate over the z-axis (slices)
    filled_stack[z] = convex_hull_image(thresholded_stack[z])

# Show a couple of slices for visual comparison
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Show slice 80 of the original and filled stack for comparison
ax[0].imshow(thresholded_stack[80], cmap='gray')
ax[0].set_title('Original Thresholded Slice 80')
ax[1].imshow(filled_stack[80], cmap='gray')
ax[1].set_title('Filled Slice 80 using 3D Convex Hull')
plt.show()

# Optionally save the modified stack as a new TIFF file
imsave(r"C:\Users\pyx\Desktop\documents\SBU WORK\DEGREE\Co3O4_June_FXI\porosity_definition\Modified_Result_97960_LP.tif", filled_stack)
