'''
Akond Rahman, Feb 18, 2017
Code for Puppet Lint
'''
import os , bug_git_util
tmp_log_holder = 'tmp.lint.log'
WARN='WARNING:'
ERROR='ERROR:'

def getLintMetrics(full_file_path_param_):
  str2ret=''
  errorCount = 0
  warnCount  = 0
  ## get lines of code for file
  SLOC_for_file  = sum(1 for line in open(full_file_path_param_))
  bug_git_util.performCleanUp(tmp_log_holder)
  # run puppet lint
  cmd = 'puppet-lint ' + full_file_path_param_ + ' > ' + tmp_log_holder
  os.system(cmd)
  print "A temp file for the lint log is created of {} bytes".format(os.stat(tmp_log_holder).st_size)
  print "-"*100
  # get values from the temp log
  with open(tmp_log_holder, 'rU') as myfile:
    linesInFile = myfile.readlines()
    for eachLine in linesInFile:
       if(WARN in eachLine):
         warnCount = warnCount + 1
       elif(ERROR in eachLine):
         errorCount = errorCount + 1
  warning_rate = float(warnCount)/float(SLOC_for_file)
  error_rate   = float(errorCount)/float(SLOC_for_file)
  warning_rate = round(warning_rate, 5)
  error_rate   = round(error_rate,   5)
  str2ret = str2ret + str(errorCount) + ',' + str(error_rate) + ',' + str(warnCount) + ',' + str (warning_rate) + ','
  return str2ret
