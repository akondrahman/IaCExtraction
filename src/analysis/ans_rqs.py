'''
Answers to RQs
Akond: Feb 13, 2017
'''
import os, csv, xlrd, collections




notFoundMsg='NotFound'
WHAT_THE_FUCK='WTF'
THE_SPACE=' '


def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)





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



def constructDataset(ParamFiles, output_file_param):
  str2dump=''
  for file_ in ParamFiles:
    print "="*100  
    print"Started processing:", file_
    with open(file_, 'rU') as categ_file:
      categ_reader = csv.reader(categ_file)
      next(categ_reader, None)
      for categ_row in categ_reader:
        id_of_message   = categ_row[0]
        repo_of_message = categ_row[1]
        the_message     = categ_row[2]
        the_message     = the_message.replace('\n', ' ')
        the_message     = the_message.replace(',', ';')
        categ_message   = categ_row[3]
        if((repo_of_message!=WHAT_THE_FUCK) and (len(repo_of_message)>0)):
          file_message    = getMappedFile(id_of_message, repo_of_message)
          size_file       = os.stat(file_message).st_size
          lines_for_file  = sum(1 for line in open(file_message))
          time_message    = getMappedTimestamp(id_of_message, repo_of_message).split(THE_SPACE)[0]
        #   print "ID:{}, repo:{}, message:{}, category:{}, file:{}, time:{}, size:{}, lines:{}".format(id_of_message, repo_of_message,
        #                                                                                               the_message,   categ_message,
        #                                                                                               file_message,  time_message,
        #                                                                                               size_file,     lines_for_file)

          str2dump = str2dump + id_of_message + ',' + repo_of_message + ',' + the_message + ',' + categ_message + ',' + file_message + ',' + time_message + ',' + str(size_file) + ',' + str(lines_for_file) + ',' + '\n'
  stat_ = dumpContentIntoFile(str2dump, output_file_param)
  print "Dumped a file of {} bytes".format(stat_)



file1='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Phase1_Final_Cat_Locked.csv'
file2='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Phase2_Final_Cat_Locked.csv'
listOfFiles=[file1, file2]
outputFileForDB='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Categ_For_DB.csv'
constructDataset(listOfFiles, outputFileForDB)
