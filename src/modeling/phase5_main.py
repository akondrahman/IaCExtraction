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
all_features = full_dataset_from_csv[:, 1:feature_cols]
feature_cols = full_cols - 2  ## the last couln is null, and have to skip bug count, so two colums  to skip

print "Glimpse at features (11th entry in dataset): \n", all_features[glimpseIndex]
print "-"*50
print "Ended at:", Utility.giveTimeStamp()
