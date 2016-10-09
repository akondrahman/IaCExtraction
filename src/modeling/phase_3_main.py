# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 01:06:28 2016

@author: akond
"""



import warnings
import Utility , numpy as np 
import tuned_sklearn_models
print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed 
'''
warnings.filterwarnings("ignore", category=DeprecationWarning) 
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/LOCKED_WIKIMEDIA_23_REPOS_DATASET.csv"
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)


## we will skip the first column, as it has file names 
feature_cols = full_cols - 2  ## the last couln is null, and have to skip bug count, so two colums  to skip 
all_features = full_dataset_from_csv[:, 1:feature_cols]
print "Glimpse at features (10th entry in dataset): \n", all_features[9]
print "-"*50


dataset_for_labels = Utility.getDatasetFromCSV(dataset_file, False)
label_cols = full_cols - 1
all_labels  =  dataset_for_labels[:, label_cols]
print "Glimpse at  labels (10th entry in dataset):", all_labels[9]
print "-"*50
formatted_labels = Utility.assignNumericLabels(all_labels)
print "Glimpse at  labels (10th entry in label list):", formatted_labels[9]
print "-"*50


### use randomized logi. regression to get the features 
selected_indices_for_features = tuned_sklearn_models.getElgiibleFeatures(all_features, formatted_labels)
print "The selected indicies are: \n", selected_indices_for_features
print "The selected feature names: ", Utility.printFeatureName(selected_indices_for_features)
print "-"*50