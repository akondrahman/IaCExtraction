'''
Author: Akond Rahman
Date: Oct 03, 2016 
'''




import os 
def getPuppetFileCountForRepo(repoParam):
  contOfPupp = 0 
  contOfAll = 0   
  for root, subFolders, files in os.walk(repoParam):
    for file_ in files:
      contOfAll = contOfAll + 1    	
      file_name, file_extension = os.path.splitext(file_)   
      if file_extension=='.pp':
        contOfPupp = contOfPupp + 1 
  return contOfPupp, contOfAll 


def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)



def performSummaryForOrganizarion(orgParam):
  str2Write=""	
  allRepos = [x_ for x_ in os.listdir(orgParam)]       
  for repo_ in allRepos:
    path2explore=orgParam + repo_
    if os.path.isdir(path2explore):	
      print "The name of the repo is:", repo_  
      str2Write = str2Write + repo_ + ","
      pupp_cnt, allCount = getPuppetFileCountForRepo(path2explore) 
      pupp_ratio = float(pupp_cnt) / float(allCount)     
      print "The puppet-to-all-file ratio is:", pupp_ratio
      str2Write = str2Write + str(pupp_cnt) + ',' + str(allCount) + ',' + str(pupp_ratio) 
      str2Write = str2Write + '\n'  
      print "*"*50     
  summary_file_name= orgParam + 'summary_pp_cnt.csv'    
  status_quo = dumpContentIntoFile(str2Write, summary_file_name)
  print "Dumped a file of {} bytes".format(status_quo)


orgRepoDir='/Users/akond/PUPP_REPOS/wikimedia-downloads/'
performSummaryForOrganizarion(orgRepoDir)