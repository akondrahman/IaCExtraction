# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 01:10:02 2016

@author: akond
"""



import numpy as np 
from sklearn.tree import DecisionTreeClassifier 
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
  
  
