'''
cross organization
defect prediction
'''
from sklearn import decomposition
import Utility , numpy as np , cross_org_sklearn_models, pandas as pd
glimpseIndex = 10
top_compo    = 5
pcasToDo     = 10
def getPCAInsights(pcaParamObj, no_feat_param):
    top_components_index = np.abs(pcaParamObj.components_[no_feat_param]).argsort()[::-1][:top_compo]
    print top_components_index


print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed
'''
mozilla_file   = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/SYNTHETIC_MOZ_FULL_DATASET.csv"
wikimedia_file = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/SYNTHETIC_WIKI_FULL_DATASET.csv"

full_dataset_from_csv = Utility.getDatasetFromCSV(mozilla_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)
print "Total number of columns", full_cols
## we will skip the first column, as it has file names
feature_cols = full_cols - 1  ## the last column is defect status, so one column to skip
all_features = full_dataset_from_csv[:, 2:feature_cols]
print "Glimpse at features (11th entry in dataset): \n", all_features[glimpseIndex]
print "-"*50
wikimedia_dataset = Utility.getDatasetFromCSV(wikimedia_file)  ## unlike phase-1, the labels are '1' and '0', so need to take input as str
label_cols = full_cols - 1
wikimedia_labels  =  wikimedia_dataset[:, label_cols]
print "Glimpse at mozilla labels (11th entry in dataset):", wikimedia_labels[glimpseIndex]
print "-"*50
pcaObj = decomposition.PCA(n_components=pcasToDo)
pcaObj.fit(all_features)
# variance of features
variance_of_features = pcaObj.explained_variance_
# how much variance is explained each component
variance_ratio_of_features = pcaObj.explained_variance_ratio_
for index_ in xrange(len(variance_ratio_of_features)):
    print "Principal component#{}, explained variance:{}".format(index_+1, variance_ratio_of_features[index_])
#print variance_ratio_of_features
print "-"*50
no_features_to_use = 5 #using one PCA you get lesser accuracy
pcaObj.n_components=no_features_to_use
selected_features = pcaObj.fit_transform(all_features)
print "Selected feature dataset size:", np.shape(selected_features)
print "-"*50
getPCAInsights(pcaObj, 1)
print "-"*50
#cross_org_sklearn_models.performModeling(selected_features, wikimedia_labels)
# sklearn_models.performModeling(selected_features, all_labels, 10)
# print "-"*50
print "The trainer:{} \n trainee:{}".format(mozilla_file, wikimedia_file)
print "-"*50
