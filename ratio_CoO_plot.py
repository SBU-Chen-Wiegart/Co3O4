#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:55:12 2024

@author: karenchen-wiegart
"""

import numpy as np
import matplotlib.pyplot as plt

# Provided data
x = [
    22, 26.4, 30.8, 35.4, 40.1, 46.6, 58.3, 63.1, 67.6, 72.1, 76.3, 80.9, 85.3, 
    89.6, 93.9, 99.9, 104.2, 109.1, 115.3, 123.2, 128.1, 133.1, 137.5, 150.6, 
    155.1, 159.4, 164.3, 169.7, 175, 179.5, 184.2
]
y = [
    0.7774044068747447, 0.8689362823955968, 0.9082909440076292, 0.9331745649097687,
    0.9589029897727584, 0.9629285914881262, 0.8285019105681627, 0.6263286151599443,
    0.5172610069215964, 0.48835645846225023, 0.35746037811131687, 0.3124273352962928,
    0.30247912091490653, 0.239984988322368, 0.2192366309764078, 0.2353698217048119,
    0.19692302028562872, 0.18310514760123858, 0.19308430459997078,  0.09077295378010601, 0.08810374398409339, 0.06408840436113583, 0.05496984034407995,
    0.11867837248045629, 0.25368066348070756, 0.34357523391304196,
    0.4257235621542583, 0.49679838852312386, 0.595242660133402, 0.7192733178201935,
    0.7617222078088891]

# Remove None values for plotting
x_filtered = [x[i] for i in range(len(x)) if y[i] is not None]
y_filtered = [yi for yi in y if yi is not None]

# Plot the data
plt.figure(figsize=(12, 8))

# Column plot
bar_width = 2.5  # Adjust this value to control the bar width
plt.bar(
    x_filtered, y_filtered, width=bar_width, color='red', edgecolor='black', alpha=0.8)

# Line plot without markers
plt.plot(
    x_filtered, y_filtered, color='blue', linestyle='-', linewidth=2)

# Add labels, title, and legend
plt.xlabel('Time (min)', fontsize=24)
plt.ylabel('Fraction of CoO', fontsize=24)
#plt.title('Time vs. Fraction of CoO', fontsize=24)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.legend(fontsize=20)

# Grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
