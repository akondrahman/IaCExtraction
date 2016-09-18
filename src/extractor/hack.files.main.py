# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:25:33 2016

@author: akond
"""



import os 
from SmellDetector import Analyzer, Utilities
currentItem = 0
folderOfPuppetRepos="/Users/akond/Documents/AkondOneDrive/OneDrive/Fall16-ThesisTopic/puppet_repos/" 
headerStr1="Filename, max_nest_depth, class_dec, def_dec, pack_dec, file_dec, serv_dec, exec_dec, cohe_meth, body_txt_size,"
headerStr2="lines_w_comm, lines_wo_comm, outerelems, file_reso, service_reso, package_reso, hard_coded_stmt, node_decl, parent_class,"
headerStr = headerStr1 + headerStr2



print "Started at: ", Utilities.giveTimeStamp()
totalRepos = len(os.listdir(folderOfPuppetRepos))
for item in os.listdir(folderOfPuppetRepos):
 currentFolder = os.path.join(folderOfPuppetRepos, item)
 print "---------------------------------------"
 print "Analyzing: ",  currentFolder
 if not os.path.isfile(currentFolder):
   fileToSave = currentFolder + "/all.file.metrics.csv"
   file_level_output = Analyzer.hackFileLevelDetails(currentFolder, item)
   # append contetn with header
   fullStr = headerStr + "\n" + file_level_output
   #print file_level_output
   dump_status = Utilities.dumpStrToFile(fileToSave, fullStr)
   print "Dumped a file of {} bytes ...".format(dump_status)
 currentItem += 1
 stausStr = str("{:.2f}".format(float(currentItem * 100)/float(totalRepos))) + "% analysis completed"
 print stausStr
 print "---------------------------------------"
print "Done with metric extraction!"
print "Ended at: ", Utilities.giveTimeStamp()