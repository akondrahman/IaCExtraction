# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:06:45 2016

@author: akond
"""



import numpy as np 
from sklearn.tree import DecisionTreeClassifier 
from sklearn import cross_validation
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, accuracy_score

def evalClassifier(actualLabels, predictedLabels):  
  '''
    the way skelarn treats is the following: first index -> lower index -> 0 -> 'Low'
                                             next index after first  -> next lower index -> 1 -> 'high'    
  '''
  target_labels =  ['N', 'Y']
  '''
    peeking into the labels of the dataset 
  '''
  print "Glimpse at  actual:{}, and predicted:{} labels(10th entry in label list)".format(actualLabels[9], predictedLabels[9])
  print "precison, recall, F-stat"
  print classification_report(actualLabels, predictedLabels, target_names=target_labels)
  print"*"*25
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  '''
    are under the curve values .... reff: http://gim.unmc.edu/dxtests/roc3.htm 
    0.80~0.90 -> good, any thing less than 0.70 bad , 0.90~1.00 -> excellent 
  '''
  area_roc_output = roc_auc_score(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  print "Area under the ROC curve is ", area_roc_output
  print"*"*25  
  '''
    mean absolute error (mae) values .... reff: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html
    the smaller the better , ideally expect 0.0 
  '''
  mae_output = mean_absolute_error(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  print "Mean absolute errro output  is ", mae_output  
  print"*"*25    
  '''
  accuracy_score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions 
  ideally 1.0, higher the better 
  '''
  accuracy_score_output = accuracy_score(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  print "Accuracy output  is ", accuracy_score_output   
  print"*"*25  





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
  print "-----Performing cross validation(end)-----"  






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
  ### lets do CART (decision tree)
  performCART(features, labels, foldsParam)  

  ### lets do knn (nearest neighbor)
  performKNN(features, labels, foldsParam)  