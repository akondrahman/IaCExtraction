# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:23:09 2016

@author: akond
"""



import IO_Utility , numpy as np 
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/LOCKED_WIKIMEDIA_23_REPOS_DATASET.csv"
full_dataset_from_csv = IO_Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)
## we will skip the first column, as it has file names 
feature_cols = full_cols - 2  ## the last couln is null , so two colums  to skip 
all_features = full_dataset_from_csv[:, 1:feature_cols]
print "Glimpse at features (10th entry in dataset): \n", all_features[9]
dataset_for_labels = IO_Utility.getDatasetFromCSV(dataset_file, False)
all_labels  =  dataset_for_labels[:, full_cols - 2]
print "All labels: \n", all_labels