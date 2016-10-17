from SmellDetector import AbsSmellDectector, ModSmellDectector, HieSmellDectector, DepSmellDectector, EncSmellDectector
from SmellDetector import Utilities
import os
import SourceModel.SM_File

def detectSmells(folder, outputFile):
    AbsSmellDectector.detectSmells(folder, outputFile)
    EncSmellDectector.detectSmells(folder, outputFile)
    ModSmellDectector.detectSmells(folder, outputFile)
    DepSmellDectector.detectSmells(folder, outputFile)
    HieSmellDectector.detectSmells(folder, outputFile)
    ### get Graph data
    graph_for_this_folder = ModSmellDectector.getGraph(folder)
    #graph_for_this_folder.printGraph()
    avg_degre = graph_for_this_folder.getAverageDegree()
    str_avg_degree =  "Average degree of {} graph={}".format(folder, avg_degre) + "\n"
    str_avg_degree =  str_avg_degree + "#######################" + "\n"
    node_count = graph_for_this_folder.getNodeCount()
    edge_count = graph_for_this_folder.getEdgeCount()
    graph_details_as_str = graph_for_this_folder.printGraph()
    nodes_edges_str = "Nodes in this graph:{}, edges in this graph:{}".format(node_count, edge_count) + "\n"
    nodes_edges_str = nodes_edges_str +  "#######################" + "\n"
    graph_file_to_save = folder + "/full_graph.txt"
    str_graph = graph_details_as_str + str_avg_degree + nodes_edges_str
    #print str_graph
    dump_status = Utilities.dumpStrToFile(graph_file_to_save, str_graph)
    print "Dumped a file of {} bytes".format(dump_status)


def extractFileMetrics(folderToLook):
  str2ret=""
  for root, dirs, files in os.walk(folderToLook):
    for file_ in files:
      metric_str_for_file=""
      if file_.endswith(".pp") and not os.path.islink(os.path.join(root, file_)):
        fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file_))
        metric_str_for_file = fileObj.fileName + ","
        # direct metrics

        # Metric-1
        max_nest_depth_for_file  = fileObj.getMaxNestingDepth()
        metric_str_for_file = metric_str_for_file + str(max_nest_depth_for_file) + ","

        # Metric-2
        no_class_dec_for_file    = fileObj.getNoOfClassDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_class_dec_for_file) + ","

        # Metric-3
        no_def_dec_for_file      = fileObj.getNoOfDefineDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_def_dec_for_file) + ","

        # Metric-4
        no_pack_dec_for_file     = fileObj.getNoOfPackageDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_pack_dec_for_file) + ","

        # Metric-5
        no_file_dec_for_file     = fileObj.getNoOfFileDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_file_dec_for_file) + ","

        # Metric-6
        no_serv_dec_for_file     = fileObj.getNoOfServiceDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_serv_dec_for_file) + ","

        # Metric-7
        no_exec_dec_for_file     = fileObj.getNoOfExecDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_exec_dec_for_file) + ","

        # Metric-8
        lack_cohe_meth_file      = fileObj.getLCOM()
        metric_str_for_file = metric_str_for_file + str(lack_cohe_meth_file) + ","

        # Metric-9
        body_txt_size_file       = fileObj.getBodyTextSize()[1] # tuple, first:loc, second: size
        metric_str_for_file = metric_str_for_file + str(body_txt_size_file) + ","

        # Metric-10
        no_lines_w_comm_file     = fileObj.getLinesOfCode()
        metric_str_for_file = metric_str_for_file + str(no_lines_w_comm_file) + ","

        # Metric-11
        no_lines_wo_comm_fil     = fileObj.getLinesOfCodeWithoutComments()
        metric_str_for_file = metric_str_for_file + str(no_lines_wo_comm_fil) + ","




        # indirect metrics
        # Metric-12
        no_outerelem_for_file = len(fileObj.getOuterElementList())
        metric_str_for_file = metric_str_for_file + str(no_outerelem_for_file) + ","

        # Metric-13
        no_file_res_for_file =  len(fileObj.getFileResourceList())
        metric_str_for_file = metric_str_for_file + str(no_file_res_for_file) + ","

        # Metric-14
        no_ser_res_for_file  =  len(fileObj.getServiceResourceList())
        metric_str_for_file = metric_str_for_file + str(no_ser_res_for_file) + ","

        # Metric-15
        no_package_res_for_file = len(fileObj.getPackageResourceList())
        metric_str_for_file = metric_str_for_file + str(no_package_res_for_file) + ","

        # Metric-16
        no_hard_coded_stmt  = len(fileObj.getHardCodedStatments())
        metric_str_for_file = metric_str_for_file + str(no_hard_coded_stmt) + ","

        # Metric-17
        no_node_dec_for_file = len(fileObj.getNodeDeclarations())
        metric_str_for_file = metric_str_for_file + str(no_node_dec_for_file) + ","

        # Metric-18
        no_parent_cls_for_file = len(fileObj.getClassHierarchyInfo()[1])
        metric_str_for_file = metric_str_for_file + str(no_parent_cls_for_file) + ","
        # second item in the tuple gives parent classes

        #print "file:{}, parent classes:{}".format(fileObj.fileName, str(lack_cohe_meth_file))
        str2ret = str2ret + metric_str_for_file + "\n"




  return str2ret



def getMetricsForFile(fully_qualaified_path_to_file):
        str2ret = ""
        metric_str_for_file=""
        fileObj = SourceModel.SM_File.SM_File(fully_qualaified_path_to_file)
        #metric_str_for_file = fileObj.fileName + ","
        # direct metrics

        # Metric-1
        max_nest_depth_for_file  = fileObj.getMaxNestingDepth()
        metric_str_for_file = metric_str_for_file + str(max_nest_depth_for_file) + ","
        max_nest_depth_for_file = 0

        # Metric-2
        no_class_dec_for_file    = fileObj.getNoOfClassDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_class_dec_for_file) + ","
        no_class_dec_for_file = 0
        # Metric-3
        no_def_dec_for_file      = fileObj.getNoOfDefineDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_def_dec_for_file) + ","
        no_def_dec_for_file = 0
        # Metric-4
        no_pack_dec_for_file     = fileObj.getNoOfPackageDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_pack_dec_for_file) + ","
        no_pack_dec_for_file = 0
        # Metric-5
        no_file_dec_for_file     = fileObj.getNoOfFileDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_file_dec_for_file) + ","
        no_file_dec_for_file = 0
        # Metric-6
        no_serv_dec_for_file     = fileObj.getNoOfServiceDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_serv_dec_for_file) + ","
        no_serv_dec_for_file = 0
        # Metric-7
        no_exec_dec_for_file     = fileObj.getNoOfExecDeclarations()
        metric_str_for_file = metric_str_for_file + str(no_exec_dec_for_file) + ","
        no_exec_dec_for_file = 0
        # Metric-8
        lack_cohe_meth_file      = fileObj.getLCOM()
        metric_str_for_file = metric_str_for_file + str(lack_cohe_meth_file) + ","
        lack_cohe_meth_file = 0
        # Metric-9
        body_txt_size_file       = fileObj.getBodyTextSize()[1] # tuple, first:loc, second: size
        metric_str_for_file = metric_str_for_file + str(body_txt_size_file) + ","
        body_txt_size_file = 0
        # Metric-10
        no_lines_w_comm_file     = fileObj.getLinesOfCode()
        metric_str_for_file = metric_str_for_file + str(no_lines_w_comm_file) + ","
        no_lines_w_comm_file = 0
        # Metric-11
        no_lines_wo_comm_fil     = fileObj.getLinesOfCodeWithoutComments()
        metric_str_for_file = metric_str_for_file + str(no_lines_wo_comm_fil) + ","
        no_lines_wo_comm_fil = 0



        # indirect metrics
        # Metric-12
        no_outerelem_for_file = len(fileObj.getOuterElementList())
        metric_str_for_file = metric_str_for_file + str(no_outerelem_for_file) + ","
        no_outerelem_for_file = 0

        # Metric-13
        no_file_res_for_file =  len(fileObj.getFileResourceList())
        metric_str_for_file = metric_str_for_file + str(no_file_res_for_file) + ","
        no_file_res_for_file = 0
        # Metric-14
        no_ser_res_for_file  =  len(fileObj.getServiceResourceList())
        metric_str_for_file = metric_str_for_file + str(no_ser_res_for_file) + ","
        no_ser_res_for_file = 0
        # Metric-15
        no_package_res_for_file = len(fileObj.getPackageResourceList())
        metric_str_for_file = metric_str_for_file + str(no_package_res_for_file) + ","
        no_package_res_for_file = 0
        # Metric-16
        no_hard_coded_stmt  = len(fileObj.getHardCodedStatments())
        metric_str_for_file = metric_str_for_file + str(no_hard_coded_stmt) + ","
        no_hard_coded_stmt = 0
        # Metric-17
        no_node_dec_for_file = len(fileObj.getNodeDeclarations())
        metric_str_for_file = metric_str_for_file + str(no_node_dec_for_file) + ","
        no_node_dec_for_file = 0
        # Metric-18
        no_parent_cls_for_file = len(fileObj.getClassHierarchyInfo()[1])
        metric_str_for_file = metric_str_for_file + str(no_parent_cls_for_file) + ","
        no_parent_cls_for_file = 0
        # second item in the tuple gives parent classes
        ##Added : Oct 03, 2016 ::: densit/ratio metrics
        '''
         to prevent division by zero , adding a small value (1) to  'no_lines_wo_comm_fil'
         assuming a file must have at least one line
        '''
        if (no_lines_wo_comm_fil==0):
          no_lines_wo_comm_fil = no_lines_wo_comm_fil + 1
        # Metric-19
        density_class_dec = float(no_class_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_class_dec) + ","
        density_class_dec = 0
        # Metric-20
        density_define_dec = float(no_def_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_define_dec) + ","
        density_define_dec = 0

        # Metric-21
        density_pack_dec = float(no_pack_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_pack_dec) + ","
        density_pack_dec = 0

        # Metric-22
        density_file_dec = float(no_file_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_file_dec) + ","
        density_file_dec = 0

        # Metric-23
        density_serv_dec = float(no_serv_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_serv_dec) + ","
        density_serv_dec = 0

        # Metric-24
        density_exec_dec = float(no_exec_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_exec_dec) + ","
        density_exec_dec = 0
        # Metric-25
        density_outerlem = float(no_outerelem_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_outerlem) + ","
        density_outerlem = 0
        # Metric-26
        density_hardcode = float(no_hard_coded_stmt)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_hardcode) + ","
        density_hardcode = 0


        #More metrics to go ... Oct 14, 2016
        #Metric-27
        count_of_includes = fileObj.getOnlyIncludeClassesCount()
        metric_str_for_file = metric_str_for_file + str(count_of_includes) + ","
        count_of_includes = 0
        #Metric-28
        count_of_git_usages = fileObj.getNoOfGitUsages()
        metric_str_for_file = metric_str_for_file + str(count_of_git_usages) + ","
        count_of_git_usages = 0
        #Metric-29
        count_of_requi = fileObj.getOnlyRequireCount()
        metric_str_for_file = metric_str_for_file + str(count_of_requi) + ","
        count_of_requi = 0
        #Metric-30
        count_of_notify = fileObj.getOnlyNotifyCount()
        metric_str_for_file = metric_str_for_file + str(count_of_notify) + ","
        count_of_notify = 0
        #Metric-31
        count_of_ensure = fileObj.getOnlyEnsureCount()
        metric_str_for_file = metric_str_for_file + str(count_of_ensure) + ","
        count_of_ensure = 0
        #Metric-32
        count_of_alias = fileObj.getOnlyAliasCount()
        metric_str_for_file = metric_str_for_file + str(count_of_alias) + ","
        count_of_alias = 0
        #Metric-33
        count_of_subsc = fileObj.getOnlySubscribeCount()
        metric_str_for_file = metric_str_for_file + str(count_of_subsc) + ","
        count_of_subsc = 0
        #Metric-34
        count_of_consume = fileObj.getOnlyConsumeCount()
        metric_str_for_file = metric_str_for_file + str(count_of_consume) + ","
        count_of_consume = 0
        #Metric-35
        count_of_export = fileObj.getOnlyExportCount()
        metric_str_for_file = metric_str_for_file + str(count_of_export) + ","
        count_of_export = 0

        #Metric-36
        count_of_sched = fileObj.getOnlyScheduleCount()
        metric_str_for_file = metric_str_for_file + str(count_of_sched) + ","
        count_of_sched = 0
        #Metric-37
        count_of_stage = fileObj.getOnlyStageCount()
        metric_str_for_file = metric_str_for_file + str(count_of_stage) + ","
        count_of_stage = 0
        #Metric-38
        count_of_tags = fileObj.getOnlyTagCount()
        metric_str_for_file = metric_str_for_file + str(count_of_tags) + ","
        count_of_tags = 0
        #Metric-39
        count_of_noop = fileObj.getOnlyNoopCount()
        metric_str_for_file = metric_str_for_file + str(count_of_noop) + ","
        count_of_noop = 0
        #Metric-40
        count_of_before = fileObj.getOnlyBeforeCount()
        metric_str_for_file = metric_str_for_file + str(count_of_before) + ","
        count_of_before = 0
        #Metric-41
        count_of_audit = fileObj.getOnlyAuditCount()
        metric_str_for_file = metric_str_for_file + str(count_of_audit) + ","
        count_of_audit = 0
        meta_param_total_cnt = ( count_of_requi + count_of_notify  + count_of_alias + count_of_subsc +
                                 count_of_consume +  count_of_export +  count_of_sched +  count_of_stage +  count_of_tags +
                                 count_of_noop +   count_of_before +  count_of_audit
                                )
        metric_str_for_file = metric_str_for_file + str(meta_param_total_cnt) + ","
        meta_param_total_cnt = 0
        #Metric-42
        count_of_inheri_usage = fileObj.getOnlyInheritanceUsageCount()
        metric_str_for_file = metric_str_for_file + str(count_of_inheri_usage) + ","
        count_of_inheri_usage = 0
        #Metric-43
        count_of_sql_usage = fileObj.getOnlySQLUsageCount()
        metric_str_for_file = metric_str_for_file + str(count_of_sql_usage) + ","
        count_of_sql_usage = 0
        #Metric-44
        non_pp_count = fileObj.getNonPuppetUsageCount()
        metric_str_for_file = metric_str_for_file + str(non_pp_count) + ","
        non_pp_count = 0
        #Metric-45
        mcx_count = fileObj.getMCXCount()
        metric_str_for_file = metric_str_for_file + str(mcx_count) + ","
        mcx_count = 0
        #Metric-46
        rsyslog_count = fileObj.getRSysLogCount()
        metric_str_for_file = metric_str_for_file + str(rsyslog_count) + ","
        rsyslog_count = 0
        #Metric-47
        valid_hash_count = fileObj.getValidateHashCount()
        metric_str_for_file = metric_str_for_file + str(valid_hash_count) + ","
        valid_hash_count = 0
        #Metric-48
        req_pack_count = fileObj.getRequirePackageCount()
        metric_str_for_file = metric_str_for_file + str(req_pack_count) + ","
        req_pack_count = 0
        #Metric-49
        hiera_incl_count = fileObj.getHieraIncludeCount()
        metric_str_for_file = metric_str_for_file + str(hiera_incl_count) + ","
        hiera_incl_count = 0
        #Metric-50
        incl_packs_count = fileObj.getIncludePacksCount()
        metric_str_for_file = metric_str_for_file + str(incl_packs_count) + ","
        incl_packs_count = 0
        #Metric-51
        ensure_packs_count = fileObj.getEnsurePacksCount()
        metric_str_for_file = metric_str_for_file + str(ensure_packs_count) + ","
        ensure_packs_count = 0
        #Metric-52
        if_count = fileObj.getIfElseCount()
        metric_str_for_file = metric_str_for_file + str(if_count) + ","
        if_count = 0
        #Metric-53
        undef_count = fileObj.getUndefCount()
        metric_str_for_file = metric_str_for_file + str(undef_count) + ","
        undef_count = 0

        clsParamStat  = fileObj.getClassParamCount()
        #Metric-54
        avg_param_cnt = clsParamStat[0]
        metric_str_for_file = metric_str_for_file + str(avg_param_cnt) + ","
        avg_param_cnt = 0
        #Metric-55
        medi_param_cnt = clsParamStat[1]
        metric_str_for_file = metric_str_for_file + str(medi_param_cnt) + ","
        medi_param_cnt = 0
        #Metric-56
        max_param_cnt = clsParamStat[2]
        metric_str_for_file = metric_str_for_file + str(max_param_cnt) + ","
        max_param_cnt = 0
        #Metric-57
        min_param_cnt = clsParamStat[3]
        metric_str_for_file = metric_str_for_file + str(min_param_cnt) + ","
        min_param_cnt = 0
        #Metric-58
        var_assign_cnt = fileObj.getVarAssiCount()
        metric_str_for_file = metric_str_for_file + str(var_assign_cnt) + ","
        var_assign_cnt = 0
        ### Oct 16, 2016
        #Metric-59
        case_stmt_cnt = fileObj.getCaseStmtCount()
        metric_str_for_file = metric_str_for_file + str(case_stmt_cnt) + ","
        case_stmt_cnt = 0
        #Metric-60
        env_cnt = fileObj.getEnvCount()
        metric_str_for_file = metric_str_for_file + str(env_cnt) + ","
        env_cnt = 0
        #Metric-61
        crone_cnt = fileObj.getCronCount()
        metric_str_for_file = metric_str_for_file + str(crone_cnt) + ","
        crone_cnt = 0
        #Metric-62
        ## count of  '=>' 's
        reff_cnt = fileObj.getReffCount()
        metric_str_for_file = metric_str_for_file + str(reff_cnt) + ","
        reff_cnt = 0
        ### Oct 17, 2016
        #Metric-63 : summation
        total_reso_cnt_per_file = no_exec_dec_for_file + no_file_dec_for_file + no_pack_dec_for_file + no_serv_dec_for_file
        metric_str_for_file = metric_str_for_file + str(total_reso_cnt_per_file) + ","
        total_reso_cnt_per_file = 0
        
        str2ret = str2ret + metric_str_for_file
        return str2ret





def hogarbal():
  fileObj = SourceModel.SM_File.SM_File('paikhana4.pp')
  cnt_includes = fileObj.getOnlyIncludeClassesCount()
  count_of_git_usages = fileObj.getNoOfGitUsages()
  print "Git count:", count_of_git_usages
  count_of_requires = fileObj.getOnlyRequireCount()
  count_of_notifies = fileObj.getOnlyNotifyCount()
  count_of_ensures  = fileObj.getOnlyEnsureCount()
  count_of_aliases  = fileObj.getOnlyAliasCount()
  count_of_subscri  = fileObj.getOnlySubscribeCount()
  count_of_consume  = fileObj.getOnlyConsumeCount()
  count_of_export   = fileObj.getOnlyExportCount()
  count_of_schedu   = fileObj.getOnlyScheduleCount()
  count_of_stages   = fileObj.getOnlyStageCount()
  count_of_tags     = fileObj.getOnlyTagCount()
  count_of_noop     = fileObj.getOnlyNoopCount()
  count_of_before   = fileObj.getOnlyBeforeCount()
  count_of_audit    = fileObj.getOnlyAuditCount()


  #count_of_inher    = fileObj.getOnlyInheritanceUsageCount()
  #count_of_sql_ref    = fileObj.getOnlySQLUsageCount()
  #non_pp_count = fileObj.getNonPuppetUsageCount()
  #mcx_cnt = fileObj.getMCXCount()
  #rsysLogCnt = fileObj.getRSysLogCount()
  #vHashCnt   = fileObj.getValidateHashCount()
  reqPackCnt   = fileObj.getRequirePackageCount()
  hierInclCnt  = fileObj.getHieraIncludeCount()
  ensPackCnt   = fileObj.getEnsurePacksCount()
  #clsParamCnt  = fileObj.getClassParamCount()
  #inclPacklCnt  = fileObj.getIncludePacksCount()
  ifelseCnt    = fileObj.getIfElseCount()
  undefCnt     = fileObj.getUndefCount()
  print "req Package Cnt: ", reqPackCnt
  print "hiear include cnt:", hierInclCnt
  print "ensure packs cnt: ", ensPackCnt
  #print "if else cnt:", ifelseCnt
  #print "undef cnt:", undefCnt
  clsParamStat  = fileObj.getClassParamCount()
  print "Param count stats:", clsParamStat
  var_assi_cnt =  fileObj.getVarAssiCount()
  print "Var assignment cnt:", var_assi_cnt




  reff_cnt =  fileObj.getReffCount()
  print "=> cnt:", reff_cnt
