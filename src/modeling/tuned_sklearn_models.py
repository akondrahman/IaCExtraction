# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 01:10:02 2016

@author: akond
"""



import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, accuracy_score




def getElgiibleFeatures(allFeatureParam, allLabelParam):
  '''
    reff for paper : 
    http://scikit-learn.org/stable/modules/feature_selection.html#randomized-l1
    http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RandomizedLogisticRegression.html
  ''' 
   
  logiRegObj = RandomizedLogisticRegression()
  logiRegObj.fit(allFeatureParam, allLabelParam)
  ### Output ###
  #print "Model score: ", logiRegObj.scores_
  eligible_indices = logiRegObj.get_support(indices=True)
  return eligible_indices  
  

def getAreaROC(actualLabelsParam, predictedLabelsParam):
  area_roc_output = roc_auc_score(actualLabelsParam, predictedLabelsParam)
  return area_roc_output    

def perform_cross_validation(classiferP, featuresP, labelsP, cross_vali_param):
  predicted_labels = cross_validation.cross_val_predict(classiferP, featuresP , labelsP, cv=cross_vali_param)  
  area_roc_to_ret = getAreaROC(labelsP, predicted_labels)
  return area_roc_to_ret  

def performTunedKNN(featureParam, labelParam, foldParam, no_neighbors):
  theKNNModel = KNeighborsClassifier(n_neighbors=no_neighbors)    
  knn_area_under_roc = perform_cross_validation(theKNNModel, featureParam, labelParam, foldParam)
  return knn_area_under_roc  
  




def performTunedModeling(features, labels, foldsParam):
  no_of_evals = 100     
  ### lets do knn (nearest neighbor) 