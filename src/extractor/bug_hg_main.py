# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:30:41 2016

@author: akond
"""



import hglib , subprocess, os, time, datetime, re, numpy as np 
import bug_hg_developer 



def splitBugMapping(bug_map_param): 
  tupToRet = ()
  y_bug_list = [] 
  n_bug_list = [] 
  for elem in bug_map_param:
    status_ = elem[2]  # the lst element, index 3, has bug ID, the 2nd last elem has bug flag
    if status_=='y':
      y_bug_list.append(elem)
    else: 
      n_bug_list.append(elem)
  print "len-y:{}, len-n:{}".format(len(y_bug_list), len(n_bug_list))  
  tupToRet=(y_bug_list, n_bug_list)    
  return tupToRet    


def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret  

def getLegitFiles(fileListParam):
  outputList = []
  for file_ in fileListParam:
    #print file_
    tmp_ = file_[4] # has a lot fo stuff get only the file name
    if '.pp' in tmp_:
      outputList.append(tmp_)	
  return outputList	


def getPuppetCommitMapping(all_commits_param, legit_files_param):
  listToRet = []
  cnt_ = 0 
  for e in  all_commits_param:
    commit_hash = e[1]
    cnt_ = cnt_ + 1 
    #print "Total {} commits analyzed ".format(cnt_)
    #print commit_hash
    diffCommand = bashCommand + commit_hash
    diff_output = subprocess.check_output(['bash','-c', diffCommand])
    #print diff_output
    for legitFile in pp_files:
      if(legitFile in diff_output):
        #print "Mapping found !!!"
        tmp_tup = (legitFile, commit_hash)
        listToRet.append(tmp_tup)  
    #returnDirCommand= " cd /Users/akond/Documents/AkondOneDrive/OneDrive/Fall16-ThesisTopic/Puppeteer/"
    returnDirCommand= " cd ."      
    ret_dir_output = subprocess.check_output(['bash','-c', returnDirCommand]) 
  return listToRet  

def getBugIDMatch(messageToSearchParam):
  valToRet=False  
  #matched_elems = re.findall(r'[\bbug\b].*[0-9]+', messageToSearchParam)   
  matched_elems = re.findall(r'[\bbug\b]', messageToSearchParam) 
  if len(matched_elems) > 0:
    valToRet = True        
  return valToRet


def getPuppetBugMappingList(mappingListParam, repo_abs_path):
  listToRet = []
  cnt_ = 0 
  for tuple_elem in mappingListParam:
    file_ = tuple_elem[0]  	
    commit_hash = tuple_elem[1]
    cnt_ = cnt_ + 1 
    #print "Total {} commits analyzed ".format(cnt_)
    #print commit_hash
    diffCommand = bashCommand + commit_hash + " | " +  " awk '/summary/' "
    diff_output = subprocess.check_output(['bash','-c', diffCommand])
    diff_output = diff_output.lower()    
    #print diff_output
    #if ( ('bug' in diff_output)or ('fix' in diff_output)or ('patch' in diff_output))
    file_to_save = os.path.join(repo_abs_path, file_)
    if ('merg' in diff_output) or ('no bug' in diff_output) or ('debug' in diff_output) or ('out' in diff_output) or ('revert' in diff_output) or ('minor' in diff_output) or ('nobug' in diff_output):    
        tup_ = (file_to_save, commit_hash, 'n', diff_output)
    else:
      #if (('bug' in diff_output) or ('fix' in diff_output)):
      if ('bug' in diff_output):      
        #print "$$ Bug detected @", diff_output    
        tup_ = (file_to_save, commit_hash, 'y', diff_output)
      else:
        tup_ = (file_to_save, commit_hash, 'n', diff_output)
    listToRet.append(tup_)            	
    #returnDirCommand= " cd /Users/akond/Documents/AkondOneDrive/OneDrive/Fall16-ThesisTopic/Puppeteer/"
    returnDirCommand= " cd ."      
    ret_dir_output = subprocess.check_output(['bash','-c', returnDirCommand]) 
  return listToRet  



print "Started at:", giveTimeStamp()
repo_path="/Users/akond/PUPP_REPOS/v2/mozilla_releng_only/relabs-puppet"
repo_branch="master"
bashCommand= " cd " + repo_path  +" ; hg log -p -r " 
repo_complete = hglib.open(repo_path) 
files = list(repo_complete.manifest())
pp_files =getLegitFiles(files)
#print "Count of legit files:", len(pp_files)
pp_to_all_file_ratio = (float(len(pp_files))/float(len(files)))
all_commits = repo_complete.log()
#print "All commit count", len(all_commits)
puppet_commit_mapping_list = getPuppetCommitMapping(all_commits, pp_files)
print "Performed commit mapping"
print "#"*75
puppet_bug_mapping_list = getPuppetBugMappingList(puppet_commit_mapping_list, repo_path)
print "Performed bug mapping"
print "#"*75
#print puppet_bug_mapping_list
y_n_bug_mapiing = splitBugMapping(puppet_bug_mapping_list)
yes_bug_mapping = y_n_bug_mapiing[0]
no_bug_mapping  = y_n_bug_mapiing[1]
print "Yes and no classification based on bug evidence"
print "#"*75
# junk_bug = [('/Users/akond/PUPP_REPOS/sample-mozilla/manifests/moco-config.pp', '12wer', 'y', 'bug hoga'), 
#             ('/Users/akond/PUPP_REPOS/sample-mozilla/manifests/moco-config.pp', '34wer', 'n', 'nai'), 
#             ('/Users/akond/PUPP_REPOS/sample-mozilla/manifests/stages.pp', '39wer', 'n', 'putkey')]

# junk_comm = [('/Users/akond/PUPP_REPOS/sample-mozilla/manifests/site.pp', '12werx'), 
#             ('/Users/akond/PUPP_REPOS/sample-mozilla/manifests/site.pp', '34wery'), 
#             ('/Users/akond/PUPP_REPOS/sample-mozilla/manifests/stages.pp', '39wezr')]            
files_that_have_defects = bug_hg_developer.getFilesFromMappingInfo(yes_bug_mapping)
files_that_are_mixed = bug_hg_developer.getFilesFromMappingInfo(no_bug_mapping)
no_deftect_files = bug_hg_developer.getNoDefectsOnlyFiles(files_that_have_defects, files_that_are_mixed)
# only pass files that have bugs in them , not the whole thing!

# file 2 bug mapping file
y_file2bug= repo_path + "/" + "y_bug_msg.csv"
yf2b = open(y_file2bug, "w")
y_str_to_dump = bug_hg_developer.getAllDevelopmentMetricList(files_that_have_defects, repo_path, yes_bug_mapping, yf2b)
print "#"*75
#print str_to_dump
# dumped yes metrics 
y_file_to_save = repo_path + "/" + "y_metrics.csv"
y_dump_status = bug_hg_developer.dumpContentIntoFile(y_str_to_dump, y_file_to_save)
print "Dumped a CSV file of {} bytes".format(y_dump_status)
print "#"*75
if len(no_deftect_files) > 0:
  #print no_bug_mapping  
  # even though I am passing , "n_bug_msg.csv" it will eb ana empty file as no bug messgaes for files that dont have bugs 
  # file 2 bug mapping file
  n_file2bug= repo_path + "/" + "n_bug_msg.csv"
  nf2b = open(n_file2bug, "w")
  n_str_to_dump = bug_hg_developer.getAllDevelopmentMetricList(no_deftect_files, repo_path, no_bug_mapping , nf2b, False)
  # dumped no metrics 
  n_file_to_save = repo_path + "/" + "n_metrics.csv"
  n_dump_status = bug_hg_developer.dumpContentIntoFile(n_str_to_dump, n_file_to_save)
  print "Dumped a CSV file of {} bytes".format(n_dump_status)
  print "#"*75  
else: 
  print "Didn't find non-defected files! " 
  print "Wow!"*10  
print "#"*75
print "Count fo files was:", len(files)
print "The puppet to all file ratio was:", pp_to_all_file_ratio
print "#"*75
print "REPO:", repo_path
print "#"*75
print "defected file count:{}, no-defected files:{}".format(len(files_that_have_defects), len(no_deftect_files))
print "#"*75



#### For bug message project ::: start ::::
all_bug_msgs = bug_hg_developer.getBugMessages(yes_bug_mapping)
print "Count of all bug messages:", len(all_bug_msgs)
print "#"*75
unique_bug_msg = np.unique(all_bug_msgs)
print "Count of unique bug messages:", len(unique_bug_msg)
print "#"*75
msg_file_to_save = repo_path + "/" + "bug_msgs.txt"
msgs_as_str=bug_hg_developer.dumpBugMessageAsStr(unique_bug_msg, msg_file_to_save)
print "#"*75
#### For bug message project ::: end ::::
print "Ended at:", giveTimeStamp()