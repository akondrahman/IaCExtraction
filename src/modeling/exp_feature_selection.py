# -*- coding: utf-8 -*-
"""
Created on Sat Dec 04, 2016

"""




from sklearn.ensemble import ExtraTreesClassifier
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
'''
Which experiment would you conduct? 1 for PCA
'''
exp_flag = 2
selected_features = None
if exp_flag==1:
    '''
    PCA reff:
    1. http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.fit
    2. http://scikit-learn.org/dev/tutorial/statistical_inference/unsupervised_learning.html#principal-component-analysis-pca
    '''
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
    print "Selected feature dataset size:", np.shape(selected_features)
elif exp_flag==2:
    '''
    Ranking based feature selection 
    '''
    forestForFeatureSelection = ExtraTreesClassifier()
    forestForFeatureSelection.fit(all_features, all_labels)
    importances = forestForFeatureSelection.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forestForFeatureSelection.estimators_], axis=0)
    indices = np.argsort(importances)[::-1]
    #print "Feature ranking:"
    #for ind_ in range(all_features.shape[1]):
    #  print ("%d. feature %d (%f)" % (ind_ + 1, indices[ind_], importances[indices[ind_]]))
    selected_indices_for_features = [8, 24, 9, 59, 18, 10, 26, 0, 60, 25, 15, 28, 41, 30, 32, 21, 58, 2, 23, 6]
    selected_features = Utility.createSelectedFeatures(all_features, selected_indices_for_features)
    print "Selected feature dataset size:", np.shape(selected_features)


print "-"*50
print "Shape of transformed data:", selected_features.shape
print "Transformed features: \n", selected_features
print "-"*50
sklearn_models.performModeling(selected_features, all_labels, 10)
print "-"*50
