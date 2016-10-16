# -*- coding: utf-8 -*-
"""
Created on  Oct  15, 2016

@author: akond
"""



import csv, os 
def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)
def giveContents(fileNameParam):
  file2read= open(fileNameParam, 'rU')       
  data=file2read.read() 
  return data   	

def gatherPuppContent(fileParam):
 y_all = ""
 n_all = ""
 with open(fileParam, 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
       y_file_name = row[0]
       if len(y_file_name) > 0:
         y_content = giveContents(y_file_name)
         y_all =  y_all + y_file_name + "\n" +  "-"*25 + "\n" + y_content + "*"*50 + "\n"       
       n_file_name = row[1]       
       if len(n_file_name) > 0:       
         n_content = giveContents(n_file_name)
         #print n_content
         #rint "*"*50         
         n_all =  n_all + n_file_name + "\n" +  "-"*25 + "\n" + n_content + "*"*50 + "\n"       

 dumpContentIntoFile(y_all, "y_all.txt")
 dumpContentIntoFile(n_all, "n_all.txt") 





fileListing='wikimedia_vagrant_y_n_file_names.csv'
gatherPuppContent(fileListing)