#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:17:42 2025

@author: karenchen-wiegart
"""
import numpy as np
from tifffile import imread
from PIL import Image
import os

# Define the range of fn values
start_fn = 85976
end_fn = 86007

# Iterate through the specified range of image numbers
for fn in range(start_fn, end_fn + 1):
    # Format the image path dynamically based on fn value
    image_path = f"/media/karenchen-wiegart/Expansion3/Karen_311953_2024Q1/YUxiang/2D_XANES_quantification/raw_{fn}.tiff"
    
    # Check if files exist
    if not os.path.exists(image_path) or not os.path.exists(image_path):
        print(f"File not found for fn={fn}, skipping.")
        continue

    # Load the image stack for the current image
    stack = imread(image_path)

    # Get the dimensions of the image stack
    num_images, height, width = stack.shape

    # Create an empty array to store the new image
    distance_image = np.zeros((height, width))

    # Iterate through every pixel in the image
    for i in range(height):
        for j in range(width):
            # Extract the pixel values across all images for the current pixel (i, j)
            pixel_values = stack[:, i, j]
            
            # If pixel_values[26] is 0, set the distance to 0 directly
            if pixel_values[26] == 0:
                distance_image[i, j] = 0
            else:
                # Line A: Fit a line through points No. 27 and No. 28
                x_vals_A = np.array([27, 28])
                y_vals_A = np.array([pixel_values[26], pixel_values[27]])
                coeff_A = np.polyfit(x_vals_A, y_vals_A, 1)  # Linear fit
                
                # Line B: Parallel line through point (6, pixel_values[5])
                slope = coeff_A[0]
                intercept_B = pixel_values[5] - slope * 6  # y = ax + b -> b = y - ax
                
                # Distance between the two parallel lines
                intercept_A = coeff_A[1]
                distance = abs(intercept_A - intercept_B) / np.sqrt(1 + slope**2)
                
                # Store the distance in the new image
                distance_image[i, j] = distance

    # Normalize the distance image for saving
    #distance_image_normalized = (255 * (distance_image / np.max(distance_image))).astype(np.uint8)

    # Format the output path dynamically based on fn value
    output_path = f"/media/karenchen-wiegart/Expansion3/Karen_311953_2024Q1/YUxiang/2D_XANES_quantification/distance_image_{fn}.tiff"
    
    # Save the distance image as a TIFF file
    distance_image_pil = Image.fromarray(distance_image)
    distance_image_pil.save(output_path)

    print(f"Processed and saved: {output_path}")
