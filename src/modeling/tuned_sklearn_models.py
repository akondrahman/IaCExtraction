# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 01:10:02 2016

@author: akond
"""



import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.tree import DecisionTreeClassifier 




def getDetailedReport(actualLabels, predictedLabels):  
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
  print">"*10
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  '''
    are under the curve values .... reff: http://gim.unmc.edu/dxtests/roc3.htm 
    0.80~0.90 -> good, any thing less than 0.70 bad , 0.90~1.00 -> excellent 
  '''
  area_roc_output = roc_auc_score(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  #print "Area under the ROC curve is ", area_roc_output
  #print">"*10  
  '''
    mean absolute error (mae) values .... reff: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html
    the smaller the better , ideally expect 0.0 
  '''
  #mae_output = mean_absolute_error(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  #print "Mean absolute errro output  is ", mae_output  
  #print">"*25    
  '''
  accuracy_score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions 
  ideally 1.0, higher the better 
  '''
  #accuracy_score_output = accuracy_score(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  #print "Accuracy output  is ", accuracy_score_output   
  #print">"*10
  '''
    this function returns area under the curve , which will be used 
    for D.E. and repated measurements 
  '''
  return area_roc_output

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
  
  
  
def getBestParamCombo(dictParam):
  #print dictParam    
  sorted_keys =sorted(dictParam, reverse=True) 
  top_key = sorted_keys[0]
  top_val = dictParam[top_key] 
  # the param that gave the best value, and the best value aka best area under ROC      
  return top_val, top_key 
    


def getAreaROC(actualLabelsParam, predictedLabelsParam):
  area_roc_output = roc_auc_score(actualLabelsParam, predictedLabelsParam)
  return area_roc_output    


def perform_cross_validation_for_tuning(classiferP, featuresP, labelsP, cross_vali_param):
  predicted_labels = cross_validation.cross_val_predict(classiferP, featuresP , labelsP, cv=cross_vali_param)  
  area_roc_to_ret = getAreaROC(labelsP, predicted_labels)
  return area_roc_to_ret  

def performTunedKNN(featureParam, labelParam, foldParam, no_neighbors):
  res_holder = {}     
  for neighbor2test in no_neighbors:    
    theKNNModel = KNeighborsClassifier(n_neighbors=neighbor2test)    
    knn_area_under_roc = perform_cross_validation_for_tuning(theKNNModel, featureParam, labelParam, foldParam)
    res_holder[knn_area_under_roc] = neighbor2test # the key is the area_under_roc value, we will sort by this value
  bestTuple = getBestParamCombo(res_holder)      
  return bestTuple


def perform_cross_validation(classiferP, featuresP, labelsP, cross_vali_param, infoP):
  print "-----Cross Validation#{}(Start)-----".format(infoP)  
  predicted_labels = cross_validation.cross_val_predict(classiferP, featuresP , labelsP, cv=cross_vali_param)  
  area_roc_to_ret = getDetailedReport(labelsP, predicted_labels)
  print "-----Cross Validation#{}(End)-----".format(infoP) 
  return area_roc_to_ret  

  


def performKNN(featureParam, labelParam, foldParam, infoP, no_of_neighbor_param):
  theKNNModel = KNeighborsClassifier(n_neighbors = no_of_neighbor_param)    
  knn_area_under_roc = perform_cross_validation(theKNNModel, featureParam, labelParam, foldParam, infoP)
  print "For {}, area under ROC is: {}".format(infoP, knn_area_under_roc)  
  return knn_area_under_roc    





def performedTunedCART(featureParam, labelParam, foldParam, paramComboParam):
  resHolder={} 
  max_feat_for_cart_param      = paramComboParam[0]
  min_sam_split_for_cart_param = paramComboParam[1]
  min_sam_leaf_for_cart_param  = paramComboParam[2]
  max_depth_for_cart_param     = paramComboParam[3]
  for max_feat in max_feat_for_cart_param:
    for  min_sam_split in min_sam_split_for_cart_param:
      for min_sam_leaf  in min_sam_leaf_for_cart_param:
        for max_depth_ in max_depth_for_cart_param:
          theCARTModel = DecisionTreeClassifier(max_features=max_feat, min_samples_split=min_sam_split, min_samples_leaf=min_sam_leaf, max_depth=max_depth_)     
          cart_area_under_roc = perform_cross_validation_for_tuning(theCARTModel, featureParam, labelParam, foldParam)
          resHolder[cart_area_under_roc] = (max_feat, min_sam_split, min_sam_leaf, max_depth_) 
  bestTuple = getBestParamCombo(resHolder)      
  return bestTuple





def performCART(featureParam, labelParam, foldParam, infoP, optimalParam_):
  max_feat      = optimalParam_[0]
  min_sam_split = optimalParam_[1]      
  min_sam_leaf  = optimalParam_[2]  
  max_depth_    = optimalParam_[3]  
  theCARTModel = DecisionTreeClassifier(max_features=max_feat, min_samples_split=min_sam_split, min_samples_leaf=min_sam_leaf, max_depth=max_depth_)     
  cart_area_under_roc = perform_cross_validation(theCARTModel, featureParam, labelParam, foldParam, infoP)
  print "For {}, area under ROC is: {}".format(infoP, cart_area_under_roc) 
  return cart_area_under_roc  


def performTunedModeling(features, labels, foldsParam):
  ### lets do knn (nearest neighbor) 
  #no_neighbors_to_test = [1, 5, 9, 13, 17] ## from Hassan-ICSE'16 Paper
  no_neighbors_to_test = [x1 + 1 for x1 in xrange(100)] ## just for testing   
  optimalParam, optimalVal =  performTunedKNN(features, labels, foldsParam, no_neighbors_to_test)  
  print "For kNN, best parameter was:{}, AUC was:{}".format(optimalParam, optimalVal)  
  print "-"*50  
  performKNN(features, labels, foldsParam, "kNN", optimalParam)
  optimalParam, optimalVal = 0, 0  
  print "-"*50  
  
  ### lets do CART
  # param-1
  max_feat_for_cart        = [(float(x_)/float(100)) + 0.01 for x_ in xrange(100) ] #from Fu paper 2016 
  # param-2
  min_sam_split_for_cart   = [ x_+1                         for x_ in xrange(20)  ] #from Fu paper 2016 
  min_sam_split_for_cart.remove(1) # remove 1 to get the list [2, 20] from Fu paper 2016 
  # param-3    
  min_sam_leaf_for_cart    = [ x_+1                         for x_ in xrange(20)  ] #from Fu paper 2016 
  # param-4 
  max_depth_for_cart       = [ x_+1                         for x_ in xrange(50)  ] #from Fu paper 2016  
  ## supply all param combos as tuple 
  param_combo_tuple = ( max_feat_for_cart, min_sam_split_for_cart, min_sam_leaf_for_cart, max_depth_for_cart )   
  #optimalParam, optimalVal = performedTunedCART(features , labels, foldsParam,  param_combo_tuple)  
  #print "For CART, best parameter was:{}, AUC was:{}".format(optimalParam, optimalVal) 
  print "-"*50 
  optimalParam = (0.33, 20, 16, 1)
  performCART(features, labels, foldsParam, "CART" , optimalParam)   
  print "-"*50  