# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:59:30 2018

@author: AdilDSW
"""

import h5py
f = h5py.File('C:\\Users\\AdilDSW\\Downloads\\GLAH12_634_1102_001_0071_0_01_0001.H5', 'r')
print("Keys: %s" % f.keys())
a_group_key = list(f.keys())[4]
data = list(f[a_group_key])
data1 = list(f[a_group_key][data][0])
img=[[0 for i in range(1000)] for j in range(700)]
for i in range(700):
    for j in range(1000):
        img[i][j]=data1[i][j][0]
        

