'''
Feb 18, 2017
Akond Rahman
utility stuff for metric extraction code
'''
import os, csv
theCompleteCategFile=''


def getPuppetFileDetails():
    dictOfAllFiles={}
    dict2Ret={}
    with open(theCompleteCategFile, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
        categ_of_file      = row_[3]
        full_path_of_file  = row_[4]
        if full_path_of_file not in dictOfAllFiles:
            dictOfAllFiles[full_path_of_file] = [ categ_of_file ]
        else:
            dictOfAllFiles[full_path_of_file] = dictOfAllFiles[full_path_of_file] + [ categ_of_file ]
    for k_, v_ in dictOfAllFiles.items():
       if ((len(v_)==1) and (v_[0]=='N')):
         dict2Ret[k_] = '0'
       else:
         dict2Ret[k_] = '1'
    return dictOfAllFiles
