# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15, 2016

@author: akond
"""



import warnings
import Utility , numpy as np , sklearn_models
glimpseIndex=10
print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed 
'''
warnings.filterwarnings("ignore", category=DeprecationWarning) 
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/wikimedia_vagrant_steroided_full.csv"
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)
## we will skip the first column, as it has file names 
feature_cols = full_cols - 2  ## the last couln is null, and have to skip bug count, so two colums  to skip 
all_features = full_dataset_from_csv[:, 1:feature_cols]
print "Glimpse at features (11th entry in dataset): \n", all_features[glimpseIndex]
print "-"*50
dataset_for_labels = Utility.getDatasetFromCSV(dataset_file)  ## unlike phase-1, the labels are '1' and '0', so need to take input as str
label_cols = full_cols - 1   
all_labels  =  dataset_for_labels[:, label_cols]
print "Glimpse at  labels (11th entry in dataset):", all_labels[glimpseIndex]
print "-"*50
### use l1-penalized logi. regression to get teh features 
selected_indices_for_features = sklearn_models.performPenalizedLogiRegression(all_features, all_labels)
### use randomized logi. regression to get the features ::: as this performs worse then l1-penalized , it wil not be used 
# selected_indices_for_features = sklearn_models.getElgiibleFeatures(all_features, all_labels)
print "Total selected feature count:", len(selected_indices_for_features)
print "The selected feature names: ", Utility.printFeatureName(selected_indices_for_features, True) ##True for enbaling steroid headers
print "-"*50
### select the features based on feature indicies 
selected_features = Utility.createSelectedFeatures(all_features, selected_indices_for_features)
print "Selected feature dataset size:", np.shape(selected_features)
print "Glimpse at  selected features (11th entry in label list): \n", selected_features[glimpseIndex]
print "-"*50
fold2Use =10 
'''
Single iteration zone : turn off 'performIterativeModeling()'
while running this 
'''
# this method runs the classifiers once
sklearn_models.performModeling(selected_features, all_labels, fold2Use)
print "-"*50
print "Ended at:", Utility.giveTimeStamp()