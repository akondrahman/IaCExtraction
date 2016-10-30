# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:15:49 2016

@author: akond
"""



from SmellDetector import SmellDectector
from git import Repo
import  subprocess, os, time, datetime , numpy as np, re
import sys, random, csv, os
reload(sys)
sys.setdefaultencoding('utf8')
getCheckFilesFromHashCommand="git diff-tree --no-commit-id --name-only --pretty=tformat:%h -r"
#getCheckFilesFromHashCommand="git diff-tree --no-commit-id --name-only -r"
def getPuppetFilesOfRepo(repo_dir_absolute_path):

  # unused but improtant command to add strings to bash output: | sed 's/$/,/'
  bashCommand= " find " + repo_dir_absolute_path + "  -type f -name '*.pp' ;"
  pupp_file_output = subprocess.check_output(['bash','-c', bashCommand])
  output_as_list = pupp_file_output.split('\n')
  #print dir(pupp_file_output)
  #print output_as_list
  print "length: before filtering", len(output_as_list)
  output_as_list = [x for x in output_as_list if x!='']
  output_as_list = np.unique(output_as_list)
  print "length: after filtering", len(output_as_list)
  return output_as_list




def getPuppRelatedCommits(repo_dir_absolute_path, ppListinRepo, branchName='master'):
  mappedPuppetList=[]
  track_exec_cnt = 0
  repo_  = Repo(repo_dir_absolute_path)
  all_commits = list(repo_.iter_commits(branchName))
  print "Total commits in this branch ", len(all_commits)
  for each_commit in all_commits:
    track_exec_cnt = track_exec_cnt + 1
    #print "\t \t ***So far {} commits processed*** ".format( track_exec_cnt )
    #tree_for_commit = each_commit.tree  ## this is giivng systematic overshhoting of commits
    #tree_diff = repo_.git.diff(tree_for_commit)
    #print each_commit
    # naother apporach
    cmd_of_interrest1 = "cd  " + repo_dir_absolute_path + " ; "
    cmd_of_interrest2 = "git show --name-status " + str(each_commit)  +  "  | awk '/.pp/ {print $2}'"
    cmd_of_interrest = cmd_of_interrest1 + cmd_of_interrest2
    commit_of_interest  = subprocess.check_output(['bash','-c', cmd_of_interrest])
    #print commit_of_interest
    for ppFile in ppListinRepo:
      if ppFile in commit_of_interest:
       #print "Asi mama asi, commit:{}, file:{}".format(each_commit, ppFile)
       file_with_path = os.path.join(repo_dir_absolute_path, ppFile)
       mapped_tuple = (file_with_path, each_commit)
       mappedPuppetList.append(mapped_tuple)
       #print "-"*50
  #print mappedPuppetList
  print "Total matched puppet commits", len(mappedPuppetList)
  return mappedPuppetList



def getPuppRelatedBugInfo(repo_path_param, repo_branch_param, pupp_commits_mapping):
  track_exec_cnt = 0
  pupp_bug_list = []
  for tuple_ in pupp_commits_mapping:
    track_exec_cnt =   track_exec_cnt + 1
    #print "\t \t ***So far {} commits processed*** ".format( track_exec_cnt )
    file_ = tuple_[0]
    commit_ = tuple_[1]
    msg_commit =  commit_.message.lower()
    #if (('fix' in msg_commit)or ('bug' in msg_commit)or ('patch' in msg_commit)):
    if ('merg' in msg_commit) or ('no bug' in msg_commit) or ('debug' in msg_commit) or ('out' in msg_commit) or ('revert' in msg_commit):
        tup_ = (file_, msg_commit, 'n', msg_commit)
    else:
      #if (  ('bug' in msg_commit) or ('fix' in msg_commit) ):
      #if ( getBugIDMatch(msg_commit)or ('fix' in msg_commit) ):
      if ('bug' in msg_commit) :
        #print "$$ Defect detected @", msg_commit
        tup_ = (file_, msg_commit, 'y', msg_commit)
      else:
        tup_ = (file_, msg_commit, 'n', msg_commit)
    pupp_bug_list.append(tup_)
  #print pupp_bug_list
  return pupp_bug_list

def splitBugMapping(bug_map_param):
  tupToRet = ()
  y_bug_list = []
  n_bug_list = []
  for elem in bug_map_param:
    status_ = elem[2]
    if status_=='y':
      y_bug_list.append(elem)
    else:
      n_bug_list.append(elem)
  print "len-y:{}, len-n:{}".format(len(y_bug_list), len(n_bug_list))
  tupToRet=(y_bug_list, n_bug_list)
  return tupToRet


def getFilesFromMappingInfo(mappingListParam, bugFlag=True):
  list_of_files = []
  for tuple_ in mappingListParam:
     file_in_tuple = tuple_[0]
     list_of_files.append(file_in_tuple)
  list_of_files = np.unique(list_of_files)
  return list_of_files



def getRelPathOfFiles(all_pp_param, repo_dir_absolute_path):
  common_path = repo_dir_absolute_path
  files_relative_paths = [os.path.relpath(path, common_path) for path in all_pp_param]

  #print files_relative_paths
  return files_relative_paths
def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret
def getGitChurnOfRepo(repo_abs_pathP):
  dictToRet={}
  churn_magic_sauce = "git log --all -M -C --name-only --format='format:' $@ | sort | grep -v '^$' | uniq -c | sort -n "
  awk_magic_sauce = "| awk '{print $1,$2}' | sed -e  's/ /,/g'"
  churnCmd="cd " + repo_abs_pathP  +" ; " +  churn_magic_sauce  + awk_magic_sauce
  repo_churn_output = subprocess.check_output(['bash','-c', churnCmd])
  repo_churn_output = repo_churn_output.split('\n')
  repo_churn_output = [x_ for x_ in repo_churn_output if x_!='']
  #print repo_churn_output
  for fileElem in repo_churn_output:
    splitted_ = fileElem.split(',')
    cnt_splitted = splitted_[0]
    fileName_Splitted = splitted_[1]
    if '.pp' in fileName_Splitted:
      dictToRet[fileName_Splitted]=cnt_splitted
  #print dictToRet
  return dictToRet
awkMagic_author = "| awk '{ print $2}' ;"
def getRelevantCommitCount(file_abs_path, allBugMapping, bugFlag=True):
  file_cnt = 0
  if bugFlag:
    for tuple_ in allBugMapping:
      #print "asi mama:", tuple_
      #print "khaisi:", file_abs_path
      file_ = tuple_[0]
      if file_==file_abs_path:
        file_cnt = file_cnt + 1
  else:
    file_cnt =  0
  return file_cnt



def getBugIDMatch(messageToSearchParam):
  valToRet=False
  #matched_elems = re.findall(r'[\bbug\b].*[0-9]+', messageToSearchParam)
  matched_elems = re.findall(r'[\bbug\b]', messageToSearchParam)
  if len(matched_elems) > 0:
    valToRet = True
  return valToRet

def getChurnForFile(dictParam, file_rel_pathParam):
  cntToRet = '0'
  if file_rel_pathParam in dictParam:
    cntToRet = dictParam[file_rel_pathParam]
  return cntToRet

def getBugMessageForFile(file_abs_path, allBugMapping):
  msg2ret=""
  for tuple_ in allBugMapping:
      file_ = tuple_[0]
      if file_==file_abs_path:
        msg2ret= msg2ret  + tuple_[-1]  + '|'
  return msg2ret

def getAllDevelopmentMetricList(uniqueFileList, repo_abs_path, allBugMapping, msgfile_, bugFlag=True):
  file_churn_dict = getGitChurnOfRepo(repo_abs_path)
  headerStr1="Filename,max_nest_depth,class_dec,def_dec,pack_dec,file_dec,serv_dec,exec_dec,cohe_meth,body_txt_size,"
  # 9 metrics
  headerStr2="lines_w_comm,lines_wo_comm,outerelems,file_reso,service_reso,package_reso,hard_coded_stmt,node_decl,parent_class,"
  # 9 metrics
  headerStr3="d_class_dec,d_define_dec,d_pack_dec,d_file_dec,d_serv_dec,d_exec_dec,d_outerlem,d_hardcode,"
  # 8 metrics
  headerStr4="cnt_include,cnt_git,cnt_req,cnt_noti,cnt_ensur,cnt_alias,cnt_subsc,cnt_consum,cnt_export,cnt_sched,cnt_of_stage,"
  # 11 metrics
  headerStr5="cnt_tag,cnt_noop,cnt_before,cnt_audit,meta_param_total_cnt,cnt_inheri,cnt_sql,non_pp_cnt,mcx_cnt,rsyslog_cnt,"
  # 10 metrics
  headerStr6="validhash_cnt,reqpack_cnt,hieraincl_cnt,inclpacks_cnt,ensurepacks_cnt,if_cnt,undef_cnt,"
  # 7 metrics
  headerStr7="avgparam_cnt,mediparam_cnt,maxparam_cnt,min_param_cnt,var_assi_cnt,"
  # 5 metrics
  headerStr8="case_stmt_cnt,env_cnt,crone_cnt,reff_cnt,total_reso_cnt_per_file,total_reso_cnt_per_blocks,"
  # 6 metrics
  headerStr9="total_reso_cnt_per_lines,svc_cnt_per_blocks,inc_per_svc_cnt,inc_per_pkg_cnt,inc_per_file_cnt,inc_per_tot_reso_cnt,"
  # 6 metrics
  headerStr10="inc_per_line,cron_per_line,if_cnt_per_block,incl_cnt_per_block,req_pack_cnt_per_block,pack_decl_cnt_per_block,"
  # 6 metrics
  headerStr11="req_pack_cnt_per_lines,require_per_lines,var_per_lines,var_to_reffs,reffs_per_block,reff_cnt_per_lines,"
  # 6 metrics
  headerStr12="reff_cnt2total_reso,reff_cnt2req_pack,reff_cnt2incl_cnt,"
  # 3 metrics
  headerStr13="churn,UdevCnt,bugCnt,defectStatus"
  # 2 metrics
  '''
    In total we have 88 metrics now ... enough ? :-P
  '''
  headerStr = headerStr1 + headerStr2 + headerStr3 +  headerStr4 +  headerStr5 + headerStr6 + headerStr7 + headerStr8 + headerStr9 + headerStr10 + headerStr11 + headerStr12 + headerStr13 + "\n"
  #print file_churn_dict
  '''
    extra header for defect falg, used in predcition modeling
  '''
  defectHeader=""
  '''
  '''
  finalStr= headerStr
  for uni_file_ in uniqueFileList:
      metric_as_str_for_file=""
      file_relative_path = os.path.relpath(uni_file_, repo_abs_path)
      print "File currently analyzed: ", file_relative_path
      metric_as_str_for_file = metric_as_str_for_file + uni_file_ + ","

      puppeteer_metrics_for_file = SmellDectector.getMetricsForFile(uni_file_)
      #print puppeteer_metrics_for_file
      metric_as_str_for_file = metric_as_str_for_file + puppeteer_metrics_for_file

      # Metric-1: Churn
      churn_for_file = getChurnForFile(file_churn_dict, file_relative_path)
      #print "Churn:", churn_for_file
      metric_as_str_for_file = metric_as_str_for_file + churn_for_file + ","

      # Metric -2 and 3: no of develoeprs involved
      developerCmd="cd " + repo_abs_path  +" ; git blame -e " + file_relative_path + awkMagic_author
      developer_output = subprocess.check_output(['bash','-c', developerCmd])
      developer_churn_output = developer_output.split('\n')
      developer_churn_output = [x_ for x_ in developer_churn_output if x_!='']
      '''
      # Metric -2: no of develoeprs involved .... gives erroneous results, will not be used
      act_dev_cnt = len(developer_churn_output)
      metric_as_str_for_file = metric_as_str_for_file + str(act_dev_cnt) + ","
      '''
      # Metric -3: no of unqiue develoeprs involved
      developer_churn_output = np.unique(developer_churn_output)
      #print developer_churn_output
      developer_cnt_for_file = len(developer_churn_output)
      #print "Developer Count:", developer_cnt_for_file
      ### developer_cnt_for_file presents the unique number of developers for the file
      metric_as_str_for_file = metric_as_str_for_file + str(developer_cnt_for_file) + ","

      # Metric -4: no of bugs involved
      bug_cnt = getRelevantCommitCount(uni_file_, allBugMapping, bugFlag)
      # to handle weird values
      if bug_cnt > churn_for_file:
        bug_cnt = bug_cnt - churn_for_file
      #print "Defect involvement count:", bug_cnt
      metric_as_str_for_file = metric_as_str_for_file + str(bug_cnt) + ","

      # Extra: message to bug mapping
      bug_msg = getBugMessageForFile(uni_file_, allBugMapping)
      bug_msg = bug_msg.replace('\n', '\t')
      str2write= uni_file_ + "," + bug_msg
      #print "LOL: ", str2write
      print >> msgfile_, str2write

      # Metric -4: no of commmits involved , will not be used as similar to churn
      # allCommitMapping doesn't have full path fo file
      #commit_cnt = getRelevantCommitCount(uni_file_, allCommitMapping)
      #print "Commit involvement count:", commit_cnt
      # Metric -5: timestamp   ::: attempted, but too little for a lot of effort, abadoning ....
      #timestamp = getListOfTimestamp(uni_file_, repo_abs_path)
      #print "Commit involvement count:", commit_cnt
      #print "FULL STR:", metric_as_str_for_file

      # # Extra header to faculitatte preition models : Oct 03, 2016
      # if (bugFlag):
      #   defectHeader = 'Y'
      # else:
      #   defectHeader = 'N'

      # Extra header to facilitate prediction models : Oct 15, 2016
      if (bugFlag):
        defectHeader = '1'
      else:
        defectHeader = '0'





      metric_as_str_for_file = metric_as_str_for_file +  defectHeader + ','




      ##The whole thing
      finalStr = finalStr + metric_as_str_for_file + "\n"
      print "-"*50


      #returnDirCommand= " cd /Users/akond/Documents/AkondOneDrive/OneDrive/Fall16-ThesisTopic/Puppeteer/"
      returnDirCommand= " cd ."
      subprocess.check_output(['bash','-c', returnDirCommand])


  return finalStr



def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)


def getNoDefectsOnlyFiles(defected, mixed):
  defected_set = set(defected)
  mixed_set  = set(mixed)
  diff_set = mixed_set - defected_set
  non_defect_list = list(diff_set)
  return non_defect_list




def getRecursivelyAlFilles(repo_path):
  all_files = []
  for root, subFolders, _files in os.walk(repo_path):
    all_files.append(_files)
  return all_files




def getBugMessages(bugMappingParam):
  list_ =[]
  bug_msg_=""
  for tup_ in bugMappingParam:
    bug_msg_ = tup_[-1]
    list_.append(bug_msg_)
  return list_



def encodeStr(strParam):
  text=""
  try:
    text = unicode(strParam, 'utf-8')
  except TypeError:
    text =" "
  return text



def dumpBugMessageAsStr( bugListParam, fileParam):
  indexCount=1
  #print bugListParam
  with open(fileParam, "a") as myfile_:
    for elm in bugListParam:
      tmpStr = ""
      #elm = elm + "\n"
      tmpStr = tmpStr + str(indexCount) + ',' + elm
      tmpStr = tmpStr + '------------------------------' + '\n'
      myfile_.write(tmpStr)
      indexCount = indexCount + 1

'''
Oct 19, 2016
This method grabs all the messages for both yes and no defected files
and dumps them in a aseperate file
'''
def getPuppMessages(yesBugMappingParam, noBugMappingParam):
  list_ =[]
  dict2ret={}
  bug_msg_=""
  for tup_ in yesBugMappingParam:
    bug_msg_ = tup_[-1]
    list_.append(bug_msg_)
    fileName = tup_[0]
    if fileName in dict2ret:
      tmpList = dict2ret[fileName]
      tmpList.append(bug_msg_)
      dict2ret[fileName] = tmpList
      tmpList = []
    else:
       tmpList = [bug_msg_]
       dict2ret[fileName] = tmpList
       tmpList = []
  for tup_ in noBugMappingParam:
    bug_msg_ = tup_[-1]
    list_.append(bug_msg_)
    fileName = tup_[0]
    if fileName in dict2ret:
      tmpList = dict2ret[fileName]
      tmpList.append(bug_msg_)
      dict2ret[fileName] = tmpList
      tmpList = []
    else:
       tmpList = [bug_msg_]
       dict2ret[fileName] = tmpList
       tmpList = []
  return list_, dict2ret
'''
Oct 21, 2016
'''
def dumpRandBugMessageAsStr(unique_pupp_msg_papram, rand_msg_file_pupp_param, qual_coding_file_param, randRangeParam, msgCntParam, pupp_to_msgs_dict_param, msg_to_id_file_param):
  indexCount=1
  rand_indices = [random.randint(1, msgCntParam) for x in xrange(randRangeParam)]
  #print len(rand_indices)
  qual_mapping_str=""
  ''' ID to message mapping for better data crucnhing
      CCERP Start Oct 29
  '''
  msg_to_id_mapping_str=""
  ''' ID to message mapping for better data crucnhing
      CCERP End Oct 29
  '''
  #print bugListParam
  matchedFileName=""

  with open(rand_msg_file_pupp_param, "a") as myfile_:
    for elm in unique_pupp_msg_papram:
       #elm = elm.replace('\n', '')
       if indexCount in rand_indices:
          tmpStr = ""
          tmpStr = tmpStr + str(indexCount) + ',' + elm
          tmpStr = tmpStr + '\n' + '------------------------------' + '\n'
          myfile_.write(tmpStr)
          qual_mapping_str = qual_mapping_str + str(indexCount) + "," + "\n"
          '''
          added Oct 29, 2016
          '''
          if checkIfMsgInDict(elm, pupp_to_msgs_dict_param):
            matchedFileName =  getMatchingFileNameForMsg(elm, pupp_to_msgs_dict_param) # need the indexing to get the name of the list
            #print "The matching file:", matchedFileName
            msg_to_id_mapping_str = msg_to_id_mapping_str + str(indexCount) + ',' + matchedFileName + ',' + '\n'
       indexCount = indexCount + 1

  dumpContentIntoFile(qual_mapping_str, qual_coding_file_param)
  '''
  added Oct 29, 2016
  '''
  dumpContentIntoFile(msg_to_id_mapping_str, msg_to_id_file_param)
'''
Read projects from csv file, for eligible projects
'''
def getEligibleProjectsFromCSVForRandAnalysis(fileNameParam):
  repo_list = []
  with open(fileNameParam, 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
      subList = []
      name_ = row[0]
      subList.append(name_)
      srs__ = int(row[1])  # coutn of samples determined by 95% CI
      subList.append(srs__)
      full_ = int(row[2])  # count of all samples related to puppet
      subList.append(full_)
      repo_list.append(subList)
  return repo_list


def checkIfMsgInDict(elemParam, dictToSearchParam):
   returnVal = False
   for k_, v_ in dictToSearchParam.items():
    if elemParam in v_:
       returnVal = True
   return returnVal




def getMatchingFileNameForMsg(msgParam, dictToSearchParam):
    fileToRet='None'
    for k_, v_ in dictToSearchParam.items():
      if msgParam in v_:
        fileToRet=k_
        #print "msg:{}, listOfMsgs:{}".format(msgParam, v_)
    return fileToRet


def performCleanUp(fileParam):
  '''
     Oct 29, 2016 
     deleet the file
  '''
  if os.path.isfile(fileParam):
    os.remove(fileParam)
