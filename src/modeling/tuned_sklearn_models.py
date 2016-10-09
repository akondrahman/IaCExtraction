# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 01:10:02 2016

@author: akond
"""



import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
from sklearn.linear_model import RandomizedLogisticRegression

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
  

def performTunedKNN(featureParam, labelParam, foldParam, infoP, no_neighbors):
  theKNNModel = KNeighborsClassifier()    
  knn_area_under_roc = perform_cross_validation(theKNNModel, featureParam, labelParam, foldParam, infoP)
  print "For {}, area under ROC is: {}".format(infoP, knn_area_under_roc)  
  return knn_area_under_roc  
  
def performTunedModeling(features, labels, foldsParam):
  ### lets do knn (nearest neighbor)
  performTunedKNN(features, labels, foldsParam, "KNN")       