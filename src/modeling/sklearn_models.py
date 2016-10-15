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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model


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
  

def perform_cross_validation(classiferP, featuresP, labelsP, cross_vali_param, infoP):
  print "-----Cross Validation#{}(Start)-----".format(infoP)  
  predicted_labels = cross_validation.cross_val_predict(classiferP, featuresP , labelsP, cv=cross_vali_param)  
  area_roc_to_ret = evalClassifier(labelsP, predicted_labels)
  print "-----Cross Validation#{}(End)-----".format(infoP) 
  return area_roc_to_ret  




def performCART(featureParam, labelParam, foldParam, infoP):
  theCARTModel = DecisionTreeClassifier()     
  cart_area_under_roc = perform_cross_validation(theCARTModel, featureParam, labelParam, foldParam, infoP)
  print "For {}, area under ROC is: {}".format(infoP, cart_area_under_roc) 
  return cart_area_under_roc  
  




def performKNN(featureParam, labelParam, foldParam, infoP):
  theKNNModel = KNeighborsClassifier()    
  knn_area_under_roc = perform_cross_validation(theKNNModel, featureParam, labelParam, foldParam, infoP)
  print "For {}, area under ROC is: {}".format(infoP, knn_area_under_roc)  
  return knn_area_under_roc  





def performRF(featureParam, labelParam, foldParam, infoP):
  theRndForestModel = RandomForestClassifier() 
  rf_area_under_roc = perform_cross_validation(theRndForestModel, featureParam, labelParam, foldParam, infoP)  
  print "For {} area under ROC is: {}".format(infoP, rf_area_under_roc)
  return rf_area_under_roc  





def performModeling(features, labels, foldsParam):  
  #r_, c_ = np.shape(features)
  ### lets do CART (decision tree)
  performCART(features, labels, foldsParam, "CART")  

  ### lets do knn (nearest neighbor)
  performKNN(features, labels, foldsParam, "KNN") 
  
  ### lets do RF (ensemble method: random forest)
  performRF(features, labels, foldsParam, "RF")   
  
  
  


def performIterativeModeling(featureParam, labelParam, foldParam, iterationP):
  holder_cart = []
  holder_knn  = []
  holder_rf   = []  
  for ind_ in xrange(iterationP):
    ## iterative modeling for CART  
    cart_area_roc = performCART(featureParam, labelParam, foldParam, "CART")
    holder_cart.append(cart_area_roc)
    cart_area_roc = float(0)
      
    ## iterative modeling for KNN  
    knn_area_roc = performKNN(featureParam, labelParam, foldParam, "K-NN")
    holder_knn.append(knn_area_roc)
    knn_area_roc = float(0) 
    

    ## iterative modeling for RF  
    rf_area_roc = performRF(featureParam, labelParam, foldParam, "Rand. Forest")
    holder_rf.append(rf_area_roc)
    rf_area_roc = float(0) 
    
  print "-"*50      
  print "Summary: AUC, for:{}, mean:{}, median:{}, max:{}, min:{}".format("CART", np.mean(holder_cart),
                                                                          np.median(holder_cart), max(holder_cart), 
                                                                          min(holder_cart))   
  print "-"*50                                                                          
  print "Summary: AUC, for:{}, mean:{}, median:{}, max:{}, min:{}".format("K-NN", np.mean(holder_knn),
                                                                          np.median(holder_knn), max(holder_knn), 
                                                                          min(holder_knn))  
  print "-"*50                                                                           
  
  print "Summary: AUC, for:{}, mean:{}, median:{}, max:{}, min:{}".format("Rand. Forest", np.mean(holder_rf),
                                                                          np.median(holder_rf), max(holder_rf), 
                                                                          min(holder_rf))  
  print "-"*50      





def performPenalizedLogiRegression(allFeatureParam, allLabelParam):
  feat_index_to_ret = [] 
  index_ = 0   
  '''
    See Hoa MSR 2015 paper for reference 
  '''  
  print "<------------ Performing Logistic Regression ------------->"

  logisticRModel = linear_model.LogisticRegression(C=1e5,  penalty='l1')
  ### if you dont fit , you will get an error 
  logisticRModel.fit(allFeatureParam, allLabelParam)
  print "Output of score (mean accuracy) "
  print logisticRModel.score(allFeatureParam, allLabelParam)
  feature_coeffs = logisticRModel.coef_[0]  ## output from logi. reg is list of lists  
  print "Output of co-efficients ={}".format(feature_coeffs)
  for x_ in np.nditer(feature_coeffs):
    if (x_ != float(0)):
      feat_index_to_ret.append(index_)  
    index_ = index_ + 1          
  #print "Output of intercept ={}, n_iter_ = {} ".format(logisticRModel.intercept_, logisticRModel.n_iter_)
  return feat_index_to_ret    