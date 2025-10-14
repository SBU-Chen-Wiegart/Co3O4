# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:44:03 2024

@author: pyx
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Define the equation as a function
def pixel_transform(x):
    return (-4.11335559093599970162e-06*(x*1000-1)**4 + 6.35780352164096868028e-02*(x*1000-1)**3 + 
            -2.94722271414887236618e-02*(x*1000-1)**2 + -3.79679115550591936335e+06*(x*1000-1)**1 + 
            1.46712653362280311584e+10)

# Load the TIFF image
image_path = r"C:\Users\pyx\Desktop\documents\SBU WORK\DEGREE\Co3O4_FXI_Mar\CoO_ratio_calculation\fitting_85912.tiff"
original_image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(original_image, dtype=np.float64)

# Apply the equation to each pixel
transformed_image_array = pixel_transform(image_array)


# Apply thresholding: Set values greater than 1.02 or less than -0.005 to 0
transformed_image_array[transformed_image_array > 1.02] = 0
transformed_image_array[transformed_image_array < -0.005] = 0

# Create a mask image (1 where pixel value is 0, 0 otherwise)
mask_image_array = (transformed_image_array != 0)

# Optional: Check min/max values of the transformed image
print("Min value after transformation:", np.min(transformed_image_array))
print("Max value after transformation:", np.max(transformed_image_array))

# Original Image
plt.figure(figsize=(8, 6))
#plt.title("Original Image")
plt.imshow(image_array, cmap='gnuplot')
plt.colorbar(shrink=0.8)  # Shorten colorbar
plt.axis('off')
plt.show()

# Transformed Image
plt.figure(figsize=(8, 6))
#plt.title("Transformed Image")
plt.imshow(transformed_image_array, cmap='gnuplot')
plt.colorbar(shrink=0.8)  # Shorten colorbar
plt.axis('off')
plt.show()

# Mask Image
plt.figure(figsize=(8, 6))
#plt.title("Mask Image (0 and 1 Values)")
plt.imshow(mask_image_array, cmap='binary')  # Use 'binary' colormap for discrete values
plt.colorbar(ticks=[0, 1], shrink=0.8)  # Shorten colorbar and show only 0 and 1 ticks
plt.axis('off')
plt.show()
