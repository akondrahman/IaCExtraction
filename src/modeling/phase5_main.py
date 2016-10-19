# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19, 2016

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
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/wikimedia_vagrant_ninety_metrics_full.csv"
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)
## we will skip the first column, as it has file names
feature_cols = full_cols - 3  ## the last couln is null, and have to skip bug count, so two colums  to skip
all_features = full_dataset_from_csv[:, 1:feature_cols]
print "Glimpse at features (11th entry in dataset): \n", all_features[glimpseIndex]
print "-"*50
dataset_for_labels = Utility.getDatasetFromCSV(dataset_file)  ## unlike phase-1, the labels are '1' and '0', so need to take input as str
label_cols = full_cols - 2
all_labels  =  dataset_for_labels[:, label_cols]
print "Glimpse at  labels (11th entry in dataset):", all_labels[glimpseIndex]
print "-"*50
### use l1-penalized logi. regression to get teh features
selected_indices_for_features = sklearn_models.performPenalizedLogiRegression(all_features, all_labels)
print "Total selected feature count:", len(selected_indices_for_features)
print "The selected feature names: ", Utility.printNinetyMetricFeatureName(selected_indices_for_features) ## different menthod than phase-4
print "-"*50
print "Ended at:", Utility.giveTimeStamp()
