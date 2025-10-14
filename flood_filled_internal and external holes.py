# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:42:36 2024

@author: pyx
"""
import numpy as np
import tifffile as tiff
from scipy.ndimage import label
from skimage.segmentation import flood
import matplotlib.pyplot as plt

# Load the binary 3D image stack
image_path = r"C:\Users\pyx\Desktop\documents\SBU WORK\DEGREE\Co3O4_June_FXI\porosity_definition\Result of 97960_LP.tif"
image_stack = tiff.imread(image_path)  # Load TIFF as NumPy array
assert image_stack.ndim == 3, "Image is not a 3D stack!"

# Step 1: Prepare the edge mask
z, y, x = image_stack.shape
edge_mask = np.zeros_like(image_stack, dtype=bool)
edge_mask[0, :, :] = True  # Top face
edge_mask[-1, :, :] = True  # Bottom face
edge_mask[:, 0, :] = True  # Left face
edge_mask[:, -1, :] = True  # Right face
edge_mask[:, :, 0] = True  # Front face
edge_mask[:, :, -1] = True  # Back face

# Step 2: Flood-fill the background connected to edges
filled_stack = np.copy(image_stack)  # Start with a copy of the original image
flood_mask = np.zeros_like(filled_stack, dtype=bool)  # Mask for flooded regions

for z_idx in [0, z - 1]:  # Iterate over top and bottom slices
    for y_idx in range(y):
        for x_idx in range(x):
            if filled_stack[z_idx, y_idx, x_idx] == 0 and not flood_mask[z_idx, y_idx, x_idx]:
                flood_region = flood(filled_stack, seed_point=(z_idx, y_idx, x_idx))
                flood_mask = flood_mask | flood_region

# Step 3: Identify internal and external holes
external_holes = flood_mask & (image_stack == 0)
internal_holes = ~flood_mask & (image_stack == 0)

# Step 4: Label internal and external holes
labeled_internal_holes, num_internal = label(internal_holes)
labeled_external_holes, num_external = label(external_holes)

# Output Results
print(f"Number of internal holes: {num_internal}")
print(f"Number of external holes: {num_external}")

# Step 5: Save the internal and external hole stacks
internal_holes_path = r"C:\Users\pyx\Desktop\documents\SBU WORK\DEGREE\Co3O4_June_FXI\porosity_definition\Result of 97960_LP_internal.tif"
external_holes_path = r"C:\Users\pyx\Desktop\documents\SBU WORK\DEGREE\Co3O4_June_FXI\porosity_definition\Result of 97960_LP_external.tif"


tiff.imwrite(internal_holes_path, labeled_internal_holes.astype(np.uint8), photometric='minisblack')
tiff.imwrite(external_holes_path, labeled_external_holes.astype(np.uint8), photometric='minisblack')

print(f"Internal holes saved to: {internal_holes_path}")
print(f"External holes saved to: {external_holes_path}")

# Step 6: Visualize slices (optional)
slice_idx = z // 2  # Middle slice for visualization
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(image_stack[slice_idx], cmap="gray")
plt.subplot(1, 3, 2)
plt.title("Internal Holes")
plt.imshow(labeled_internal_holes[slice_idx], cmap="jet")
plt.subplot(1, 3, 3)
plt.title("External Holes")
plt.imshow(labeled_external_holes[slice_idx], cmap="jet")
plt.tight_layout()
plt.show()
