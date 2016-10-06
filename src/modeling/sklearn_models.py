# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:06:45 2016

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
  


def perform_cross_validation(classiferP, featuresP, labelsP, cross_vali_param):
  print "-----Performing cross validation(start)-----"  
  predicted_labels = cross_validation.cross_val_predict(classiferP, featuresP , labelsP, cv=cross_vali_param)  
  evalClassifier(labelsP, predicted_labels)
  print "-----Performing cross validation(start)-----"  





def performCART(featureParam, labelParam, foldParam):
  theCARTModel = DecisionTreeClassifier()     
  perform_cross_validation(theCARTModel, featureParam, labelParam, foldParam)


def performModeling(features, labels, foldsParam):
  '''
    thsi paper https://www.cs.utah.edu/~piyush/teaching/cross-validation-kohavi.pdf
    with 6000+ citations says to use 10 fold validation , so will use 
    10 fodl validation instaed of bootstrap 
  '''    
  r_, c_ = np.shape(features)
  performCART(features, labels, foldsParam)  

  