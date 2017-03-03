'''
main script to call DE for parameter tuning
of statistical learners
Akond Rahman
Feb 23, 2017
'''



import de_for_learners, de_utility
print "Started at:", de_utility.giveTimeStamp()
print "*"*100
# 1. run DE for tuning CART
# de_for_learners.evaluateLearners('CART')
# 2. run DE for tuning RF
# de_for_learners.evaluateLearners('RF')
# ###3. run DE for tuning SVM
# de_for_learners.evaluateLearners('SVM')
###4. run DE for tuning Logistic Regression
de_for_learners.evaluateLearners('LOGI')
print "Ended at:", de_utility.giveTimeStamp()
print "*"*100
