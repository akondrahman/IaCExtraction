'''
Answers to RQs
Akond: Feb 13, 2017
'''
import os, csv, xlrd, collections




notFoundMsg='NotFound'
WHAT_THE_FUCK='WTF'
def getMappedFile(id_Param, repo_Param):
    fileNameTiRet=notFoundMsg
    createDict={}
    #print "repo-name=>",repo_Param
    if repo_Param[-1]!='/':
        repo_Param = repo_Param + '/'
    file2read_=repo_Param+'fullThrottle_msg_file_map.csv'
    with open(file2read_, 'rU') as key_file:
      key_reader = csv.reader(key_file)
      for _row in key_reader:
        id_             = _row[0]
        fullFilePath_   = _row[1]
        createDict[id_]=fullFilePath_

    for k_, v_ in createDict.items():
        #print " 3: {}, 4:{}".format( k_, id_Param)
        if((k_==id_Param)):
          #print "paisi mamare"
          fileNameTiRet=createDict[k_]
    return fileNameTiRet



def getMappedTimestamp(id_Param, repo_Param):
    timestamp2ret='0000-00-00'
    createDict={}
    #print "repo-name=>",len(repo_Param)
    if repo_Param[-1]!='/':
        repo_Param = repo_Param + '/'
    file2read_=repo_Param+'fullThrottle_msg_ID_map.csv'
    if(os.path.isfile(file2read_)==False):
      file2read_=repo_Param+'fullThrottle_id_msg_map.csv'

    with open(file2read_, 'rU') as key_file:
      key_reader = csv.reader(key_file)
      for _row in key_reader:
        #print "lol->", _row
        id_             = _row[0]
        timestamp_      = _row[3]
        createDict[id_] = timestamp_
    for k_, v_ in createDict.items():
      if( (k_==id_Param)):
        #print "paisi mamare"
        timestamp2ret = timestamp_
    return timestamp2ret


def constructDataset(ParamFiles):
  for file_ in ParamFiles:
    #print"file:", file_
    with open(file_, 'rU') as categ_file:
      categ_reader = csv.reader(categ_file)
      next(categ_reader, None)
      for categ_row in categ_reader:
        id_of_message   = categ_row[0]
        repo_of_message = categ_row[1]
        the_message     = categ_row[2]
        categ_message   = categ_row[3]
        if((repo_of_message!=WHAT_THE_FUCK) and (len(repo_of_message)>0)):
          file_message    = getMappedFile(id_of_message, repo_of_message)
          time_message    = getMappedTimestamp(id_of_message, repo_of_message)
          print "ID:{}, repo:{}, message:{}, category:{}, file:{}, time:{}".format(id_of_message, repo_of_message, the_message,
                                                                                 categ_message,
                                                                                 file_message,
                                                                                 time_message)


file1='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Phase1_Final_Cat_Locked.csv'
file2='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Phase2_Final_Cat_Locked.csv'
listOfFiles=[file2]
constructDataset(listOfFiles)
