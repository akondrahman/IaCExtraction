# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:05:36 2016

@author: akond
"""



import warnings
import Utility , numpy as np , sklearn_models
print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed 
'''
warnings.filterwarnings("ignore", category=DeprecationWarning) 
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/LOCKED_WIKIMEDIA_23_REPOS_DATASET.csv"
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)