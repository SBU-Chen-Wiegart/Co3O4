#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:04:27 2023

@author: karenchen-wiegart
"""



from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.signal import find_peaks
import os
'''
    #file_name = os.path.basename(f_3d)
    his, bin_edges = np.histogram(crop_norm, bins = 256)   #set range of histogram
    plt.plot(bin_edges[:-1],his)
    peaks, pi = find_peaks(his,height=800000)
    x_axis_peak = []
    for peak in peaks:
        peak_x_axis = bin_edges[peak]
        x_axis_peak.append(peak_x_axis)
    plt.plot(x_axis_peak, his[peaks],'x')
    plt.title(file_name+'_peak')
    plt.savefig('I:\\Chen_Wiegart_09242019_FXI_Backup_2\\Recon_full_xiaoyang_20200224\\Segmentation_xiaoyang_20200224\\histogram_norm_crop\\'+str(file_name))
  
    #his_btw2peaks = his[peaks[0]:peaks[1]] 
    his_btw2peaks = his[peaks[-2]:peaks[-1]]     #y
    #bins_btw2peaks = bin_edges[peaks[0]:peaks[1]]
    bins_btw2peaks = bin_edges[peaks[-2]:peaks[-1]]   #x
    his_btw2peaks_min = np.amin(his_btw2peaks)
    bins_btw2peaks_index = np.where(his_btw2peaks == his_btw2peaks_min)
    threshold = bins_btw2peaks[bins_btw2peaks_index]
    img_seg = np.where(crop_norm < float(threshold), 0, 255)
    plt.show()
    io.imsave('I:\\Chen_Wiegart_09242019_FXI_Backup_2\\Recon_full_xiaoyang_20200224\\Segmentation_xiaoyang_20200224\\seg\\'+str(file_name)+'_seg'+str(threshold)+'_'+str(file_name),img_seg)
    '''
    
file='NI20Cr_LICl-KCl_500C_air/53215.tiff'
img = io.imread(file)
file_name = os.path.basename(file)
#print(img.shape)
#print(img.dtype)
hist, bin_edges = np.histogram(img, bins = 256)   #set range of histogram
plt.plot(bin_edges[:-1],hist)
#plt.show()
peaks, pi = find_peaks(hist,height=100000)
selected_peaks=peaks[hist[peaks]<1000000]
#print(selected_peaks,pi)
x_axis_selected_peak = []
for peak in selected_peaks:
    peak_x_axis = bin_edges[peak]
    x_axis_selected_peak.append(peak_x_axis)
plt.plot(x_axis_selected_peak, hist[selected_peaks],'x')
plt.title(file_name+'_peak')
plt.savefig('NI20Cr_LICl-KCl_500C_air/peak_plot/'+str(file_name))
    
    #his_btw2peaks = his[peaks[0]:peaks[1]] 
his_btw2peaks = hist[selected_peaks[-2]:selected_peaks[-1]]  
#print(his_btw2peaks)
    #bins_btw2peaks = bin_edges[peaks[0]:peaks[1]]
bins_btw2peaks = bin_edges[selected_peaks[-2]:selected_peaks[-1]] 
#print(bins_btw2peaks)
his_btw2peaks_min = np.amin(his_btw2peaks)
bins_btw2peaks_index = np.where(his_btw2peaks == his_btw2peaks_min)
#print(bins_btw2peaks_index)
threshold = bins_btw2peaks[bins_btw2peaks_index]
#print(threshold)
img_seg = np.where(img < float(threshold), 0, 255)
#plt.show()
img_seg_float=img_seg.astype(np.float32)
img_seg_float_crop=img_seg_float[4:227, :, :]
volume_cal=np.sum(img_seg_float_crop)
#volume_ratio=volume_cal/(364*391*223*256)
print(volume_cal)
#print(volume_ratio)
io.imsave('NI20Cr_LICl-KCl_500C_air/img_seg/'+str(file_name)+'_seg'+str(threshold)+'_'+str(file_name),img_seg_float_crop)