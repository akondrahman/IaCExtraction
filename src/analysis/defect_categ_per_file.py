'''
are some files have
more types of defects than
others
March 17, 2017
Akond Rahman
'''
import os, csv, numpy as np

def getFileToDefectCateg(fileParam, orgName):
   dict2Ret={}
   with open(fileParam, 'rU') as f:
     reader_ = csv.reader(f)
     for row in reader_:
        fileName = row[4]
        categ    = row[3]
        if orgName in fileName:
           if fileName not in dict2Ret:
              dict2Ret[fileName] = [categ]
           else:
              dict2Ret[fileName] =  dict2Ret[fileName] + [categ]
   return dict2Ret


def processFileToCategMapping(dictP):

    theZeroDefectList      = []
    atLeastOneDefectList   = []
    atLeastTwoDefectList   = []
    atLeastThreeDefectList = []
    atLeastFourDefectList  = []
    atLeastFiveDefectList  = []
    atLeastSixDefectList   = []
    atLeastSevenDefectList = []
    atLeastEightDefectList = []
    atLeastNineDefectList  = []
    for k_, v_ in dictP.items():
        unique_defect_categ = np.unique(v_)
        unique_defect_categ = [defect_type for defect_type in unique_defect_categ if defect_type !='' ]
        if((len(unique_defect_categ)==1) and (unique_defect_categ[0]=='N')):
            theZeroDefectList.append(k_)
        elif((len(unique_defect_categ)==1) and (unique_defect_categ[0]!='N')):
            atLeastOneDefectList.append(k_)
        elif((len(unique_defect_categ)==2) ):
            atLeastTwoDefectList.append(k_)
        elif((len(unique_defect_categ)==3) ):
            atLeastThreeDefectList.append(k_)
        elif((len(unique_defect_categ)==4) ):
            atLeastFourDefectList.append(k_)
        elif((len(unique_defect_categ)==5) ):
            atLeastFiveDefectList.append(k_)
        elif((len(unique_defect_categ)==6) ):
            atLeastSixDefectList.append(k_)
        elif((len(unique_defect_categ)==7) ):
            atLeastSevenDefectList.append(k_)
        elif((len(unique_defect_categ)==8) ):
            atLeastEightDefectList.append(k_)
        elif((len(unique_defect_categ)==9) ):
            atLeastNineDefectList.append(k_)
    print "Count of files with no defects:", len(theZeroDefectList)
    print "Count of files with at least 1 types of defects:", len(atLeastOneDefectList)
    print "Count of files with at least 2 types of defects:", len(atLeastTwoDefectList)
    print "Count of files with at least 3 types of defects:", len(atLeastThreeDefectList)
    print "Count of files with at least 4 types of defects:", len(atLeastFourDefectList)
    print "Count of files with at least 5 types of defects:", len(atLeastFiveDefectList)
    print "Count of files with at least 6 types of defects:", len(atLeastSixDefectList)
    print "Count of files with at least 7 types of defects:", len(atLeastSevenDefectList)
    print "Count of files with at least 8 types of defects:", len(atLeastEightDefectList)
    print "Count of files with at least 9 types of defects:", len(atLeastNineDefectList)

theFile='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/New.Categ.csv'
moziDict = getFileToDefectCateg(theFile, 'mozilla')
wikiDict = getFileToDefectCateg(theFile, 'wikimedia')
# print moziDict
# print "="*100
# print wikiDict
print "="*100
print "THE MOZILLA DATASET"
processFileToCategMapping(moziDict)
print "="*100
print "THE WIKIMEDIA DATASET"
processFileToCategMapping(wikiDict)
print "="*100
