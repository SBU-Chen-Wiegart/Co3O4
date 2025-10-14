# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 12:17:42 2025

@author: pyx
"""

import matplotlib.pyplot as plt
import numpy as np

# Data
x_labels_volume = ['800°C', '850°C', '800°C', '900°C', 'RT']
x = np.arange(len(x_labels_volume))

y1 = np.array([644, 1507, 1420, 1041, 1558])   # Microparticle Volume (μm³)
y3 = np.array([1519, 3810, 4137, 2596, 3977])  # micro surface Volume (μm³)
y2 = np.array([290, 284, 303, 306, 280])       # nano volume (μm²)
y4 = np.array([1443, 1623, 1722, 1864, 1644])  # Nanoparticle Surface Area (μm²)

# Specific Surface Area
ssa_micro = y3 / y1
ssa_nano = y4 / y2

# Plot settings
bar_width = 0.35
fontsize = 20

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Volume plot
axs[0].bar(x - bar_width/2, y1, bar_width, label='Microparticle')
axs[0].bar(x + bar_width/2, y3, bar_width, label='Nanoparticle')
axs[0].set_title('Volume', fontsize=fontsize)
axs[0].set_ylabel('Volume (μm³)', fontsize=fontsize)
axs[0].set_xticks(x)
axs[0].set_xticklabels(x_labels_volume, fontsize=fontsize)
axs[0].legend(fontsize=fontsize)
axs[0].tick_params(axis='y', labelsize=fontsize)

# Surface area plot
axs[1].bar(x - bar_width/2, y2, bar_width, label='Microparticle')
axs[1].bar(x + bar_width/2, y4, bar_width, label='Nanoparticle')
axs[1].set_title('Surface Area', fontsize=fontsize)
axs[1].set_ylabel('Surface Area (μm²)', fontsize=fontsize)
axs[1].set_xticks(x)
axs[1].set_xticklabels(x_labels_volume, fontsize=fontsize)
axs[1].legend(fontsize=fontsize)
axs[1].tick_params(axis='y', labelsize=fontsize)

# Specific surface area plot
axs[2].bar(x - bar_width/2, ssa_micro, bar_width, label='Microparticle')
axs[2].bar(x + bar_width/2, ssa_nano, bar_width, label='Nanoparticle')
axs[2].set_title('Specific Surface Area', fontsize=fontsize)
axs[2].set_ylabel('SSA (μm⁻¹)', fontsize=fontsize)
axs[2].set_xticks(x)
axs[2].set_xticklabels(x_labels_volume, fontsize=fontsize)
axs[2].legend(fontsize=fontsize)
axs[2].tick_params(axis='y', labelsize=fontsize)

plt.tight_layout()
plt.show()
