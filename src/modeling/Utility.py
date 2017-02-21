# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:53:19 2016

@author: akond
"""



import math, os
import numpy as np
def getDatasetFromCSV(fileParam, dataTypeFlag=True):
  if dataTypeFlag:
    data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1, dtype='float')
  else:
        data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1,  dtype='str')
  return data_set_to_return



def assignNumericLabels(labelListParam):
  y_cnt = 0
  n_cnt = 0
  label_list = []
  for label_ in labelListParam:
   if label_=='Y':
     label_list.append(1)
     y_cnt = y_cnt + 1
   else:
     label_list.append(0)
     n_cnt = n_cnt + 1
  print "before: {}, after:{}, yes:{}, no:{}".format(len(labelListParam), len(label_list), y_cnt, n_cnt)
  return label_list


def createSelectedFeatures(allFeatureParam, selectedIndicies):
  feature_dataset_to_ret = []
  for ind_ in selectedIndicies:
    features_for_this_index = allFeatureParam[:, ind_]
    feature_dataset_to_ret.append(features_for_this_index)
  ## convert to numpy  array
  feature_dataset_to_ret = np.array(feature_dataset_to_ret)
  ## transpose array
  feature_dataset_to_ret = feature_dataset_to_ret.transpose()

  return feature_dataset_to_ret




def giveTimeStamp():
  import time, datetime
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret
def printFeatureName(indicesParam, steroidFlag=False):
#  headers=['max_nest_depth','class_dec','def_dec','pack_dec',
#           'file_dec','serv_dec','exec_dec','cohe_meth','body_txt_size',
#           'lines_w_comm','lines_wo_comm','outerelems','file_reso','service_reso',
#           'package_reso','hard_coded_stmt','node_decl','parent_class','d_class_dec',
#           'd_define_dec','d_pack_dec','d_file_dec','d_serv_dec','d_exec_dec',
#           'd_outerlem','d_hardcode','churn','NUdevCnt','UdevCnt']
  headers=['max_nest_depth','class_dec','def_dec','pack_dec',
           'file_dec','serv_dec','exec_dec','cohe_meth','body_txt_size',
           'lines_w_comm','lines_wo_comm','outerelems','file_reso','service_reso',
           'package_reso','hard_coded_stmt','node_decl','parent_class','d_class_dec',
           'd_define_dec','d_pack_dec','d_file_dec','d_serv_dec','d_exec_dec',
           'd_outerlem','d_hardcode','churn','UdevCnt']
  if steroidFlag:
     headers=[ 'max_nest_depth','class_dec','def_dec','pack_dec','file_dec','serv_dec','exec_dec',
               'cohe_meth','body_txt_size','lines_w_comm','lines_wo_comm','outerelems','file_reso','service_reso',
               'package_reso','hard_coded_stmt','node_decl','parent_class',
               'd_class_dec','d_define_dec','d_pack_dec','d_file_dec','d_serv_dec','d_exec_dec','d_outerlem','d_hardcode',
               'cnt_include','cnt_git',
               'cnt_req','cnt_noti','cnt_ensur','cnt_alias','cnt_subsc','cnt_consum','cnt_export','cnt_sched','cnt_of_stage','cnt_tag','cnt_noop','cnt_before','cnt_audit',
               'meta_param_total_cnt','cnt_inheri','cnt_sql','non_pp_cnt','mcx_cnt','rsyslog_cnt','validhash_cnt','reqpack_cnt','hieraincl_cnt','inclpacks_cnt',
               'ensurepacks_cnt','if_cnt','undef_cnt','avgparam_cnt','mediparam_cnt','maxparam_cnt','min_param_cnt','var_assi_cnt',
               'churn','UdevCnt']
  #print "Total features:", len(headers)   ## for sanity check, checked: everythign OK
  featureNameToRet=[]
  for selIndex in indicesParam:
    featureNameToRet.append(headers[selIndex])
  return featureNameToRet



def createLogTransformedSelectedFeatures(allFeatureParam, selectedIndicies):
  #exp_coeff = 2.71828182846
  log_transformed_feature_dataset_to_ret = []
  for ind_ in selectedIndicies:
    features_for_this_index = allFeatureParam[:, ind_]
    ## do the log tranform on the extracted index
    ## the following code gives error for 0 values , so using the other
    ####log_transformed_features_for_index = [math.log(x_, exp_coeff) for x_ in features_for_this_index]
    ## the following code handles the issue for zero values
    log_transformed_features_for_index = [math.log1p(x_) for x_ in features_for_this_index]
    log_transformed_feature_dataset_to_ret.append(log_transformed_features_for_index)
  ## convert to numpy  array
  log_transformed_feature_dataset_to_ret = np.array(log_transformed_feature_dataset_to_ret)
  ## transpose array
  log_transformed_feature_dataset_to_ret = log_transformed_feature_dataset_to_ret.transpose()

  return log_transformed_feature_dataset_to_ret

def printNinetyMetricFeatureName(indicesParam):
     headers=['max_nest_depth','class_dec','def_dec','pack_dec','file_dec','serv_dec','exec_dec',
     'cohe_meth','body_txt_size',
     'lines_w_comm','lines_wo_comm','outerelems','file_reso','service_reso','package_reso','hard_coded_stmt','node_decl',
     'parent_class','d_class_dec','d_define_dec','d_pack_dec','d_file_dec','d_serv_dec','d_exec_dec','d_outerlem',
     'd_hardcode','cnt_include','cnt_git','cnt_req','cnt_noti','cnt_ensur','cnt_alias','cnt_subsc','cnt_consum','cnt_export',
     'cnt_sched','cnt_of_stage','cnt_tag','cnt_noop','cnt_before','cnt_audit','meta_param_total_cnt','cnt_inheri','cnt_sql','non_pp_cnt',
     'mcx_cnt','rsyslog_cnt','validhash_cnt','reqpack_cnt','hieraincl_cnt','inclpacks_cnt','ensurepacks_cnt','if_cnt','undef_cnt','avgparam_cnt',
     'mediparam_cnt','maxparam_cnt','min_param_cnt','var_assi_cnt','case_stmt_cnt','env_cnt','crone_cnt','reff_cnt','total_reso_cnt_per_file',
     'total_reso_cnt_per_blocks','total_reso_cnt_per_lines','svc_cnt_per_blocks','inc_per_svc_cnt','inc_per_pkg_cnt','inc_per_file_cnt',
     'inc_per_tot_reso_cnt',
     'inc_per_line','cron_per_line','if_cnt_per_block','incl_cnt_per_block','req_pack_cnt_per_block','pack_decl_cnt_per_block',
     'req_pack_cnt_per_lines',
     'require_per_lines','var_per_lines','var_to_reffs','reffs_per_block','reff_cnt_per_lines',
     'reff_cnt2total_reso','reff_cnt2req_pack','reff_cnt2incl_cnt','churn','UdevCnt']
     ##print "Total count of features :", len(headers)
     ###### for sanity check, checked: everything OK
     featureNameToRet=[]
     for selIndex in indicesParam:
       featureNameToRet.append(headers[selIndex])
     return featureNameToRet




def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)
