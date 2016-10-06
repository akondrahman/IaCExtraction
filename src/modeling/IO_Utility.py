# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:53:19 2016

@author: akond
"""



import numpy as np 
def getDatasetFromCSV(fileParam, trainFlag=True): 
  if trainFlag:    
    data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1, dtype='float')
  else:
        data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1,  dtype='str')      
  return data_set_to_return  