# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:23:09 2016

@author: akond
"""



import warnings
import Utility , numpy as np , sklearn_models
'''
Deprecating warnings will be suppressed 
'''
warnings.filterwarnings("ignore", category=DeprecationWarning) 
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/LOCKED_WIKIMEDIA_23_REPOS_DATASET.csv"
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)
## we will skip the first column, as it has file names 
feature_cols = full_cols - 2  ## the last couln is null , so two colums  to skip 
all_features = full_dataset_from_csv[:, 1:feature_cols]
print "Glimpse at features (10th entry in dataset): \n", all_features[9]
dataset_for_labels = Utility.getDatasetFromCSV(dataset_file, False)
all_labels  =  dataset_for_labels[:, feature_cols]
print "Glimpse at  labels (10th entry in dataset):", all_labels[9]
formatted_labels = Utility.assignNumericLabels(all_labels)
print "Glimpse at  labels (10th entry in label list):", formatted_labels[9]

### use randomized logi. regression to get the features 
selected_indices_for_features = sklearn_models.getElgiibleFeatures(all_features, formatted_labels)
print "The selected indicies are: \n", selected_indices_for_features