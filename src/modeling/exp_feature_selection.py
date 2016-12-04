# -*- coding: utf-8 -*-
"""
Created on Sat Dec 04, 2016

"""




from sklearn import decomposition
import Utility , numpy as np , sklearn_models
glimpseIndex=10
print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed
'''
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


pcaObj = decomposition.PCA()
pcaObj.fit(all_features)
variance_of_features = pcaObj.explained_variance_
print variance_of_features
print "-"*50
selective_feature_indices = [x_ for x_ in variance_of_features if x_ > float(1) ]
no_features_to_use = len(selective_feature_indices)
print "Of all the features, we will use:", no_features_to_use
pcaObj.n_components=no_features_to_use
selected_features = pcaObj.fit_transform(all_features)
print "Shape of transformed data:", selected_features.shape
print "Transformed features: \n", selected_features
print "-"*50
