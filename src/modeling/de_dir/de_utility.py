'''
Akond Rahman, Feb 27, 2017
Utility file for running DE
'''
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, accuracy_score, confusion_matrix
import numpy as np
from sklearn import cross_validation


learnerDict = {'CART': [[0.01, 1.00], [2, 20], [1, 20], [1, 50]],
               'RF'  : [[0.01, 1.00], [1, 50], [2, 20], [1, 20], [50, 150]],
               'SVC' : [[]]}


# def giveMeFuncNameOfThisLearner(learnerName):
#   return learnerDict[learnerName][0]



def giveMeLimitsOfThisLearner(learnerName):
  return learnerDict[learnerName]



def getDatasetFromCSV(fileParam, dataTypeFlag=True):
  if dataTypeFlag:
    data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1, dtype='float')
  else:
        data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1,  dtype='str')
  return data_set_to_return




def evalClassifier(actualLabels, predictedLabels):
  '''
    the way skelarn treats is the following: first index -> lower index -> 0 -> 'Low'
                                             next index after first  -> next lower index -> 1 -> 'high'
  '''
  target_labels =  ['N', 'Y']
  '''
    peeking into the labels of the dataset
  '''
  #print "Glimpse at  actual:{}, and predicted:{} labels(10th entry in label list)".format(actualLabels[10], predictedLabels[10])
  #print classification_report(actualLabels, predictedLabels, target_names=target_labels)
  #print">"*25
  '''
  getting the confusion matrix
  '''
  #conf_matr_output = confusion_matrix(actualLabels, predictedLabels)
  #print "Confusion matrix start"
  #print conf_matr_output
  #conf_matr_output = pd.crosstab(actualLabels, predictedLabels, rownames=['True'], colnames=['Predicted'], margins=True)
  #print conf_matr_output
  #print "Confusion matrix end"
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  '''
  the precision score is computed as follows:
  '''
  #prec_ = precision_score(actualLabels, predictedLabels, average='binary')
  #print "The precision score is:", prec_
  #print">"*25
  '''
  the recall score is computed as follows:
  '''
  #recall_ = recall_score(actualLabels, predictedLabels, average='binary')
  #print">"*25
  '''
    are under the curve values .... reff: http://gim.unmc.edu/dxtests/roc3.htm
    0.80~0.90 -> good, any thing less than 0.70 bad , 0.90~1.00 -> excellent
  '''
  #print predictedLabels
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


def perform_cross_validation(classiferP, featuresP, labelsP, cross_vali_param, infoP):
  #print "-----Cross Validation#{}(Start)-----".format(infoP)
  predicted_labels = cross_validation.cross_val_predict(classiferP, featuresP , labelsP, cv=cross_vali_param)
  area_roc_to_ret = evalClassifier(labelsP, predicted_labels)
  #print "-----Cross Validation#{}(End)-----".format(infoP)
  return area_roc_to_ret
