# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:23:09 2016

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
selected_indices_for_features = sklearn_models.getElgiibleFeatures(all_features, formatted_labels)
print "The selected indicies are: \n", selected_indices_for_features
print "The selected feature names: ", Utility.printFeatureName(selected_indices_for_features)
print "-"*50
### select the features based on feature indicies 
selected_features = Utility.createSelectedFeatures(all_features, selected_indices_for_features)
print "Selected feature dataset size:", np.shape(selected_features)
print "Glimpse at  selected features (10th entry in label list): \n", selected_features[9]
print "-"*50
'''
    thsi paper https://www.cs.utah.edu/~piyush/teaching/cross-validation-kohavi.pdf
    with 6000+ citations says to use 10 fold validation , so will use 
    10 fold validation instaed of bootstrap 
'''  
fold2Use =10 
'''
Single iteration zone : turn off 'performIterativeModeling()'
while running this 
'''
# this method runs the classifiers once
sklearn_models.performModeling(selected_features, formatted_labels, fold2Use)
print "-"*50
'''
Multiple iteration zone : turn off 'performModeling()'
while running this 
'''
# this method runs the classifiers 'iteration' number of times 
#iteration=1000
#sklearn_models.performIterativeModeling(selected_features, formatted_labels, fold2Use, iteration)
#print "-"*50

print "Ended at:", Utility.giveTimeStamp()