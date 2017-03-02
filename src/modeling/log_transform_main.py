'''
Akond Rahman
March 02, 2017
transform metrics
with ln(x+1)
'''



from sklearn.ensemble import ExtraTreesClassifier
from sklearn import decomposition
import Utility , numpy as np , sklearn_models, pandas as pd
glimpseIndex=10
topFeaturesinPCA = 5

def getPCAInsights(pcaParamObj, no_feat_param):
    top_components_index = np.abs(pcaParamObj.components_[no_feat_param]).argsort()[::-1][:topFeaturesinPCA]
    print top_components_index

print "Started at:", Utility.giveTimeStamp()
'''
Deprecating warnings will be suppressed
'''
# dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/SYNTHETIC_MOZ_FULL_DATASET.csv"
# dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/SYNTHETIC_WIKI_FULL_DATASET.csv"
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
