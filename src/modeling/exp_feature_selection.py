# -*- coding: utf-8 -*-
"""
Created on Sat Dec 04, 2016

"""




from sklearn.ensemble import ExtraTreesClassifier
from sklearn import decomposition
import Utility , numpy as np , sklearn_models, pandas as pd
glimpseIndex=10

def getPCAInsights(pcaParamObj, no_feat_param):
    '''
    reff-1: http://stackoverflow.com/questions/22348668/pca-decomposition-with-python-features-relevances
    reff-2: http://stackoverflow.com/questions/22984335/recovering-features-names-of-explained-variance-ratio-in-pca-with-sklearn
    '''
    #print pd.DataFrame(pcaParamObj.components_)
    top_three_components_index = np.abs(pcaParamObj.components_[no_feat_param]).argsort()[::-1][:3]
    print top_three_components_index
    #for row_ in pcaParamObj.components_:
    #    print row_
    #    print "~"*25




print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed
'''
#dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/REDACTED_WIKI_DATASET.csv"
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/SYNTHETIC_MOZ_FULL_DATASET.csv"
print "The dataset is:", dataset_file
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)
print "Total number of columns", full_cols
## we will skip the first column, as it has file names
feature_cols = full_cols - 1  ## the last column is defect status, so one column to skip
all_features = full_dataset_from_csv[:, 2:feature_cols]
print "Glimpse at features (11th entry in dataset): \n", all_features[glimpseIndex]
print "-"*50
# only_churn_features = full_dataset_from_csv[:, 38:feature_cols]
# print "Glimpse at churn features (11th entry in dataset): \n", only_churn_features[glimpseIndex]
# print "-"*50
# only_lint_features = full_dataset_from_csv[:, 38:42]
# print "Glimpse at lint features (11th entry in dataset): \n", only_lint_features[glimpseIndex]
# print "-"*50
dataset_for_labels = Utility.getDatasetFromCSV(dataset_file)  ## unlike phase-1, the labels are '1' and '0', so need to take input as str
label_cols = full_cols - 1
all_labels  =  dataset_for_labels[:, label_cols]
print "Glimpse at  labels (11th entry in dataset):", all_labels[glimpseIndex]
print "-"*50
# only_pupp_features = full_dataset_from_csv[:, 1:38]
# print "Glimpse at Puppet-specific features (11th entry in dataset): \n", only_pupp_features[glimpseIndex]
# print "-"*50
defected_file_count     = len([x_ for x_ in all_labels if x_==1.0])
non_defected_file_count = len([x_ for x_ in all_labels if x_==0.0])
print "No of. defects={}, non-defects={}".format(defected_file_count, non_defected_file_count)
print "-"*50
'''
Which experiment would you conduct? 1 for PCA
'''
exp_flag = 1
feature_input_for_pca = all_features
pca_comp              = 15
selected_features = None
if exp_flag==1:
    '''
    PCA reff:
    1. http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.fit
    2. http://scikit-learn.org/dev/tutorial/statistical_inference/unsupervised_learning.html#principal-component-analysis-pca
    '''
    pcaObj = decomposition.PCA(n_components=pca_comp)
    pcaObj.fit(feature_input_for_pca)
    # variance of features
    variance_of_features = pcaObj.explained_variance_
    # how much variance is explained each component
    variance_ratio_of_features = pcaObj.explained_variance_ratio_
    print "Explained varaince ratio"
    for index_ in xrange(len(variance_ratio_of_features)):
        print "Principal component#{}, explained variance:{}".format(index_+1, variance_ratio_of_features[index_])
    #print variance_ratio_of_features
    print "-"*50
    selective_feature_indices = [x_ for x_ in variance_of_features if x_ > float(1) ]
    no_features_to_use = len(selective_feature_indices)
    # see how much explained variance is covered by the number of compoenents , and set the number
    no_features_to_use = 5 #using one PCA you get lesser accuracy
    print "Of all the features, we will use:", no_features_to_use
    print "-"*50
    pcaObj.n_components=no_features_to_use
    selected_features = pcaObj.fit_transform(feature_input_for_pca)
    print "Selected feature dataset size:", np.shape(selected_features)
    print "-"*50
    pca_insight = getPCAInsights(pcaObj, 1)
    print  pca_insight
    print "-"*50

print "-"*50
print "Shape of transformed data:", selected_features.shape
#print "Transformed features: \n", selected_features
print "-"*50
# sklearn_models.performModeling(selected_features, all_labels, 10)
# print "-"*50
sklearn_models.performIterativeModeling(selected_features, all_labels, 10, 100)
print "-"*50
