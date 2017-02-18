'''
Feb 18, 2017
Churn of files belonging to git repos
'''
import os, subprocess
def getRelativeChurnMetrics(param_file_path, repo_path):
  churn_added_lines = getAddedChurnMetrics(param_file_path, repo_path)


def getAddedChurnMetrics(param_file_path, repo_path):
   totalAddedLinesForChurn = 0

   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(param_file_path, repo_path)
   #print "full path: {}, repo path:{}, theFile:{}".format(param_file_path, repo_path, theFile)
   churnAddedCommand = "git log --numstat --oneline " + theFile + " |  awk '!(NR%2)' | awk '{ print $1 }' | sed -e  's/ /,/g'"
   command2Run = cdCommand + churnAddedCommand

   add_churn_output = subprocess.check_output(['bash','-c', command2Run])
   add_churn_output = add_churn_output.split('\n')
   add_churn_output = [x_ for x_ in add_churn_output if x_!='']
   add_churn_output = [int(y_) for y_ in add_churn_output if y_!='']
   print add_churn_output
   totalAddedLinesForChurn = sum(add_churn_output)
   print totalAddedLinesForChurn
   return totalAddedLinesForChurn
