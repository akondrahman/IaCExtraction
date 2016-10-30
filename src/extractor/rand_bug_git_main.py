# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 2016

@author: akond
"""



import numpy as np
import bug_git_util
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def rand_bug_git_main(orgParamName, repo_name_param, branchParam, randRangeParam, msgCntP):
  print "Started at:", bug_git_util.giveTimeStamp()

  # do not end path with '/'
  repo_path="/Users/akond/PUPP_REPOS/"+orgParamName+"/"+repo_name_param
  repo_branch=branchParam

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
  y_file2bug= repo_path + "/" + "randFile_y_bug_msg.csv"
  # doing cleanup tp prevent false appendig
  bug_git_util.performCleanUp(y_file2bug)
  yf2b = open(y_file2bug, "w")
  y_str_to_dump = bug_git_util.getAllDevelopmentMetricList(files_that_have_defects, repo_path, yes_bug_mapping, yf2b)
  print "#"*75


  # dumped yes metrics
  #y_file_to_save = repo_path + "/" + "y_metrics.csv"
  ## 60 metrics now
  y_file_to_save = repo_path + "/" + "randFile_y_ninety_metrics.csv"
  # doing cleanup tp prevent false appendig
  bug_git_util.performCleanUp(y_file_to_save)
  y_dump_status = bug_git_util.dumpContentIntoFile(y_str_to_dump, y_file_to_save)
  print "Dumped a CSV file of {} bytes".format(y_dump_status)
  if len(no_deftect_files) > 0:
    #print no_bug_mapping
    n_file2bug= repo_path + "/" + "randFile_n_bug_msg.csv"
    # doing cleanup tp prevent false appendig
    bug_git_util.performCleanUp(n_file2bug)
    nf2b = open(n_file2bug, "w")
    n_str_to_dump = bug_git_util.getAllDevelopmentMetricList(no_deftect_files, repo_path, no_bug_mapping, nf2b, False)

    # dumped no metrics
    #n_file_to_save = repo_path + "/" + "n_metrics.csv"
    ## 60 metrics now
    n_file_to_save = repo_path + "/" + "randFile_n_ninety_metrics.csv"
    # doing cleanup tp prevent false appendig
    bug_git_util.performCleanUp(n_file_to_save)
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




  # #### For bug message project ::: start ::::
  # all_bug_msgs = bug_git_util.getBugMessages(yes_bug_mapping)
  # print "Count of all bug messages:", len(all_bug_msgs)
  # unique_bug_msg = np.unique(all_bug_msgs)
  # print "#"*75
  # print "Count of unique bug messages:", len(unique_bug_msg)
  # msg_file_to_save = repo_path + "/" + "bug_msgs.txt"
  # msgs_as_str=bug_git_util.dumpBugMessageAsStr(unique_bug_msg, msg_file_to_save)
  # print "#"*75
  # #### For bug message project ::: end ::::
  #
  #
  # '''
  # Oct 19, 2016
  # Dump all commit messages for all puppet files
  # the method getPuppetMessages will dump all
  # messages related to Puppet files in a text file
  # The mapping of puppet files to the commit messages
  # is available as _bug_msg.csv and n_bug_msg.csv
  # 'bug_msgs.txt' only represents the messages to
  # y_bug_files
  # '''
  # all_pupp_msgs = bug_git_util.getPuppMessages(yes_bug_mapping, no_bug_mapping)
  # unique_pupp_msg = np.unique(all_pupp_msgs)
  # print "Count of all unique Puppet messages (both yes and no):", len(unique_pupp_msg)
  # print "#"*75
  # msg_file_pupp = repo_path + "/" + "pupp_bug_msgs.txt"
  # bug_git_util.dumpBugMessageAsStr(unique_pupp_msg, msg_file_pupp)
  # print "#"*75
  # print "Ended at:", bug_git_util.giveTimeStamp()
  # print "#"*75





  '''
  Oct 21, 2016
  get randomly selected bug messages for qual. coding
  '''
  all_pupp_msgs, pupp_to_msgs_dict = bug_git_util.getPuppMessages(yes_bug_mapping, no_bug_mapping)
  unique_pupp_msg = np.unique(all_pupp_msgs)
  print "Count of all unique Puppet messages (both yes and no):", len(unique_pupp_msg)
  print "#"*75
  # pupp_to_msgs_dict contains puppet files as dict keys, and the values are the corresponding messages
  rand_msg_file_pupp = repo_path + "/" + "randFile_pupp_bug_msgs.txt"
  # doing cleanup tp prevent false appendig
  bug_git_util.performCleanUp(rand_msg_file_pupp)
  qual_coding_file   = repo_path + "/" + "randFile_qual_coding.csv"
  # doing cleanup tp prevent false appendig
  bug_git_util.performCleanUp(qual_coding_file)
  '''
  Added Oct 29, 2016
  '''
  msg_to_id_fileP =   repo_path + "/" + "randFile_msg_file_map.csv"
  # doing cleanup tp prevent false appendig
  bug_git_util.performCleanUp(msg_to_id_fileP)
  '''
  '''
  bug_git_util.dumpRandBugMessageAsStr(unique_pupp_msg, rand_msg_file_pupp, qual_coding_file, randRangeParam, msgCntP, pupp_to_msgs_dict, msg_to_id_fileP)
  print "#"*75
  print "Ended at:", bug_git_util.giveTimeStamp()
  print "#"*75

'''
get the whole list of eligible projects
'''
orgName='wikimedia-downloads'
fileName="/Users/akond/PUPP_REPOS/"+orgName+'/'+'eligible_repos.csv'
elgibleProjects=bug_git_util.getEligibleProjectsFromCSVForRandAnalysis(fileName)

'''
Call the function
'''
for proj_ in elgibleProjects:
  # 0. org name: 1. project name  2. branch name  3.  95% sample  4. all messages
  #rand_bug_git_main('puppet-oslo', 'master', 31, 34)
  print "Processing ", proj_
  rand_bug_git_main(orgName, proj_[0], 'master', proj_[1], proj_[2])
  print "="*75

'''
Seperate function for one project only
'''
# rand_bug_git_main(orgName, 'puppet', 'master', 74, 8085)
# print "="*75
