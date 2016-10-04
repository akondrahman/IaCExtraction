# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:30:41 2016

@author: akond
"""



from SmellDetector import SmellDectector
import os , subprocess, numpy as np 
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
    if elem !='':      
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
        msg2ret= msg2ret  + tuple_[-1]  + '|'
  return msg2ret

def getAllDevelopmentMetricList(uniqueFileList, repo_abs_path, allBugMapping, msgfile_, bugFlag=True): 
  headerStr1="Filename,max_nest_depth,class_dec,def_dec,pack_dec,file_dec,serv_dec,exec_dec,cohe_meth,body_txt_size,"
  headerStr2="lines_w_comm,lines_wo_comm,outerelems,file_reso,service_reso,package_reso,hard_coded_stmt,node_decl,parent_class,"
  headerStr3="d_class_dec,d_define_dec,d_pack_dec,d_file_dec,d_serv_dec,d_exec_dec,d_outerlem,d_hardcode,"  
  headerStr4="churn,NUdevCnt,UdevCnt,bugCnt,defectStatus"  
  headerStr = headerStr1 + headerStr2 + headerStr3 +  headerStr4 + "\n"
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
      # Metric -2: no of develoeprs involved  
      non_unique_developer_list = getNonUniqueDevelopers(developer_churn_output) 
      act_dev_cnt               = len(non_unique_developer_list)                  
      metric_as_str_for_file    = metric_as_str_for_file + str(act_dev_cnt) + "," 
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
      # Extra header to faculitatte preition models : Oct 03, 2016
      if (bugFlag):
        defectHeader = 'Y'
      else:
        defectHeader = 'N'   
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
