# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:02:51 2024

@author: pyx
"""

import matplotlib.pyplot as plt
import numpy as np

# New data points
x_new = [13.15,	16.47,	18.98,	22.85,	24.92,	26.93,	28.6,	31.18,	32.9,]
y_new = [3.109519,2.956475134, 2.884893617, 2.750504847, 2.712679253, 2.651086511, 2.641102457, 2.587798515, 2.57979778]

# Calculate y^-1, y^-2, y^-3, y^-4
y_inv1 = np.power(y_new, -1)
y_inv2 = np.power(y_new, -2)
y_inv3 = np.power(y_new, -3)
y_inv4 = np.power(y_new, -4)

# Create separate figures
fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.scatter(x_new, y_inv1, color='b', s=50)
#ax1.set_title('Plot of x vs. y^-1', fontsize=14)
#ax1.set_xlabel('X-axis', fontsize=16)
#ax1.set_ylabel('Y^-1-axis', fontsize=16)

ax1.set_ylim(0,0.5)
ax1.set_xlim(0,80)  # Set lower limit of y-axis to 0
ax1.grid(False)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
ax1.yaxis.set_major_locator(plt.MultipleLocator(0.1))

fig2, ax2 = plt.subplots(figsize=(7, 5))
ax2.scatter(x_new, y_inv2, color='r', s=50)
#ax2.set_title('Plot of x vs. y^-2', fontsize=14)
#ax2.set_xlabel('X-axis', fontsize=16)
#ax2.set_ylabel('Y^-2-axis', fontsize=16)
ax2.set_ylim(0,0.2)
ax2.set_xlim(0,50)  # Set lower limit of y-axis to 0
ax2.grid(False)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
ax2.yaxis.set_major_locator(plt.MultipleLocator(0.05))

fig3, ax3 = plt.subplots(figsize=(7, 5))
ax3.scatter(x_new, y_inv3, color='g', s=50)
#ax3.set_title('Plot of x vs. y^-3', fontsize=14)
#ax3.set_xlabel('X-axis', fontsize=16)
#ax3.set_ylabel('Y^-3-axis', fontsize=16)
ax3.set_ylim(0,0.08)
ax3.set_xlim(0,50)  # Set lower limit of y-axis to 0
ax3.grid(False)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
ax3.yaxis.set_major_locator(plt.MultipleLocator(0.02))

fig4, ax4 = plt.subplots(figsize=(7, 5))
ax4.scatter(x_new, y_inv4, color='m', s=50)
#ax4.set_title('Plot of x vs. y^-4', fontsize=14)
#ax4.set_xlabel('X-axis', fontsize=16)
#ax4.set_ylabel('Y^-4-axis', fontsize=16)
ax4.set_ylim(0,0.03)  # Set lower limit of y-axis to 0
ax4.set_xlim(0,50)
ax4.grid(False)
ax4.yaxis.set_major_locator(plt.MultipleLocator(0.01))

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# Show all the plots
plt.show()



