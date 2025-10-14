# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:30:40 2024

@author: pyx
"""

import numpy as np
from skimage import io
from scipy.ndimage import median_filter

# Input and output file paths
input_file = "C:/Users/pyx/Desktop/documents/SBU WORK/DEGREE/Co3O4_June_FXI/porosity_definition/97960.tif"
output_file = "C:/Users/pyx/Desktop/documents/SBU WORK/DEGREE/Co3O4_June_FXI/porosity_definition/97960_median_smoothed_segmented.tif"

# Read the image stack
image_stack = io.imread(input_file)

# Apply 3D median filtering
filter_size = 3  # Median filter size
smoothed_stack = median_filter(image_stack, size=filter_size)

# Define the threshold value
threshold_value = 0.0049

# Apply thresholding to the smoothed stack
segmented_stack = np.where(smoothed_stack > threshold_value, 255, 0).astype(np.uint8)

# Save the segmented stack as a single TIFF file
io.imsave(output_file, segmented_stack)

print(f"Median smoothed and segmented image stack saved as {output_file}")
