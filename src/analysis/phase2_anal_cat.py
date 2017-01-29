'''
Phase 2 analysis
'''

import os, csv, xlrd, collections




def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)
def phase2Anal(rater1F, rater2F):
    agreementCnt=0
    disAgreementCnt=0
    with open(rater1F, 'rU') as f1:
      reader1 = csv.reader(f1)
      next(reader1, None)
      for row1 in reader1:
        msg1=row1[0]
        categ1=row1[1]
        #print "file1:category->", categ1
        with open(rater2F, 'rU') as f2:
          reader2 = csv.reader(f2)
          next(reader2, None)
          for row2 in reader2:
            msg2=row2[0]
            categ2=row2[1]
            #print "file2:category->",categ2
            if(msg1==msg2):
               #print "msg:{}, cat1:{}, cat2:{}".format(msg1, categ1, categ2)
               if (categ1==categ2):
                 agreementCnt = agreementCnt + 1
               else:
                 disAgreementCnt = disAgreementCnt + 1
        #print "reader1: {}, reader2: {}".format(len(reader1), len(reader2))
    print "Agremments:{}, diagreements: {}".format(agreementCnt, disAgreementCnt)




def transformCate(catego_):
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
    return catego_



def phase1Anal(rater1F, rater2F):
    agreementCnt=0
    disAgreementCnt=0
    disAgreeStr=''
    agreeStr=''
    with open(rater1F, 'rU') as f1:
      reader1 = csv.reader(f1)
      next(reader1, None)
      for row1 in reader1:
        id1=row1[0]
        repo1=row1[1]
        msg1=row1[2]
        categ1=row1[3]
        #print "file1:category->", categ1
        with open(rater2F, 'rU') as f2:
          reader2 = csv.reader(f2)
          next(reader2, None)
          for row2 in reader2:
            id2=row2[0]
            repo2=row2[1]
            msg2=row2[2]
            categ2=row2[3]
            categ2 = transformCate(categ2)
            #print "file2:category->",categ2
            if(msg1==msg2):
               #print "msg:{}, cat1:{}, cat2:{}".format(msg1, categ1, categ2)
               if (categ1==categ2):
                 agreementCnt = agreementCnt + 1
                 agreeStr = agreeStr + msg1 + ',' + categ1 + ',' + categ2 + ',' + '\n'
               else:
                 disAgreementCnt = disAgreementCnt + 1
                 disAgreeStr = disAgreeStr + msg1 + ',' + categ1 + ',' + categ2 + ',' + '\n'
        #print "reader1: {}, reader2: {}".format(len(reader1), len(reader2))
    print "Agremments:{}, diagreements: {}".format(agreementCnt, disAgreementCnt)
    dumpContentIntoFile(disAgreeStr, '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/disagee.csv')
    dumpContentIntoFile(agreeStr, '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/agee.csv')




# rater1File='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/rater1/ForAnalBatchTwo.csv'
# rater2File='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/rater2/ForAnalBatchTwo.csv'
#phase2Anal(rater1File, rater2File)


rater1File='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/rater1/ForAnalBatchOne.csv'
rater2File='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/rater2/ForAnalBatchOne.csv'
phase1Anal(rater1File, rater2File)
