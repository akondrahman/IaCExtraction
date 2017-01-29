'''
Phase 2 analysis
'''

import os, csv, xlrd, collections
def readFile(rater1F, rater2F):
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


rater1File='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/rater1/ForAnalBatchTwo.csv'
rater2File='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/Phase-2/rater2/ForAnalBatchTwo.csv'
readFile(rater1File, rater2File)
