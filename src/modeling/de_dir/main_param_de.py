'''
main script to call DE for parameter tuning
of statistical learners
Akond Rahman
Feb 23, 2017
'''



import de_for_learners
# 1. run DE for tuning CART
#de_for_learners.evaluateLearners('CART')
# 2. run DE for tuning RF
de_for_learners.evaluateLearners('RF')
