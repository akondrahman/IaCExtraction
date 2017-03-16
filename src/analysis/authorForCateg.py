'''
the file gets
author id for insane 90 metrics file
'''
import csv, os




def getAuthorContent(dirParam, file2check):
    authorDict={}
    no_file   =dirParam + 'randFile_n_ninety_metrics.csv'
    yes_file  =dirParam + 'randFile_y_ninety_metrics.csv'
    with open(yes_file, 'rU') as yes_f:
      reader_ = csv.reader(yes_f)
      for row in reader_:
          fileName  =row[0]
          if(file2check==fileName):
             authorCnt =row[88]
             authorDict[fileName] = authorCnt
    with open(no_file, 'rU') as no_f:
      reader_ = csv.reader(no_f)
      for row in reader_:
          fileName  =row[0]
          if(file2check==fileName):
             authorCnt =row[88]
             authorDict[fileName] = authorCnt
    return authorDict
