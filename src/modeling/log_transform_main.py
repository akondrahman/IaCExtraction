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
