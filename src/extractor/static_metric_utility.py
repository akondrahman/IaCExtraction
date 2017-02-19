'''
Feb 18, 2017
Akond Rahman
utility stuff for metric extraction code
'''
import os, csv, numpy as np
theCompleteCategFile='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/New.Categ.csv'


def getPuppetFileDetails():
    dictOfAllFiles={}
    dict2Ret={}
    with open(theCompleteCategFile, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
        repo_of_file       = row_[1]
        categ_of_file      = row_[3]
        full_path_of_file  = row_[4]
        if full_path_of_file not in dictOfAllFiles:
            dictOfAllFiles[full_path_of_file] = [[ categ_of_file ], repo_of_file]
        else:
            dictOfAllFiles[full_path_of_file][0] = dictOfAllFiles[full_path_of_file][0] + [ categ_of_file ]
    for k_, v_ in dictOfAllFiles.items():
       uniq = np.unique(v_[0])
       if ((len(uniq)==1) and (uniq[0]=='N')):
         dict2Ret[k_] = ('0', v_[1])
       else:
         dict2Ret[k_] = ('0', v_[1])
    return dict2Ret
