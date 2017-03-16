'''
the file gets
author id for insane 90 metrics file
'''
import csv, os




def getAuthorContent(dirParam):
    authorDict={}
    no_file   =dirParam + 'randFile_n_ninety_metrics.csv'
    yes_file  =dirParam + 'randFile_y_ninety_metrics.csv'
    with open(yes_file, 'rU') as yes_f:
      reader_ = csv.reader(yes_f)
      for row in reader_:
          fileName  =row[0]
          authorCnt =row[88]
          authorDict[fileName] = authorCnt
    with open(no_file, 'rU') as no_f:
      reader_ = csv.reader(no_f)
      for row in reader_:
          fileName  =row[0]
          authorCnt =row[88]
          authorDict[fileName] = authorCnt
    print authorDict
    return authorDict


def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)


def processFilesForAuthorCount(fileParam):
    strToCreate=''
    with open(fileParam, 'rU') as file_:
      reader_ = csv.reader(file_)
      for row in reader_:
          dirName   =row[1]
          fileName  =row[4]
          authorCount = getAuthorContent(dirName)
          strToCreate = strToCreate + fileName + ',' + authorCount + ',' + '\n'
    #output = dumpContentIntoFile(strToCreate, '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/filesWithAuthorCount.csv')
    #print "Dumped a file of {} bytes, with authro information.".format(output)


theFIle='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/New.Categ.csv'
processFilesForAuthorCount(theFIle)
