# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:06:45 2016

@author: akond
"""



from sklearn.linear_model import RandomizedLogisticRegression
def getElgiibleFeatures(allFeatureParam, allLabelParam):
  logiRegObj = RandomizedLogisticRegression()
  logiRegObj.fit(allFeatureParam, allLabelParam)
  ### Output ###
  #print "Model score: ", logiRegObj.scores_
  eligible_indices = logiRegObj.get_support(indices=True)
  return eligible_indices  