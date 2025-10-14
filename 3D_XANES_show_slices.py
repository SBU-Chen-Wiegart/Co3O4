# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 15:14:53 2025

@author: pyx
"""

import tifffile
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm

# Load TIFF stack
stack_path = 'C:/Users/pyx/Desktop/documents/SBU WORK/paper/Paper_Co3O4_TCM/3D_XANES/xanes_2D_all_product_stack_with_nan.tiff'  # Replace with your actual file path
stack = tifffile.imread(stack_path)

# Slice indices: every 3 slices from 148 to 172 inclusive
slices = list(range(148, 173, 3))  # [148, 151, 154, 157, 160, 163, 166, 169, 172]
selected_slices = stack[slices]

# Value range for colorbar
vmin, vmax = 7.726, 7.732

# Get default rainbow colormap and set NaNs to black
cmap = cm.get_cmap('gnuplot').copy()
cmap.set_bad(color='black')

# Plot each slice in its own figure
for idx, slice_idx in enumerate(slices):
    fig, ax = plt.subplots(figsize=(5, 5))
    img = selected_slices[idx]
    img_masked = np.ma.masked_invalid(img)  # Mask NaNs

    im = ax.imshow(img_masked, cmap=cmap, norm=Normalize(vmin=vmin, vmax=vmax))
    ax.set_title(f"Slice {slice_idx}")
    ax.axis('off')

    # Add individual colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Value", rotation=270, labelpad=15)

    plt.tight_layout()
    plt.show()
