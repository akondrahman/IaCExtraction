# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 01:06:28 2016

@author: akond
"""



import warnings
import Utility , numpy as np , tuned_sklearn_models
print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed 
'''
warnings.filterwarnings("ignore", category=DeprecationWarning) 
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/LOCKED_WIKIMEDIA_23_REPOS_DATASET.csv"
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)