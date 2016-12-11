'''
Akond Rahman: Dec 01, 2016
'''
import os, csv, xlrd, collections
def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)
studentsToIgnore = []
def readFile(dirNameParam):
  messageDict = {}
  for file_ in os.listdir(dirNameParam):
    if file_.endswith(".csv"):
      #print "Analyzing ...", file_
      fullFileName = dirNameParam + file_
      with open(fullFileName, 'rU') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers
        for row in reader:
           if len(row) > 0:
             message_ = row[0]
             catego_  = row[1]
             if 'Build' in catego_:
                 catego_='B'
             elif 'Not' in catego_:
                 catego_='N'
             elif 'Interface' in catego_:
                 catego_='I'
             elif 'Other' in catego_:
                 catego_='O'
             elif 'Algorithm' in catego_:
                 catego_='AL'
             elif 'Assignment' in catego_:
                 catego_='AS'
             elif 'Function' in catego_:
                 catego_='F'
             elif 'Checking' in catego_:
                 catego_='C'
             elif 'Timing' in catego_:
                 catego_='T'
             elif 'Documentation' in catego_:
                 catego_='D'
             if message_ not in messageDict:
               messageDict[message_] = [catego_]
             else:
               existingList = messageDict[message_]
               tmp_ = existingList + [catego_]
               messageDict[message_] = tmp_
  return messageDict




def getResovledCategorization(resolvedFileName):
          IDHolder = {}
          catHolder = {}
          workbook2read = xlrd.open_workbook(resolvedFileName)
          sheet2read = workbook2read.sheet_by_index(1)
          number_of_rows = sheet2read.nrows
          for row2read in xrange(number_of_rows):
            cells2read = sheet2read.row_slice(rowx=row2read, start_colx=0, end_colx=5) # we have 5 columns, starting with an index of 0
            #print cells2read
            repoName = cells2read[0].value
            if (repoName!='REPO' and repoName!='WTF'):
                id_ = int(cells2read[1].value)    ## the ID
                cate_ = cells2read[4].value   ## the final category is the fifth index
                if repoName not in IDHolder:
                  IDHolder[repoName] = [id_]
                else:
                  tmp_ID_List = IDHolder[repoName]
                  IDHolder[repoName] = tmp_ID_List +  [id_]
                if repoName not in catHolder:
                  catHolder[repoName] = [cate_]
                else:
                  tmp_ = catHolder[repoName]
                  catHolder[repoName] = tmp_ +  [cate_]

          print "The IDs of messages ..."
          print "-"*50

          for k_, v_ in IDHolder.iteritems():
                  print "Repo name:", k_
                  print "IDs:", v_
                  print "*"*25
          print "-"*50
          print "The distribution of categories ..."
          print "-"*50
          for k_, v_ in catHolder.iteritems():
                  print "Repo name:", k_
                  print "Category distribution:", collections.Counter(v_)
                  print "*"*25                  
          print "-"*50

def getRepoInfo(repoKey):
    repoPathToRet=''
    # repoDict={
    #           'M1':'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet/',
    #           'M2':'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/relabs-puppet/',
    #           'W1':'/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh/',
    #           'W2':'/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh4/',
    #           'W3':'/Users/akond/PUPP_REPOS/wikimedia-downloads/kafka',
    #           'W4':'/Users/akond/PUPP_REPOS/wikimedia-downloads/kraken/',
    #           'W5':'/Users/akond/PUPP_REPOS/wikimedia-downloads/mariadb/',
    #           'W6':'/Users/akond/PUPP_REPOS/wikimedia-downloads/mesos/',
    #           'W7':'/Users/akond/PUPP_REPOS/wikimedia-downloads/nginx/',
    #           'W8':'/Users/akond/PUPP_REPOS/wikimedia-downloads/puppet/',
    #           'W9':'/Users/akond/PUPP_REPOS/wikimedia-downloads/translatewiki/',
    #           'W10':'/Users/akond/PUPP_REPOS/wikimedia-downloads/vagrant/',
    #           'W11':'/Users/akond/PUPP_REPOS/wikimedia-downloads/wikimetrics/',
    #           }
    repoDict={
              'M1':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/mozila-puppet/',
              'M2':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/mozila-relabs-puppet/',
              'W1':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-cdh/',
              'W2':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-cdh4/',
              'W3':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-kafka/',
              'W4':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-kraken/',
              'W5':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-mariadb/',
              'W6':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-mesos/',
              'W7':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-nginx/',
              'W8':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-puppet/',
              'W9':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-translatewiki/',
              'W10':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-vagrant/',
              'W11':'/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/MyStudy/wikimedia-wikimetrics/',
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
      #print "Analyzing for mapping ...", file_
      with open(fullFileName, 'rU') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers
        for row in reader:
            #print row
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
  #print "Vector-1:", rating1
  print "Vector-1:::my-rating:::distribution:", collections.Counter(rating1)
  #print "Vector-2:", rating2
  print "Vector-2:::student-rating:::distribution:", collections.Counter(rating2)
  kappa_score = metrics.cohen_kappa_score(rating1, rating2)
  return kappa_score
def getMyCategorization(idDictParam):
    dict_return = {}
    paikhana='     '
    for k_, v_ in idDictParam.iteritems():
        if k_ != paikhana:
          repo_ = v_[1]
          file2read = repo_ + 'my_full_qual_coding.xls'
          #print "message:={}=, file:{}, ID: {}".format(k_, file2read,  v_[0])
          id2check = int (v_[0])
          row2read = id2check # first row is header, and correponds to zero, so no need to add 1
          workbook2read = xlrd.open_workbook(file2read)
          sheet2read = workbook2read.sheet_by_index(0)
          #print "message:{}, file:{}, row: {}".format(k_, file2read,  row2read)
          cells2read = sheet2read.row_slice(rowx=row2read, start_colx=0, end_colx=10) # we ahve 11 columsn, starting with an index of 0
          categorization=''
          #print file2read
          #print len(cells2read)
          if int(cells2read[0].value)==id2check:
                #print cells2read[1].value
                if (cells2read[1].value==float(1)):
                    categorization='N'
                elif (cells2read[2].value==float(1)):
                    categorization='F'
                elif (cells2read[3].value==float(1)):
                    categorization='AS'
                elif (cells2read[4].value==float(1)):
                    categorization='I'
                elif (cells2read[5].value==float(1)):
                    categorization='C'
                elif (cells2read[6].value==float(1)):
                    categorization='T'
                elif (cells2read[7].value==float(1)):
                    categorization='B'
                elif (cells2read[8].value==float(1)):
                    categorization='D'
                elif (cells2read[9].value==float(1)):
                    categorization='AL'
                elif (len(cells2read)==11):
                  if (cells2read[10].value==float(1)):
                    categorization='O'
                else:
                    categorization='WTF'
                dict_return[id2check]=(k_, repo_, categorization)
    return dict_return



def performOverallRelaibility(studentCategorization, idMapping, myCategorization):
    matched= 0
    mismatched = 0
    myRating=[]
    studentRating = []
    #print idMapping
    for k_, v_ in studentCategorization.iteritems():
        #print k_
        if k_ in idMapping:
            #print "Matched !!!"
            matched = matched + 1
            tmp_ = idMapping[k_][0]# first element of idMapping values fo reach key is ID
            if tmp_!='':
              idOfMessage = int(tmp_)
              my_ctaegory_for_message = myCategorization[idOfMessage][-1] # categorization
              #print my_ctaegory_for_message
              student_catgory_for_message = v_[-1] ## same message might be assigned to  multiple people, so lets take the last
              if ((my_ctaegory_for_message!='WTF') and (student_catgory_for_message!='WTF')):
                myRating.append(my_ctaegory_for_message)
                studentRating.append(student_catgory_for_message)
        else:
            mismatched = mismatched + 1
            #print "I am surprised !!!"
    if (len(myRating)==len(studentRating)):
        print "Total messages to parse:", len(myRating)
        print '-'*50
        kapp_score = performInterRaterRelaibility(myRating, studentRating)
    else:
        print "Make kappa great again"
        kapp_score = float(0)
    print "*** Total matches:{}, total mismatches: {}***".format(matched, mismatched)
    print "-"*50
    return kapp_score



def doPerStudentInterRaterReliability(studentDirParam, msgMappingDictParam):
  for file_ in os.listdir(studentDirParam):
    indiStudentDict = {}
    if file_.endswith(".csv"):
      #print "Analyzing ...", file_
      fullFileName = studentDirParam + file_
      with open(fullFileName, 'rU') as f_:
        reader = csv.reader(f_)
        next(reader, None)  # skip the headers
        for row in reader:
           if len(row) > 0:
             message_ = row[0]
             catego_  = row[1]
             if 'Build' in catego_:
                 catego_='B'
             elif 'Not' in catego_:
                 catego_='N'
             elif 'Interface' in catego_:
                 catego_='I'
             elif 'Other' in catego_:
                 catego_='O'
             elif 'Algorithm' in catego_:
                 catego_='AL'
             elif 'Assignment' in catego_:
                 catego_='AS'
             elif 'Function' in catego_:
                 catego_='F'
             elif 'Checking' in catego_:
                 catego_='C'
             elif 'Timing' in catego_:
                 catego_='T'
             elif 'Documentation' in catego_:
                 catego_='D'
             if message_ not in indiStudentDict:
               indiStudentDict[message_] = [catego_]
             else:
               existingList = indiStudentDict[message_]
               tmp_ = existingList + [catego_]
               indiStudentDict[message_] = tmp_
      idMappingOfMessages = findIDMappingOfStudentMessages(indiStudentDict, msgMappingDictParam)
      my_categorization_of_messages = getMyCategorization(idMappingOfMessages)
      kap= performOverallRelaibility(indiStudentDict, idMappingOfMessages, my_categorization_of_messages)
      print "For {}, the kappa score is:{}".format(file_, kap)
      print "="*75

def getRepoWiseStats(dict_):
  statDict={}
  for key_, val_ in idMappingOfMessages.iteritems():
    #print "k:{}, v:{}".format(key_, val_)
    repo_ = val_[1]
    id_   = val_[0]
    #if len(id_) > 0 :
    if repo_ not in statDict:
          statDict[repo_] = [id_]
    else:
           tmp_ = statDict[repo_]
           statDict[repo_] = tmp_ +  [id_]
  return statDict


def summarizePhaseOneResults(student_categorization_, idMapping_, fileNameP):
  phaseOneSummaryStr= ""
  agreementCnt = 0
  disAgreementCnt = 0
  for k_, v_ in student_categorization_.iteritems():
    if k_ in idMapping_:
      agreementFlag = False
      detailsOfMessage = idMapping_[k_]
      IDOfMessage = detailsOfMessage[0]
      RepoOfMessage = detailsOfMessage[1]
      distOfCatego  = collections.Counter(v_)
      countOfCategories = len(distOfCatego)
      if (countOfCategories == 1):
        agreementFlag = True
        agreementCnt = agreementCnt + 1
        mostAgreedCategory = distOfCatego.most_common(1)[0][0]
      else:
        agreementFlag = False
        disAgreementCnt = disAgreementCnt + 1
        # lets get the category with the highest count ,
        # output of distOfCatego.most_common(1) is Dist:[('C', 1)]
        mostAgreedCategory = distOfCatego.most_common(1)[0][0]
      '''
      Pre process the message
      '''
      elm = k_
      elm = elm.replace('\n', ' ')
      elm = elm.replace(',', ';')
      #print "ID: {}, Repo:{}, Most agreed category:{}, agreed?:{}".format(IDOfMessage, RepoOfMessage, mostAgreedCategory, str(agreementFlag))
      phaseOneSummaryStr = phaseOneSummaryStr + RepoOfMessage + ',' + str(IDOfMessage) + ',' + str(agreementFlag) + ',' + elm + ',' + mostAgreedCategory + ',' + ','  + '\n'
  #print phaseOneSummaryStr
  outputStatus = dumpContentIntoFile(phaseOneSummaryStr, fileNameP)
  print "Agreements:{}, disagreements:{}".format(agreementCnt, disAgreementCnt)
  return outputStatus
'''
Step-1: First get the categorization of students
'''
dirName='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/completed/'
student_categorization_of_messages = readFile(dirName)
cat_messgae_mapping = summarize(student_categorization_of_messages)
#print student_categorization_of_messages
#print cat_messgae_mapping
print "#"*100
'''
Step-2: Next  get the IDs of messages
'''
mappingDir='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/ided/'
msgMappingDict = loadMessageMapping(mappingDir)
print "Length of unique messages", len(msgMappingDict)
print "#"*100
'''
Step-3: Next  get the IDs of messages catgrized by students
'''
idMappingOfMessages = findIDMappingOfStudentMessages(student_categorization_of_messages, msgMappingDict)
print "Length of unique student derived mapped messages", len(idMappingOfMessages)
print "#"*100
'''
Step-4: Next get my mapping of the messages , that are categorized by students
'''
# my_categorization_of_messages = getMyCategorization(idMappingOfMessages)
# print "Length of messages that me and students have categorized:", len(my_categorization_of_messages)
# print "#"*100
'''
Step-5: Compare my and student's categories: overall inter rater reilability
'''
# kapap= performOverallRelaibility(student_categorization_of_messages, idMappingOfMessages, my_categorization_of_messages)
# print "The overal inter rater relaibiliy is:", kapap
# print "#"*100
'''
Step-6: per student inter rater reliability
'''
# doPerStudentInterRaterReliability(dirName, msgMappingDict)
# print "#"*100
print "=====The complete categories of messages====="
one_count = 0
mul_count = 0
for k_, v_ in student_categorization_of_messages.iteritems():
   print k_
   print v_
   if (len(v_) > 1):
       mul_count = mul_count + 1
   else:
       one_count = one_count + 1
   print "-"*50
print "#"*100
# print "Messages with one rating: {}, messages with multiple rating: {}".format(one_count, mul_count)
# print "#"*100
'''
Step-7: repo wise stats
'''
analyzed_so_far=0
statRepoDict= getRepoWiseStats(idMappingOfMessages)
sorted(statRepoDict)
for keys, values in statRepoDict.iteritems():
   analyzed_so_far = analyzed_so_far + len(values)
   #print "Repo name: {}, count of messages: {}".format(keys, len(values))
print "So far analyzed {} unique messages, from {} repos".format(analyzed_so_far, len(statRepoDict))
print "#"*100
'''
Step-8:
Summarize Phase 1 work
'''
file2save='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/P1_Category_Summary.csv'
# fileStatus = summarizePhaseOneResults(student_categorization_of_messages, idMappingOfMessages, file2save)
# print "Dumped a file of {} bytes. The file is for phase one summary.".format(fileStatus)
print "#"*100
'''
Step-9:
Summarize Resolved Phase 1 work
'''
phaseOneResolvedFile='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/Analysis_P1_Category_Summary.xls'
getResovledCategorization(phaseOneResolvedFile)
print "#"*100
