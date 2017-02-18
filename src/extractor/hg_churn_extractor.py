'''
Akond Feb 18, 2017
hg churn metrics
'''
import os, subprocess, numpy as np
def getRelativeChurnMetrics(param_file_path, repo_path):
  churn_str_for_file= ""

  churn_added_lines = getAddedChurnMetrics(param_file_path, repo_path)
  churn_delet_lines = getDeletedChurnMetrics(param_file_path, repo_path)
  churn_total_lines = churn_added_lines + churn_delet_lines
  #print "Churn:add={}, churn:del={}, churn:total={}".format(churn_added_lines, churn_delet_lines, churn_total_lines)
  lines_for_file      = sum(1 for line in open(param_file_path))
  churn_total_days    = getDaysOfChurn(param_file_path, repo_path)



def getAddedChurnMetrics(param_file_path, repo_path):
   totalAddedLinesForChurn = 0

   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(param_file_path, repo_path)
   #print "full path: {}, repo path:{}, theFile:{}".format(param_file_path, repo_path, theFile)
   churnAddedCommand = "hg churn --diffstat " + theFile + " | awk '{print $2}' | cut -d'/' -f1 | cut -d'+' -f2 | sed -e  's/ /,/g'"
   command2Run = cdCommand + churnAddedCommand

   add_churn_output = subprocess.check_output(['bash','-c', command2Run])
   add_churn_output = add_churn_output.split('\n')
   add_churn_output = [x_ for x_ in add_churn_output if x_!='']
   add_churn_output = [int(y_) for y_ in add_churn_output ]
   #print add_churn_output
   totalAddedLinesForChurn = sum(add_churn_output)
   #print totalAddedLinesForChurn
   return totalAddedLinesForChurn



def getDeletedChurnMetrics(param_file_path, repo_path):
   totalAddedLinesForChurn = 0

   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(param_file_path, repo_path)
   #print "full path: {}, repo path:{}, theFile:{}".format(param_file_path, repo_path, theFile)
   churnAddedCommand = "hg churn --diffstat " + theFile + " | awk '{print $2}' | cut -d'/' -f2 | cut -d'-' -f2 | sed -e  's/ /,/g'"
   command2Run = cdCommand + churnAddedCommand

   add_churn_output = subprocess.check_output(['bash','-c', command2Run])
   add_churn_output = add_churn_output.split('\n')
   add_churn_output = [x_ for x_ in add_churn_output if x_!='']
   add_churn_output = [int(y_) for y_ in add_churn_output ]
   #print add_churn_output
   totalAddedLinesForChurn = sum(add_churn_output)
   #print totalAddedLinesForChurn
   return totalAddedLinesForChurn
def getDaysOfChurn(param_file_path, repo_path):
   totalDaysForChurn = 0

   cdCommand            = "cd " + repo_path + " ; "
   theFile              = os.path.relpath(param_file_path, repo_path)
   churnDateTimeCommand = " hg churn --dateformat '%Y-%m-%d' " + theFile + " | awk '{ print $1 }' | sed -e 's/ /,/g'"
   command2Run          = cdCommand + churnDateTimeCommand

   dt_churn_output = subprocess.check_output(['bash','-c', command2Run])
   dt_churn_output = dt_churn_output.split('\n')
   dt_churn_output = [x_ for x_ in dt_churn_output if x_!='']
   dt_churn_output = np.unique(dt_churn_output)
   #print dt_churn_output
   totalDaysForChurn = len(dt_churn_output)
   #print totalDaysForChurn
   return totalDaysForChurn
