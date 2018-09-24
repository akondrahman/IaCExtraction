'''
Akond Rahman
March 02, 2017
transform metrics
with ln(x+1)
'''
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import decomposition
import Utility , numpy as np , sklearn_models, pandas as pd
glimpseIndex        = 10

def getPCAInsights(pcaParamObj, no_of_pca_comp_to_see):
    top_components_index = np.abs(pcaParamObj.components_[no_of_pca_comp_to_see]).argsort()[::-1][:topFeaturesinPCA]
    print top_components_index

print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed
'''

# dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_MIR.csv"
# no_features_to_use = 1
# dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_MOZ.csv"
# no_features_to_use = 1
# dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_OST.csv"
# no_features_to_use = 2
# dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_WIK.csv"
# no_features_to_use = 2

topFeaturesinPCA    = 3
pca_comp_to_analyze = 10


'''
For size-only prediction model

dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/JUST_SIZE/MIR.csv"
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/JUST_SIZE/MOZ.csv"
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/JUST_SIZE/OST.csv"
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/JUST_SIZE/WIK.csv"

topFeaturesinPCA    = 1
pca_comp_to_analyze = 1
no_features_to_use = 1

'''

print "The dataset is:", dataset_file
print "-"*50
full_dataset_from_csv = Utility.getDatasetFromCSV(dataset_file)
full_rows, full_cols = np.shape(full_dataset_from_csv)
print "Total number of columns", full_cols
## we will skip the first column, as it has file names
feature_cols = full_cols - 1  ## the last column is defect status, so one column to skip
all_features = full_dataset_from_csv[:, 2:feature_cols]
print "Glimpse at features (11th entry in dataset): \n", all_features[glimpseIndex]
print "-"*50

dataset_for_labels = Utility.getDatasetFromCSV(dataset_file)  ## unlike phase-1, the labels are '1' and '0', so need to take input as str
label_cols = full_cols - 1
all_labels  =  dataset_for_labels[:, label_cols]
print "Glimpse at  labels (11th entry in dataset):", all_labels[glimpseIndex]
print "-"*50

defected_file_count     = len([x_ for x_ in all_labels if x_==1.0])
non_defected_file_count = len([x_ for x_ in all_labels if x_==0.0])
print "No of. defects={}, non-defects={}".format(defected_file_count, non_defected_file_count)
print "-"*50


'''
lets transform all the features via log transformation
'''
selected_features = Utility.createLogTransformedFeatures(all_features)
print "Selected (log-transformed) feature dataset size:", np.shape(selected_features)
print "Glimpse at (log-transformed) selected features(10th entry in label list): \n", selected_features[glimpseIndex]
print "-"*50
feature_input_for_pca = all_features
pcaObj = decomposition.PCA(n_components=pca_comp_to_analyze)
pcaObj.fit(feature_input_for_pca)
# how much variance is explained each component
variance_ratio_of_features = pcaObj.explained_variance_ratio_
for index_ in xrange(len(variance_ratio_of_features)):
    print "Principal component#{}, explained variance:{}".format(index_+1, variance_ratio_of_features[index_])
print "-"*50
# see how much explained variance is covered by the number of compoenents , and set the number
print "Of all the features, we will use:", no_features_to_use
print "-"*50
pcaObj.n_components=no_features_to_use
selected_features = pcaObj.fit_transform(all_features)
print "Selected feature dataset size:", np.shape(selected_features)
print "-"*50
sklearn_models.performIterativeModeling(selected_features, all_labels, 10, 10)
print "-"*50
print "The dataset is:",dataset_file
print "-"*50
print "Ended at:", Utility.giveTimeStamp()
