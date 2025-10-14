#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:23:57 2025

@author: karenchen-wiegart
"""


import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

start_fn = 85894
end_fn = 85927

# Loop over the fn range
for fn in range(start_fn, end_fn + 1):
    try:
        # Load the image stack
        image_path = rf"/media/karenchen-wiegart/Expansion3/Karen_311953_2024Q1/YUxiang/2D_XANES_quantification/micro/distance_image_{fn}.tiff"
        image_path2 = rf"/media/karenchen-wiegart/Expansion3/Karen_311953_2024Q1/YUxiang/2D_XANES_quantification/micro/CoO_ratio_{fn}.tiff"

        # Check if files exist
        if not os.path.exists(image_path) or not os.path.exists(image_path2):
            print(f"File not found for fn={fn}, skipping.")
            continue
        
        # Load the images
        thickness_image = imread(image_path)
        ratio_image = imread(image_path2)
        
        # Initialize empty lists to store x (thickness) and y (ratio)
        x = []
        y = []
        
        # Get the shape of the images (they have the same shape)
        height, width = thickness_image.shape
        
        # Loop through each pixel
        for i in range(height):
            for j in range(width):
                # Get the thickness and ratio values at pixel (i, j)
                thickness_value = thickness_image[i, j]
                ratio_value = ratio_image[i, j]
                
                # Only record if both values are not NaN
                if not np.isnan(thickness_value) and not np.isnan(ratio_value):
                    x.append(thickness_value)
                    y.append(ratio_value)
        
        # Convert x and y lists to numpy arrays for easier manipulation
        x = np.array(x)
        y = np.array(y)
        
        # Step size for the histogram
        step_size = 0.01
        
        # Create the histogram bins for the thickness (x) and CoO ratio (y)
        bins = np.arange(0, np.max(x) + step_size, step_size)
        
        # Initialize counts for thickness and CoO ratio sums
        thickness_counts = np.zeros(len(bins) - 1)
        ratio_sums = np.zeros(len(bins) - 1)
        
        # Loop through the thickness values to create the mask and count/sum
        for i in range(len(bins) - 1):
            # Create a mask for x values in the range [bins[i], bins[i+1])
            mask = (x >= bins[i]) & (x < bins[i + 1])
            
            # Count how many x values are in this bin
            thickness_counts[i] = np.sum(mask)
            
            # Sum the corresponding x * y values where the mask is true
            z_sum = np.sum(x[mask] * y[mask])  # Sum of x * y where mask is true
            
            # Sum the corresponding x values where the mask is true
            x_sum = np.sum(x[mask])
            
            # Calculate the ratio of z_sum to x_sum
            if x_sum != 0:
                ratio_sums[i] = z_sum / x_sum * thickness_counts[i]
            else:
                ratio_sums[i] = 0
        
        # Plot the histograms using bar plots
        fig, ax1 = plt.subplots()
        
        # Plot the histogram for thickness counts as bars
        ax1.bar(bins[:-1], thickness_counts, width=step_size, align='edge', color='blue', alpha=0.5, label='Thickness Count')
        
        # Plot the histogram for CoO ratio sums as bars
        ax1.bar(bins[:-1], ratio_sums, width=step_size, align='edge', color='red', alpha=0.5, label='CoO Ratio Sum')
        
        # Set the x-axis limit from 0 to 5
        ax1.set_xlim(0, 5)
        
        ax1.set_xlabel('Thickness (Range)')
        ax1.set_ylabel('Count / CoO Ratio Sum')
        ax1.set_title(f'Histogram of Thickness and CoO Ratio for fn={fn}')
        
        # Display the plot with legends
        ax1.legend(loc='upper right')
        # Save the plot as PNG file with high resolution (300 dpi)
        output_path = rf"/media/karenchen-wiegart/Expansion3/Karen_311953_2024Q1/YUxiang/2D_XANES_quantification/micro/Thickness_Histogram_{fn}.png"
        plt.savefig(output_path, dpi=300)
        
        # Close the plot to free up memory for the next iteration
        plt.close()
                
    except Exception as e:
        print(f"Error processing fn={fn}: {e}")

       