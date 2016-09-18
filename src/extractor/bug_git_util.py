# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:15:49 2016

@author: akond
"""



from SmellDetector import SmellDectector
from git import Repo
import  subprocess, os, time, datetime , numpy as np, re 
import sys
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
        print "$$ Defect detected @", msg_commit    
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
  headerStr1="Filename, max_nest_depth, class_dec, def_dec, pack_dec, file_dec, serv_dec, exec_dec, cohe_meth, body_txt_size,"
  headerStr2="lines_w_comm, lines_wo_comm, outerelems, file_reso, service_reso, package_reso, hard_coded_stmt, node_decl, parent_class,"
  headerStr3="churn, devCnt, bugCnt,"  
  headerStr = headerStr1 + headerStr2 + headerStr3 + "\n"
  #print file_churn_dict 
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

      # Metric -2: no of develoeprs involved  
      developerCmd="cd " + repo_abs_path  +" ; git blame -e " + file_relative_path + awkMagic_author
      developer_output = subprocess.check_output(['bash','-c', developerCmd])
      developer_churn_output = developer_output.split('\n')
      developer_churn_output = [x_ for x_ in developer_churn_output if x_!=''] 
      developer_churn_output = np.unique(developer_churn_output)      
      #print developer_churn_output
      developer_cnt_for_file = len(developer_churn_output)
      #print "Developer Count:", developer_cnt_for_file 
      metric_as_str_for_file = metric_as_str_for_file + str(developer_cnt_for_file) + ","       

      # Metric -3: no of bugs involved    
      bug_cnt = getRelevantCommitCount(uni_file_, allBugMapping, bugFlag)  
      # to handle weird values 
      if bug_cnt > churn_for_file:
        bug_cnt = bug_cnt - churn_for_file             
      print "Defect involvement count:", bug_cnt
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
      finalStr = finalStr + metric_as_str_for_file + "\n"      
      print "-"*50
      

      returnDirCommand= " cd /Users/akond/Documents/AkondOneDrive/OneDrive/Fall16-ThesisTopic/Puppeteer/"
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
  #print bugListParam    
  with open(fileParam, "a") as myfile_:
    for elm in bugListParam:   
      elm = elm + "\n"  
      myfile_.write(elm)

 