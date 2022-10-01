# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:50:43 2022

@author: angel
"""
import numpy as np 
import csv

M = np.deg2rad(5)
E = [M]
ecc = 0.100
err_arr = [0.0]
i=0
while True :
    E_new =M+(ecc*np.sin(E[i]))
    err = (E_new-E[i])/(E_new)
    acc = E_new-E[i]
    E.append(E_new)
    err_arr.append(err)
    i+=1
    
    if np.rad2deg(acc)<0.000001:
        break
    
with open('module05-prob01-output.csv', mode='w') as output:
    output_writer = csv.writer(output)
    output_writer.writerow(["E_i", "Relative Error"])
    for i in range(0,len(E)):
        output_writer.writerow([E[i],err_arr[i]])
    
    