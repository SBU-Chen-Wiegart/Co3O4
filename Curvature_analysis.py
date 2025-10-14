# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:42:11 2022

@author: Xiaoyin Zheng, Xiaoyang Liu, Yu-chen Karen Chen-Wiegart

Interacial-shape-distribution-ISD

Interfacial shape distribution (ISD) calculation from meshed 3D datasets exported from Avizo/Amira.

The surface mesh and principal curvatures need to be first generated in Avizo/Amira, and saved as ASCII files.

Under ‘Input section:’, add necessary information

    Add file path, e.g., path = r'C:\Users\testfolder’
    Add file name for meshed surface, e.g., filename_mesh = r'test_meshedfile.surf'
    Add file name for the principal curvatures (min/max curvatures), e.g., filename_curvatures = r'BothCurvatures.am'
    Add feature size; the unit needs to be consistent with the pixel size. If this is not needed, leave it as 1. The X and Y axis titles need to be changed to k1 and k2.
    Adjust the xbins and ybins based on the data
"""

import numpy as np
import os
import matplotlib.pyplot as plt



# Find coordinates of vertices

def load_data(filename, options):
    ''' Parameters
    filename: file name of .surf file
    options: 'Vertices' or 'Triangles'

    '''
    with open(filename, 'r', encoding='ISO-8859-1') as f:
        lines = f.readlines()
    f.close()
    
    for i, line in enumerate(lines):
        if options in line:
            idx = i+1
            break
    
    data = list()
    line = lines[idx]
    print(rf'Line of {options}: ', lines[idx-1])
    while line.startswith(' ') or line.startswith('\t'):
        string = line.strip()
        string = string.split(' ')
        string = np.float32(string)
        data.append(string)
        
        idx = idx+1
        line = lines[idx]
    data = np.array(data)
    return data



# Calculate area of a triangle
def areas(vertices, triangles):
    ''' Parameters
    vertices: numpy array of vertices
    triangles: 
    '''
    areas = []
    
    for i in range(len(triangles)):
    
        coordi = np.int32(triangles[i]-1)
        points = vertices[coordi]
        point1, point2, point3 = points[0], points[1], points[2]
        a = np.sqrt(sum((point1-point2)**2))
        b = np.sqrt(sum((point2-point3)**2))
        c = np.sqrt(sum((point3-point1)**2))
        s = 0.5*(a+b+c)
        area = np.sqrt(s*(s-a)*(s-b)*(s-c))
        areas.append(area)
        
    areas = np.array(areas)
    return areas


# Read both curvatures

def get_curvatures(filename_both_curvatures):
    # filename_both_curvatures = r'BothCurvatures_ascii.am'
    with open(filename_both_curvatures, 'r', encoding='ISO-8859-1') as f1:
        lines_curvatures = f1.readlines()
    f1.close()
    
    name = '# Data section follows'
    for i, line in enumerate(lines_curvatures):
        if name in line:
            idx = i+2
            break
    
    line = lines_curvatures[idx]
    min_curvature = list()
    max_curvature = list()

    while not line.startswith('\n'):
        string = line.strip()
        string = string.split(' ')
        string = np.float32(string)
        if string[0]<string[1]:
            min_curvature.append(string[0])
            max_curvature.append(string[1])
        else:
            min_curvature.append(string[1])
            max_curvature.append(string[0])
        
        idx+=1
        line = lines_curvatures[idx]
    return min_curvature, max_curvature




if __name__ == "__main__":
    '''
    Input section:
    	input parameters: file path; vertices/ triangles file; both curvature file; feature size; range of xbins and ybins
    '''
    path = r'/media/karenchen-wiegart/One Touch/pass_309703_3D_XANES/Curvature-20240909T033346Z-001/Curvature/2024_quasi_insitu_FXI/109532_run2'
    os.chdir(path)
    filename_mesh = r'110246_test_3.surf'
    filename_curvatures = r'BothCurvatures_110246.am'
    featuresize = 1     
    xbins = np.linspace(-0.1,0.3,401)
    ybins = np.linspace(-0.2,0.2,401)
    
    
    vertices = load_data(filename_mesh, 'Vertices')
    triangles = load_data(filename_mesh, 'Triangles')
    Areas = areas(vertices, triangles)
    curvature_min, curvature_max = get_curvatures(filename_curvatures)
    curvature_min_times_featuresize = [element * featuresize for element in curvature_min]
    curvature_max_times_featuresize = [element * featuresize for element in curvature_max]
    
    min_length = min(len(curvature_max_times_featuresize), len(curvature_min_times_featuresize), len(Areas))
    curvature_max_times_featuresize = curvature_max_times_featuresize[:min_length]
    curvature_min_times_featuresize = curvature_min_times_featuresize[:min_length]
    Areas = Areas[:min_length]
        
    
    
    
    
    H, xedges, yedges = np.histogram2d(curvature_max_times_featuresize, curvature_min_times_featuresize, normed=True, bins=[xbins,ybins], weights=Areas)
    H = H/np.sum(H)*100
    
    plt.figure(figsize=(12, 8))
    plt.imshow(H,origin='lower', extent=[yedges[0], yedges[-1], xedges[0], xedges[-1]],cmap='jet')
    cbar = plt.colorbar()
    cbar.set_label('Probability density (%)', fontsize=24)
    plt.axhline(y=0, color='white')
    plt.axvline(x=0, color='white')
    plt.xlabel(r'$k_1$ $l_c$', fontsize=24)
    plt.ylabel(r'$k_2$ $l_c$', fontsize=24)
    
    
    xbins = np.linspace(-4005, 400, 1001)  # For curvature_min_times_featuresize
    ybins = np.linspace(-450, 1570, 1001)  # For curvature_max_times_featuresize
    

    
    H, xedges, yedges = np.histogram2d(
    curvature_max_times_featuresize,
    curvature_min_times_featuresize,
    # density=True,  # Replacing normed=True
    bins=[xbins, ybins],
    weights=Areas
    )
    
    # Calculate the bin areas
    bin_area = (xedges[1] - xedges[0]) * (yedges[1] - yedges[0])
    
    # Normalize by bin area to ensure correct probability density
    H = H / (np.sum(H) * bin_area) * 100

    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    plt.imshow(H, origin='lower', extent=[yedges[0], yedges[-1], xedges[0], xedges[-1]], cmap='jet', vmin=0, vmax=1.42)
    cbar = plt.colorbar()
    cbar.set_label('Probability density (%)', fontsize=24)
    plt.axhline(y=0, color='white')
    plt.axvline(x=0, color='white')
    plt.xlabel(r'$k_1$ $l_c$', fontsize=24)
    plt.ylabel(r'$k_2$ $l_c$', fontsize=24)
    plt.show()
        
    
    

