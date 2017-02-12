# -*- coding: utf-8 -*-
"""
Created on Oct 21, 2016

@author: akond
"""



import hglib , subprocess, os, time, datetime, re, numpy as np
import bug_hg_developer, dict_holder as dh



def splitBugMapping(bug_map_param):
  tupToRet = ()
  y_bug_list = []
  n_bug_list = []
  for elem in bug_map_param:
    #print "el", elem
    status_ = elem[2]
    #print "line 111", status_
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


def getPuppetCommitMapping(all_commits_param, legit_files_param, bashCommand, pp_files):
  listToRet = []
  cnt_ = 0
  for e in  all_commits_param:
    #print "hg:Commit desc:", e
    commit_hash = e[1]
    ## for timestamp
    timestamp = e[-1]
    cnt_ = cnt_ + 1
    #print "Total {} commits analyzed ".format(cnt_)
    #print commit_hash
    diffCommand = bashCommand + commit_hash
    diff_output = subprocess.check_output(['bash','-c', diffCommand])
    #print diff_output
    for legitFile in pp_files:
      if(legitFile in diff_output):
        #print "Mapping found !!!"
        tmp_tup = (legitFile, commit_hash, timestamp)
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


def getPuppetBugMappingList(mappingListParam, repo_abs_path, bashCommand, pp_files):
  listToRet = []
  cnt_ = 0
  for tuple_elem in mappingListParam:
    file_ = tuple_elem[0]
    commit_hash = tuple_elem[1]
    ###timestamp
    time_ = tuple_elem[-1]
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
        tup_ = (file_to_save, commit_hash, 'n', diff_output, time_)
    else:
      #if (('bug' in diff_output) or ('fix' in diff_output)):
      if ('bug' in diff_output):
        #print "$$ Bug detected @", diff_output
        tup_ = (file_to_save, commit_hash, 'y', diff_output, time_)
      else:
        tup_ = (file_to_save, commit_hash, 'n', diff_output, time_)
    listToRet.append(tup_)
    #returnDirCommand= " cd /Users/akond/Documents/AkondOneDrive/OneDrive/Fall16-ThesisTopic/Puppeteer/"
    returnDirCommand= " cd ."
    ret_dir_output = subprocess.check_output(['bash','-c', returnDirCommand])
  return listToRet






def rand_bug_hg_main(orgParamName, repo_name_param, branchParam, randRangeParam, msgCntP):
    print "Started at:", giveTimeStamp()
    print "#"*75
    # repo_path="/Users/akond/PUPP_REPOS/v2/mozilla_releng_only/puppet"
    # repo_branch="master"
    repo_path="/Users/akond/PUPP_REPOS/"+orgParamName+"/"+repo_name_param
    repo_branch=branchParam
    bashCommand= " cd " + repo_path  +" ; hg log -p -r "
    repo_complete = hglib.open(repo_path)
    files = list(repo_complete.manifest())
    pp_files =getLegitFiles(files)
    #print "Count of legit files:", len(pp_files)
    pp_to_all_file_ratio = (float(len(pp_files))/float(len(files)))
    all_commits = repo_complete.log()
    #print "All commit count", len(all_commits)
    puppet_commit_mapping_list = getPuppetCommitMapping(all_commits, pp_files, bashCommand, pp_files)
    print "Performed commit mapping"
    print "#"*75
    puppet_bug_mapping_list = getPuppetBugMappingList(puppet_commit_mapping_list, repo_path, bashCommand, pp_files)
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
    y_file2bug= repo_path + "/" + "randFile_y_bug_msg.csv"
    # doing cleanup tp prevent false appendig
    bug_hg_developer.performCleanUp(y_file2bug)
    yf2b = open(y_file2bug, "w")
    y_str_to_dump = bug_hg_developer.getAllDevelopmentMetricList(files_that_have_defects, repo_path, yes_bug_mapping, yf2b)
    print "#"*75
    #print str_to_dump
    # dumped yes metrics
    #y_file_to_save = repo_path + "/" + "y_metrics.csv"
    ## 60 metrics now
    y_file_to_save = repo_path + "/" + "randFile_y_ninety_metrics.csv"
    # doing cleanup tp prevent false appendig
    bug_hg_developer.performCleanUp(y_file_to_save)
    y_dump_status = bug_hg_developer.dumpContentIntoFile(y_str_to_dump, y_file_to_save)
    print "Dumped a CSV file of {} bytes".format(y_dump_status)
    print "#"*75
    if len(no_deftect_files) > 0:
      #print no_bug_mapping
      # even though I am passing , "n_bug_msg.csv" it will eb ana empty file as no bug messgaes for files that dont have bugs
      # file 2 bug mapping file
      n_file2bug= repo_path + "/" + "randFile_n_bug_msg.csv"
      # doing cleanup tp prevent false appendig
      bug_hg_developer.performCleanUp(n_file2bug)
      nf2b = open(n_file2bug, "w")
      n_str_to_dump = bug_hg_developer.getAllDevelopmentMetricList(no_deftect_files, repo_path, no_bug_mapping , nf2b, False)
      # dumped no metrics
      #n_file_to_save = repo_path + "/" + "n_metrics.csv"
      ## 60 metrics now
      n_file_to_save = repo_path + "/" + "randFile_n_ninety_metrics.csv"
      # doing cleanup tp prevent false appendig
      bug_hg_developer.performCleanUp(n_file_to_save)
      n_dump_status = bug_hg_developer.dumpContentIntoFile(n_str_to_dump, n_file_to_save)
      print "Dumped a CSV file of {} bytes".format(n_dump_status)
      print "#"*75
    else:
      print "Didn't find non-defected files! "
      print "Wow!"*10
    print "#"*75
    #print "Count fo files was:", len(files)
    #print "The puppet to all file ratio was:", pp_to_all_file_ratio
    #print "#"*75
    print "REPO:", repo_path
    print "#"*75
    print "total puppet files:{}, defected file count:{}, no-defected files:{}".format(len(pp_files), len(files_that_have_defects), len(no_deftect_files))
    print "#"*75



    #### For bug message project ::: start ::::
    all_bug_msgs = bug_hg_developer.getBugMessages(yes_bug_mapping)
    print "Count of all bug messages:", len(all_bug_msgs)
    print "#"*75
    unique_bug_msg = np.unique(all_bug_msgs)
    print "Count of unique bug messages:", len(unique_bug_msg)
    print "#"*75
    msg_file_to_save = repo_path + "/" + "randFile_bug_msgs.txt"
    # doing cleanup tp prevent false appendig
    bug_hg_developer.performCleanUp(msg_file_to_save)
    #msgs_as_str=bug_hg_developer.dumpBugMessageAsStr(unique_bug_msg, msg_file_to_save)

    #### For bug message project ::: end ::::



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
    # all_pupp_msgs = bug_hg_developer.getPuppMessages(yes_bug_mapping, no_bug_mapping)
    # unique_pupp_msg = np.unique(all_pupp_msgs)
    # print "Count of all unique Puppet messages (both yes and no):", len(unique_pupp_msg)
    # print "#"*75
    # msg_file_pupp = repo_path + "/" + "pupp_bug_msgs.txt"
    # bug_hg_developer.dumpBugMessageAsStr(unique_pupp_msg, msg_file_pupp)
    # print "#"*75




    '''
    Oct 21, 2016
    get randomly selected bug messages for qual. coding
    '''
    all_pupp_msgs, pupp_to_msgs_dict = bug_hg_developer.getPuppMessages(yes_bug_mapping, no_bug_mapping)
    '''
    for itme handling
    '''
    time2messagDict = bug_git_util.getPuppTimestamps(yes_bug_mapping, no_bug_mapping)
    unique_pupp_msg = np.unique(all_pupp_msgs)
    print "Count of all unique Puppet messages (both yes and no):", len(unique_pupp_msg)
    print "#"*75
    rand_msg_file_pupp = repo_path + "/" + "randFile_pupp_bug_msgs.txt"
    # doing cleanup tp prevent false appendig
    bug_hg_developer.performCleanUp(rand_msg_file_pupp)
    qual_coding_file =   repo_path + "/" + "randFile_qual_coding.csv"
    # doing cleanup tp prevent false appendig
    bug_hg_developer.performCleanUp(qual_coding_file)
    '''
    Added Oct 29, 2016
    '''
    msg_to_id_fileP =   repo_path + "/" + "randFile_msg_to_file_map.txt"
    # doing cleanup tp prevent false appendig
    bug_hg_developer.performCleanUp(msg_to_id_fileP)
    '''
    '''
    #bug_hg_developer.dumpRandBugMessageAsStr(unique_pupp_msg, rand_msg_file_pupp, qual_coding_file, randRangeParam, msgCntP, pupp_to_msgs_dict, msg_to_id_fileP, repo_path)
    print "#"*75
    '''
    Added Nov 01, 2016
    '''
    ## for message to file mapping
    full_map_fileP =   repo_path + "/" + "fullThrottle_msg_file_map.csv"
    ## for message to id mapping
    full_map_IDP =   repo_path + "/" + "fullThrottle_msg_ID_map.csv"
    # doing cleanup tp prevent false appendig
    bug_hg_developer.performCleanUp(full_map_fileP)
    ## for qual coding
    full_qual_fileP =   repo_path + "/" + "fullThrottle_qual_coding.csv"
    bug_hg_developer.performCleanUp(full_qual_fileP)
    ## for dumping messages
    all_msg_file_pupp_param =   repo_path + "/" + "fullThrottle_msgs.txt"
    bug_hg_developer.performCleanUp(full_qual_fileP)
    ## call the method
    bug_hg_developer.dumpFullBugMessageAsStr(unique_pupp_msg, all_msg_file_pupp_param, full_qual_fileP, pupp_to_msgs_dict, full_map_fileP, repo_path, full_map_IDP, time2messagDict)




    '''
    Dec 06, 2016 : preparation for phase 2 qualitative coding
    '''
    # partial_content_file_ = repo_path + "/" + "phase_two_qual_coding.csv"
    # excludeDict= dh.excludeDictForMozilla
    # excludeIDList = excludeDict[repo_path]
    # bug_hg_developer.performCleanUp(partial_content_file_)
    # bug_hg_developer.dumpPhaseTwoBugMessageAsStr(unique_pupp_msg, partial_content_file_, pupp_to_msgs_dict, excludeIDList, repo_path)
    print "Ended at:", giveTimeStamp()
    print "#"*75



'''
get the whole list of eligible projects
'''
orgName='mozilla-releng-downloads'
fileName="/Users/akond/PUPP_REPOS/"+orgName+'/'+'eligible_repos.csv'
elgibleProjects=bug_hg_developer.getEligibleProjectsFromCSVForRandAnalysis(fileName)
#print elgibleProjects
'''
Call the function
'''
for proj_ in elgibleProjects:
  # 0. org name: 1. project name  2. branch name  3.  95% sample  4. all messages
  print "Processing ", proj_
  rand_bug_hg_main(orgName, proj_[0], 'master', proj_[1], proj_[2])
  print "="*75
