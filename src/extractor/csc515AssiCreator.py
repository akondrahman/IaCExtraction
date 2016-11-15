# -*- coding: utf-8 -*-
"""
Created on Nov 24 2016

@author: akond
"""



import os
from random import shuffle
def getAssignmentinStr(fileParam):
  with open(fileParam, 'r') as assifile:
    fullContent=assifile.read().replace('\n', ' ')
  splittedContentList = fullContent.split('!')
  #print splittedContentList
  return splittedContentList




def writeContentToFile(strP, file_):
  fileToWrite = open( file_, 'w')
  fileToWrite.write(strP )
  fileToWrite.close()
  return str(os.stat(file_).st_size)
def createAssignemnt(fileName, outFile, shuffleFlag=True):
  print "Processing:" , outFile
  contentHolder="Message,Category" + "\n"
  contentOfFileInList = getAssignmentinStr(fileName)
  if shuffleFlag:
    shuffle(contentOfFileInList)
  #print contentOfFileInList
  for elem in contentOfFileInList:
    elem = elem.replace(',', ';')
    contentHolder = contentHolder + elem + "," + "\n"
  status_ = writeContentToFile(contentHolder, outFile)
  print "Created a file of {} bytes".format(status_)
inp_file_='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/master-18/student1.txt'
out_file_='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Categorization/StudentStudy/distrubution/student70.csv'
createAssignemnt(inp_file_,  out_file_, True)
