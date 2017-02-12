# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:30:41 2016

@author: akond
"""



from SmellDetector import SmellDectector
import csv, os , random,  subprocess, numpy as np
awkMagic_author = "| awk '{ print $1}'   | sed -e 's/ /,/g' ;"
#only interested in the first field, make outptu ocmma seprated
awkMagic_churn  = "| awk '{ print $2}'   | sed -e 's/ /,/g' ;"

def getRelevantCommitCount(file_abs_path, allBugMapping, bugFlag=True):
  file_cnt = 0
  if bugFlag:
    for tuple_ in allBugMapping:
      file_ = tuple_[0]
      if file_==file_abs_path:
        file_cnt = file_cnt + 1
  else:
    file_cnt =  0
  return file_cnt



def getUniqueFiles(allBugParam):
  listToRet=[]
  for elem in allBugParam:
    file_ = elem[0]
    if file_ not in listToRet:
      listToRet.append(file_)
  return listToRet




def getChurnFromStr(splitted_param):
  valToRet = 0
  tmp_ = 0
  for elem in splitted_param:
    if '\n' in elem:
      elem=elem.split('\n')[0]
    else:
      elem = elem
    if (elem !=''):
    #if (elem !='') and (isinstance(elem, int)):
      tmp_ = int(elem)
    valToRet = valToRet + tmp_
  return valToRet

def getNonUniqueDevelopers(develParamList):
  list_to_ret = []
  for elem_ in develParamList:
    if '\n' in elem_:
      splitted_elem  = elem_.split('\n')
      splitted_elem = [x_ for x_ in splitted_elem if x_!='']
      for subElems in splitted_elem:
          list_to_ret.append(subElems)
  return list_to_ret

def getUniqueDevelopers(develParamList):
  uni_list_to_ret = []
  for elem_ in develParamList:
    if '\n' in elem_:
      splitted_elem  = elem_.split('\n')
      splitted_elem = [x_ for x_ in splitted_elem if x_!='']
      for subElems in splitted_elem:
        if subElems not in uni_list_to_ret:
          uni_list_to_ret.append(subElems)
  return uni_list_to_ret

def getBugMessageForFile(file_abs_path, allBugMapping):
  msg2ret=""
  for tuple_ in allBugMapping:
      file_ = tuple_[0]
      if file_==file_abs_path:
        #msg2ret= msg2ret  + tuple_[-1]  + '|'
        msg2ret= msg2ret  + tuple_[3]  + '|'      # 3 gives messages, 4 gives timestamp, the last elemnt of tiemstamp
  return msg2ret

def getAllDevelopmentMetricList(uniqueFileList, repo_abs_path, allBugMapping, msgfile_, bugFlag=True):
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
      print "File currently being analyzed:", file_relative_path
      metric_as_str_for_file = metric_as_str_for_file + uni_file_ + ","

      puppeteer_metrics_for_file = SmellDectector.getMetricsForFile(uni_file_)
      #print puppeteer_metrics_for_file
      metric_as_str_for_file = metric_as_str_for_file + puppeteer_metrics_for_file

      # Metric-1: Churn
      churnCmd="cd " + repo_abs_path  +" ; hg churn " + file_relative_path + awkMagic_churn
      churn_output = subprocess.check_output(['bash','-c', churnCmd])
      splitted_churn_output = churn_output.split(',')
      #print splitted_churn_output
      churn_for_file = getChurnFromStr(splitted_churn_output)
      #print "Churn:", churn_for_file
      metric_as_str_for_file = metric_as_str_for_file + str(churn_for_file) + ","

      # Metric -2 and 3: no of develoeprs involved
      developerCmd="cd " + repo_abs_path  +" ; hg churn " + file_relative_path + awkMagic_author
      developer_output = subprocess.check_output(['bash','-c', developerCmd])
      developer_churn_output = developer_output.split(',')
      developer_churn_output = [x_ for x_ in developer_churn_output if x_!='']
      ### active developer count is different from developer count: its non-unique
      '''
      # Metric -2: no of develoeprs involved .... gives erroneous results, will not be used
      act_dev_cnt = len(developer_churn_output)
      metric_as_str_for_file = metric_as_str_for_file + str(act_dev_cnt) + ","
      '''
      # Metric -3: no of unqiue develoeprs involved
      developer_churn_output = getUniqueDevelopers(developer_churn_output)
      #print "Developer list for file:", developer_churn_output
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



      # Metric -4: no of commmits involved, will not use as it is same as churn
      # allCommitMapping doesn't have full path fo file
      #commit_cnt = getRelevantCommitCount(file_relative_path, allCommitMapping)
      #print "Commit involvement count:", commit_cnt

      # Metric -5: timestamp   ::: attempted, but too little for a lot of effort, abadoning ....
      #timestamp = getListOfTimestamp(uni_file_, repo_abs_path)
      #print "Commit involvement count:", commit_cnt
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

      #print "FULL STR:", metric_as_str_for_file
      finalStr = finalStr + metric_as_str_for_file + "\n"
      print "-"*50


      #returnDirCommand= " cd /Users/akond/Documents/AkondOneDrive/OneDrive/Fall16-ThesisTopic/Puppeteer/"
      returnDirCommand= " cd ."
      ret_dir_output = subprocess.check_output(['bash','-c', returnDirCommand])
  return finalStr




def getFilesFromMappingInfo(mappingListParam):
  list_of_files = []
  for tuple_ in mappingListParam:
     file_in_tuple = tuple_[0]
     list_of_files.append(file_in_tuple)
  list_of_files = np.unique(list_of_files)
  return list_of_files




def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w')
  fileToWrite.write(strP )
  fileToWrite.close()
  return str(os.stat(fileP).st_size)
def getNoDefectsOnlyFiles(defected, mixed):
  defected_set = set(defected)
  mixed_set  = set(mixed)
  diff_set = mixed_set - defected_set
  non_defect_list = list(diff_set)
  return non_defect_list



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


def getBugMessages(bugMappingParam):
  list_ =[]
  bug_msg_=""
  for tup_ in bugMappingParam:
    bug_msg_ = tup_[-1]
    list_.append(bug_msg_)
  return list_




'''
Oct 19, 2016
This method grabs all the messages for both yes and no defected files
and dumps them ina aseperate file
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
def dumpRandBugMessageAsStr(unique_pupp_msg_papram, rand_msg_file_pupp_param, qual_coding_file_param, randRangeParam, msgCntParam, pupp_to_msgs_dict_param, msg_to_id_file_param, repo_path_param):
  indexCount=1
  ##rand_indices = [random.randint(1, msgCntParam) for x in xrange(randRangeParam)]
  rand_indices = random.sample(range(1, msgCntParam), randRangeParam)
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
          '''
          Added on Nov 07, 2016
          '''
          student_file_name = str(indexCount) + '_msg.txt'
          student_str =   elm + '\n' + '------------------------------' + '\n' + 'CATEGORY:' + '\n' + '------------------------------'
          student_folder_to_save = repo_path_param + '/' + 'student_rand' + '/'
          if not os.path.exists(student_folder_to_save):
             os.makedirs(student_folder_to_save)
          student_file_to_save   = student_folder_to_save + student_file_name
          dumpContentIntoFile(student_str, student_file_to_save)
          '''
          Ended
          '''
       indexCount = indexCount + 1

  dumpContentIntoFile(qual_mapping_str, qual_coding_file_param)
  '''
  added Oct 29, 2016
  '''
  dumpContentIntoFile(msg_to_id_mapping_str, msg_to_id_file_param)
  '''
  Added Nov 07, 2016
  '''
  # student_folder_to_save = repo_path_param + '/' + 'student' + '/'
  # if not os.path.exists(student_folder_to_save):
  #   os.makedirs(student_folder_to_save)
  # student_file_to_save   = student_folder_to_save + student_file_name
  # dumpContentIntoFile(student_str, student_file_to_save)




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



'''
Added Nov 01, 2016
'''
def dumpFullBugMessageAsStr(unique_pupp_msg_papram, all_msg_file_pupp_param, qual_coding_file_param, pupp_to_msgs_dict_param, msg_to_id_file_param, repo_path_param, id2msg_file_param, time2msgDictP):
  '''
  This method creates three files: one for bug messages, one for file mapping, one for qual. coding
  '''
  indexCount=1
  qual_mapping_str=""
  msg_to_id_mapping_str=""
  matchedFileName=""
  id2msg_mapping_str=""
  with open(all_msg_file_pupp_param, "a") as myfile_:
    for elm in unique_pupp_msg_papram:
          tmpStr = ""
          tmpStr = tmpStr + str(indexCount) + ',' + elm
          tmpStr = tmpStr + '\n' + '------------------------------' + '\n'
          myfile_.write(tmpStr)
          qual_mapping_str = qual_mapping_str + str(indexCount) + "," + "\n"
          if checkIfMsgInDict(elm, pupp_to_msgs_dict_param):
            matchedFileName =  getMatchingFileNameForMsg(elm, pupp_to_msgs_dict_param) # need the indexing to get the name of the list
            #timestamp
            matchedTimeStamp =  getMatchingTimeFromDict(elm, time2msgDictP)
            matchedTimeStamp =  str(matchedTimeStamp)
            msg_to_id_mapping_str = msg_to_id_mapping_str + str(indexCount) + ',' + matchedFileName + ',' + matchedTimeStamp + ',' + '\n'
            '''
            Dec 01, 2016
            '''
            elm = elm.replace('\n', ' ')
            elm = elm.replace(',', ';')
            id2msg_mapping_str = id2msg_mapping_str + str(indexCount) + ',' + repo_path_param + ',' + elm + ',' + matchedTimeStamp + ',' +  '\n'
          '''
          Added on Nov 07, 2016
          '''
          student_file_name = str(indexCount) + '_msg.txt'
          student_str =   elm + '\n' + '------------------------------' + '\n' + 'CATEGORY:' + '\n' + '------------------------------'
          student_folder_to_save = repo_path_param + '/' + 'student_full' + '/'
          if not os.path.exists(student_folder_to_save):
             os.makedirs(student_folder_to_save)
          student_file_to_save   = student_folder_to_save + student_file_name
          dumpContentIntoFile(student_str, student_file_to_save)
          '''
          Ended
          '''
          indexCount = indexCount + 1
  dumpContentIntoFile(msg_to_id_mapping_str, msg_to_id_file_param)
  dumpContentIntoFile(qual_mapping_str, qual_coding_file_param)
  dumpContentIntoFile(id2msg_mapping_str, id2msg_file_param)




'''
Added Dec 06, 2016
Start
'''
def dumpPhaseTwoBugMessageAsStr(unique_pupp_msg_papram, partial_content_file_param, pupp_to_msgs_dict_param, excludeIDListParam, repo_path_param):
  '''
  This method creates one file: file that contains qual. material
  '''
  indexCount=1
  partial_content_str=""
  for elm in unique_pupp_msg_papram:
          if (checkIfMsgInDict(elm, pupp_to_msgs_dict_param) and (indexCount not in excludeIDListParam)):
             elm = elm.replace('\n', ' ')
             elm = elm.replace(',', ';')
             matchedFileName =  getMatchingFileNameForMsg(elm, pupp_to_msgs_dict_param) # need the indexing to get the name of the list
             partial_content_str = partial_content_str + str(indexCount) + ',' + repo_path_param + ',' + elm + ',' + '\n'
          indexCount = indexCount + 1
  dumpContentIntoFile(partial_content_str, partial_content_file_param)
'''
End
'''

def getMatchingTimeFromDict(msgParam, dictToSearchParam):
    time2ret='0000-00-00'
    for k_, v_ in dictToSearchParam.items():
      if msgParam in v_:
          time2ret=k_
        #print "msg:{}, listOfMsgs:{}".format(msgParam, v_)
    return time2ret



'''
for timestamp
'''
def getPuppTimestamps(yesBugMappingParam, noBugMappingParam):
  dict2ret={}
  bug_msg_=""
  for tup_ in yesBugMappingParam:
    bug_msg_ = tup_[-1]
    '''
    get timestamp
    '''
    times_ = tup_[1]
    if times_ not in dict2ret:
        dict2ret[times_] = bug_msg_
  for tup_ in noBugMappingParam:
    bug_msg_ = tup_[-1]
    '''
    get timestamp
    '''
    times_ = tup_[1]
    if times_ not in dict2ret:
        dict2ret[times_] = bug_msg_
  return  dict2ret
