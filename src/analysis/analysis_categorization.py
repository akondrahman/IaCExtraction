'''
Akond Rahman: Dec 01, 2016
'''
import os, csv

studentsToIgnore = []
def readFile(dirNameParam):
  messageDict = {}
  for file_ in os.listdir(dirNameParam):
    if file_.endswith(".csv"):
      print "Analyzing ...", file_
      fullFileName = dirNameParam + file_
      with open(fullFileName, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
           if len(row) > 0:
             message_ = row[0]
             catego_  = row[1]
             if message_ not in messageDict:
               messageDict[message_] = [catego_]
             else:
               existingList = messageDict[message_]
               tmp_ = existingList + [catego_]
               messageDict[message_] = tmp_
  return messageDict

def getRepoInfo(repoKey):
    repoPathToRet=''
    repoDict={
              'M1':'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet/',
              'M2':'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/relabs-puppet/',
              'W1':'/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh/',
              'W2':'/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh4/',
              'W3':'/Users/akond/PUPP_REPOS/wikimedia-downloads/kafka',
              'W4':'/Users/akond/PUPP_REPOS/wikimedia-downloads/kraken/',
              'W5':'/Users/akond/PUPP_REPOS/wikimedia-downloads/mariadb/',
              'W6':'/Users/akond/PUPP_REPOS/wikimedia-downloads/mesos/',
              'W7':'/Users/akond/PUPP_REPOS/wikimedia-downloads/nginx/',
              'W8':'/Users/akond/PUPP_REPOS/wikimedia-downloads/puppet/',
              'W9':'/Users/akond/PUPP_REPOS/wikimedia-downloads/translatewiki/',
              'W10':'/Users/akond/PUPP_REPOS/wikimedia-downloads/vagrant/',
              'W11':'/Users/akond/PUPP_REPOS/wikimedia-downloads/wikimetrics/',
              }
    if repoKey in repoDict:
        repoPathToRet=repoDict[repoKey]
    else:
        repoPathToRet = 'WTF'
    return repoPathToRet
def loadMessageMapping(dirNameParam):
  messageDict = {}
  for file_ in os.listdir(dirNameParam):
    if file_.endswith(".csv"):
      fullFileName = dirNameParam + file_
      print "Analyzing for mapping ...", file_
      with open(fullFileName, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
              message_ = row[0]
              ID_  = row[1]
              repo_ = getRepoInfo(row[2])
              if message_ not in messageDict:
                messageDict[message_] = (ID_, repo_)
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



def findIDMappingOfStudentMessages(studentDict, idDict):
   '''
   This method retruns the ID, and repo for each message categorized by students
   '''
   dict2ret={}
   for k_, v_ in studentDict.iteritems():
     if k_ in idDict:
        dict2ret[k_] = idDict[k_]
   return dict2ret


def performInterRaterRelaibility(rating1, rating2):
  from sklearn import metrics
  #ref:: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html
  kappa_score = metrics.cohen_kappa_score(rating1, rating2)
  return kappa_score
dirName='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/completed/'
student_summary_dict = readFile(dirName)
cat_messgae_mapping = summarize(student_summary_dict)
#print summary_dict
#print cat_messgae_mapping
print "#"*100
myRatingDir='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/completed/'
mappingDir='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/ided/'
msgMappingDict = loadMessageMapping(mappingDir)
print "Length of unique messages", len(msgMappingDict)
print "#"*100
idMappingOfMessages = findIDMappingOfStudentMessages(student_summary_dict, msgMappingDict)
print "Length of unique student derived mapped messages", len(idMappingOfMessages)
print "#"*100
