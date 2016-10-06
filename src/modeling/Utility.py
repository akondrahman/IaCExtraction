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
  
  
 
def assignNumericLabels(labelListParam):
  y_cnt = 0 
  n_cnt = 0 
  label_list = []  
  for label_ in labelListParam:
   if label_=='Y':
     label_list.append(1)
     y_cnt = y_cnt + 1 
   else:
     label_list.append(0)
     n_cnt = n_cnt + 1   
  print "before: {}, after:{}, yes:{}, no:{}".format(len(labelListParam), len(label_list), y_cnt, n_cnt)
  return label_list     