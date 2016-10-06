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
  
  
def createSelectedFeatures(allFeatureParam, selectedIndicies):
  feature_dataset_to_ret = [] 
  for ind_ in selectedIndicies:
    features_for_this_index = allFeatureParam[:, ind_]
    feature_dataset_to_ret.append(features_for_this_index)
  ## convert to numpy  array    
  feature_dataset_to_ret = np.array(feature_dataset_to_ret)    
  ## transpose array 
  feature_dataset_to_ret = feature_dataset_to_ret.transpose()    

  return feature_dataset_to_ret     




def giveTimeStamp():
  import time, datetime
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret    