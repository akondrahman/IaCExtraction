'''
Akond Rahman: Dec 01, 2016
'''
import os, csv

studentsToIgnore = []
def readFile(dirNameParam):
  messageDict = {}
  for file_ in os.listdir(dirNameParam):
    if file_.endswith(".csv"):
      fullFileName = dirNameParam + file_
      with open(fullFileName, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
           message_ = row[0]
           catego_  = row[1]
           if message_ not in messageDict:
             messageDict[message_] = [catego_]
           else:
             existingList = messageDict[message_]
             tmp_ = existingList + [catego_]
             messageDict[message_] = tmp_
  return messageDict


def summarize(dictParam):
    cat2messageMap=[]
    for k_, v_ in dictParam.iteritems():
       for cat_elem in v_:
            tuple_ = (cat_elem, k_)
            cat2messageMap.append(tuple_)
    #    print"="*100
    #    print k_
    #    print "*"*25
    #    print v_
    #    print "="*100
    return cat2messageMap


def performInterRaterRelaibility(rating1, rating2):
  from sklearn import metrics
  #ref:: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html
  kappa_score = metrics.cohen_kappa_score(rating1, rating2)
  return kappa_score
dirName='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/completed/'
summary_dict = readFile(dirName)
cat_messgae_mapping = summarize(summary_dict)
#print summary_dict
#print cat_messgae_mapping
myRatingDir='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/completed/'
