# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:09:01 2024

@author: pyx
"""

import matplotlib.pyplot as plt

# Updated x and y values
x = [
    33.5, 40.07, 44.45, 49.48, 53.78, 58.37, 62.73, 65.73, 72.13, 78.5, 84.83, 
    92.45, 98.8, 105.15, 111.61, 118.16, 122.16, 126.41, 130.98, 135.39, 
    140.08, 142.08, 148.53, 155.88, 161.9, 169.81, 177.31
]

y = [
    0.9128144059429167, 0.925163598198214, 0.9413498551438224, 0.9747518989717669, 
    0.9738208405116611, 0.979558991569815, 0.9688293337916528, 0.1565192990682146, 
    0.05214825137685645, 0.05865280433217237, 0.05295187565149903, 0.04247757005250613, 
    0.06723817532190893, 0.0570451014937931, 0.0651176981298351, 0.04992717287171746, 
    0.06425624839092184, 0.014855941534175923, 0.013187846544589136, 
    0.01854728376842143, 0.011499134720167398, 0.8732728519272447, 0.9150010489591591, 
    0.9242794957420444, 0.9401546514213956, 0.9646154498910137,0.9642536179483489
]

# Filter out None values for plotting
x_filtered = [x[i] for i in range(len(x)) if y[i] is not None]
y_filtered = [yi for yi in y if yi is not None]

# Plot settings
plt.figure(figsize=(12, 8))

# Bar plot
bar_width = 2.5  # Adjust bar width
plt.bar(
    x_filtered, y_filtered, width=bar_width, color='red', edgecolor='black', alpha=0.8)

# Line plot
plt.plot(
    x_filtered, y_filtered, color='blue', linestyle='-', linewidth=2)

# Formatting
plt.xlabel('Time (min)', fontsize=24)
plt.ylabel('Fraction of CoO', fontsize=24)
plt.title('Time vs. Fraction of CoO', fontsize=24)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.legend(fontsize=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()

