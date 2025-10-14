# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:08:11 2024

@author: pyx
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image stack
image_path = r"C:\Users\pyx\Desktop\documents\SBU WORK\DEGREE\Co3O4_FXI_Mar\CoO_ratio_calculation\aligned_85912.tiff"

# Open the image stack
img_stack = Image.open(image_path)

# Seek to the 4th image (index 3, 0-based)
img_stack.seek(3)  # Image 4
img_4th = np.array(img_stack)

# Seek to the 27th image (index 26, 0-based)
img_stack.seek(26)  # Image 27
img_27th = np.array(img_stack)

# Compute the absolute difference
difference = np.abs(img_4th - img_27th)

# Normalize the difference for better visualization (scale to 0-255 range)
difference_normalized = np.uint8(255 * (difference / np.max(difference)))

# Define the equation as a function
def pixel_transform(x):
    return (-4.11335559093599970162e-06*(x*1000-1)**4 + 6.35780352164096868028e-02*(x*1000-1)**3 + 
            -2.94722271414887236618e-02*(x*1000-1)**2 + -3.79679115550591936335e+06*(x*1000-1)**1 + 
            1.46712653362280311584e+10)

# Load the TIFF image for transformation
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

# Calculate the two images
image_1 = difference * transformed_image_array  # difference * transformed_image_array
image_2 = difference * mask_image_array  # difference * mask_image_array

# Calculate total pixel values for each image
total_pixel_value_image_1 = np.sum(image_1)  # Sum of all pixel values in image_1
total_pixel_value_image_2 = np.sum(image_2)  # Sum of all pixel values in image_2

# Print the total pixel values
print(f"Total pixel value for image 1 (difference * transformed_image_array): {total_pixel_value_image_1}")
print(f"Total pixel value for image 2 (difference * mask_image_array): {total_pixel_value_image_2}")

# Display the images
plt.figure(figsize=(8, 6))


#plt.title("Image 1: difference * transformed_image_array")
plt.imshow(image_1, cmap='gnuplot',vmin=0, vmax=0.3)
plt.colorbar()
plt.axis('off')

plt.figure(figsize=(8, 6))

#plt.title("Image 2: difference * mask_image_array")
plt.imshow(image_2, cmap='gnuplot', vmin=0, vmax=0.5)
plt.colorbar()
plt.axis('off')

plt.show()

# Calculate the ratio of total pixel values
ratio = total_pixel_value_image_1 / total_pixel_value_image_2

# Print the ratio
print(f"Ratio of total pixel value in image 1 to image 2: {ratio}")
