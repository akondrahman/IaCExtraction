'''
main script to call DE for parameter tuning
of statistical learners
Akond Rahman
Feb 23, 2017
'''
no_of_iterations  =  100
dir_              = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/param-tuning-100-runs/'

import de_for_learners, de_utility
str2Dump=""
for cnt in xrange(no_of_iterations):
  print "Iteration #", cnt
  print "*"*100
  print "Started at:", de_utility.giveTimeStamp()
  print "*"*100
  '''
  learner 1 : CART
  '''
  # 1. run DE for tuning CART
  auc_ = de_for_learners.evaluateLearners('CART')
  fileToSave = dir_ + 'cart' + '.csv'

  # 2. run DE for tuning RF
  # auc_ =  de_for_learners.evaluateLearners('RF')
  #fileToSave = dir_ + 'rf' + '.csv'

  ###3. run DE for tuning SVM
  #auc_ = de_for_learners.evaluateLearners('SVM')
  #fileToSave = dir_ + 'svm' + '.csv'

  # ###4. run DE for tuning Logistic Regression
  # auc_ = de_for_learners.evaluateLearners('LOGI')
  #fileToSave = dir_ + 'logi' + '.csv'

  print "Ended at:", de_utility.giveTimeStamp()
  str2Dump = str2Dump + str(round(auc_, 5)) + ',' + '\n'
  print "*"*100




de_utility.dumpContentIntoFile(str2Dump, fileToSave)
