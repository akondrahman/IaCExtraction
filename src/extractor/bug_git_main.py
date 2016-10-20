# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:20:19 2016

@author: akond
"""



import numpy as np
import bug_git_util
import sys
reload(sys)
sys.setdefaultencoding('utf8')
print "Started at:", bug_git_util.giveTimeStamp()

# do not end path with '/'
repo_path="/Users/akond/PUPP_REPOS/wikimedia-downloads/vagrant"
repo_branch="master"

# do not end path with '/'
# repo_path="/Users/akond/PUPP_REPOS/wikimedia-downloads/vagrant"
# repo_branch="master"
#repo_path="/Users/akond/PUPP_REPOS/wikimedia_operations_puppet_only/puppet"
#repo_branch="production"



all_files= bug_git_util.getRecursivelyAlFilles(repo_path)
all_pp_files_in_repo = bug_git_util.getPuppetFilesOfRepo(repo_path)
pp_to_all_file_ratio = (float(len(all_pp_files_in_repo))/float(len(all_files)))
rel_path_pp_files = bug_git_util.getRelPathOfFiles(all_pp_files_in_repo, repo_path)
pupp_commits_in_repo = bug_git_util.getPuppRelatedCommits(repo_path, rel_path_pp_files, repo_branch)
print "Performed commit mapping"
print "#"*75
pupp_bug_info_repo = bug_git_util.getPuppRelatedBugInfo(repo_path, repo_branch, pupp_commits_in_repo)
print "Performed bug mapping"
print "#"*75
y_n_bug_mapiing = bug_git_util.splitBugMapping(pupp_bug_info_repo)
print "Yes and no classification based on bug evidence"
yes_bug_mapping = y_n_bug_mapiing[0]
no_bug_mapping  = y_n_bug_mapiing[1]
files_that_have_defects = bug_git_util.getFilesFromMappingInfo(yes_bug_mapping)
files_that_are_mixed = bug_git_util.getFilesFromMappingInfo(no_bug_mapping)
no_deftect_files = bug_git_util.getNoDefectsOnlyFiles(files_that_have_defects, files_that_are_mixed)
# only pass files that have bugs in them , not the whole thing!
print "#"*75
# file 2 bug mapping file
y_file2bug= repo_path + "/" + "y_bug_msg.csv"
yf2b = open(y_file2bug, "w")
y_str_to_dump = bug_git_util.getAllDevelopmentMetricList(files_that_have_defects, repo_path, yes_bug_mapping, yf2b)
print "#"*75


# dumped yes metrics
#y_file_to_save = repo_path + "/" + "y_metrics.csv"
## 60 metrics now
y_file_to_save = repo_path + "/" + "y_ninety_metrics.csv"
y_dump_status = bug_git_util.dumpContentIntoFile(y_str_to_dump, y_file_to_save)
print "Dumped a CSV file of {} bytes".format(y_dump_status)
if len(no_deftect_files) > 0:
  #print no_bug_mapping
  n_file2bug= repo_path + "/" + "n_bug_msg.csv"
  nf2b = open(n_file2bug, "w")
  n_str_to_dump = bug_git_util.getAllDevelopmentMetricList(no_deftect_files, repo_path, no_bug_mapping, nf2b, False)

  # dumped no metrics
  #n_file_to_save = repo_path + "/" + "n_metrics.csv"
  ## 60 metrics now
  n_file_to_save = repo_path + "/" + "n_ninety_metrics.csv"
  n_dump_status = bug_git_util.dumpContentIntoFile(n_str_to_dump, n_file_to_save)
  print "Dumped a CSV file of {} bytes".format(n_dump_status)

else:
  print "Didn't find non-defected files! WOW!!"
print "#"*75
print "Count fo files was:", len(all_files)
print "The puppet to all file ratio was:", pp_to_all_file_ratio
print "#"*75
print "REPO:", repo_path
print "#"*75
print "defected file count:{}, no-defected files:{}".format(len(files_that_have_defects), len(no_deftect_files))
print "#"*75




#### For bug message project ::: start ::::
all_bug_msgs = bug_git_util.getBugMessages(yes_bug_mapping)
print "Count of all bug messages:", len(all_bug_msgs)
unique_bug_msg = np.unique(all_bug_msgs)
print "#"*75
print "Count of unique bug messages:", len(unique_bug_msg)
msg_file_to_save = repo_path + "/" + "bug_msgs.txt"
msgs_as_str=bug_git_util.dumpBugMessageAsStr(unique_bug_msg, msg_file_to_save)
print "#"*75
#### For bug message project ::: end ::::


'''
Oct 19, 2016
Dump all commit messages for all puppet files
the method getPuppetMessages will dump all
messages related to Puppet files in a text file
The mapping of puppet files to the commit messages
is available as _bug_msg.csv and n_bug_msg.csv
'bug_msgs.txt' only represents the messages to
y_bug_files
'''
all_pupp_msgs = bug_git_util.getPuppMessages(yes_bug_mapping, no_bug_mapping)
unique_pupp_msg = np.unique(all_pupp_msgs)
print "Count of all unique Puppet messages (both yes and no):", len(unique_pupp_msg)
print "#"*75
msg_file_pupp = repo_path + "/" + "pupp_bug_msgs.txt"
bug_git_util.dumpBugMessageAsStr(unique_pupp_msg, msg_file_pupp)
print "#"*75
print "Ended at:", bug_git_util.giveTimeStamp()
print "#"*75
