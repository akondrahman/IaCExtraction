# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:06:45 2016

@author: akond
"""



import numpy as np 
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
  
def performModeling(features, labels, iterations):
  '''
    thsi paper https://www.cs.utah.edu/~piyush/teaching/cross-validation-kohavi.pdf
    with 6000+ citations says to use 10 fold validation , so will use 
    10 fodl validation instaed of bootstrap 
  '''    
  r_, c_ = np.shape(features)
  