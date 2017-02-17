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

        # Metric-20
        density_define_dec = float(no_def_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_define_dec) + ","


        # Metric-21
        density_pack_dec = float(no_pack_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_pack_dec) + ","


        # Metric-22
        density_file_dec = float(no_file_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_file_dec) + ","


        # Metric-23
        density_serv_dec = float(no_serv_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_serv_dec) + ","


        # Metric-24
        density_exec_dec = float(no_exec_dec_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_exec_dec) + ","

        # Metric-25
        density_outerlem = float(no_outerelem_for_file)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_outerlem) + ","

        # Metric-26
        density_hardcode = float(no_hard_coded_stmt)/float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(density_hardcode) + ","


        '''
        #More metrics to go ... Oct 14, 2016
        '''
        #Metric-27
        count_of_includes = fileObj.getOnlyIncludeClassesCount()
        metric_str_for_file = metric_str_for_file + str(count_of_includes) + ","

        #Metric-28
        count_of_git_usages = fileObj.getNoOfGitUsages()
        metric_str_for_file = metric_str_for_file + str(count_of_git_usages) + ","

        #Metric-29
        count_of_requi = fileObj.getOnlyRequireCount()
        metric_str_for_file = metric_str_for_file + str(count_of_requi) + ","

        #Metric-30
        count_of_notify = fileObj.getOnlyNotifyCount()
        metric_str_for_file = metric_str_for_file + str(count_of_notify) + ","

        #Metric-31
        count_of_ensure = fileObj.getOnlyEnsureCount()
        metric_str_for_file = metric_str_for_file + str(count_of_ensure) + ","

        #Metric-32
        count_of_alias = fileObj.getOnlyAliasCount()
        metric_str_for_file = metric_str_for_file + str(count_of_alias) + ","

        #Metric-33
        count_of_subsc = fileObj.getOnlySubscribeCount()
        metric_str_for_file = metric_str_for_file + str(count_of_subsc) + ","

        #Metric-34
        count_of_consume = fileObj.getOnlyConsumeCount()
        metric_str_for_file = metric_str_for_file + str(count_of_consume) + ","

        #Metric-35
        count_of_export = fileObj.getOnlyExportCount()
        metric_str_for_file = metric_str_for_file + str(count_of_export) + ","


        #Metric-36
        count_of_sched = fileObj.getOnlyScheduleCount()
        metric_str_for_file = metric_str_for_file + str(count_of_sched) + ","

        #Metric-37
        count_of_stage = fileObj.getOnlyStageCount()
        metric_str_for_file = metric_str_for_file + str(count_of_stage) + ","

        #Metric-38
        count_of_tags = fileObj.getOnlyTagCount()
        metric_str_for_file = metric_str_for_file + str(count_of_tags) + ","

        #Metric-39
        count_of_noop = fileObj.getOnlyNoopCount()
        metric_str_for_file = metric_str_for_file + str(count_of_noop) + ","

        #Metric-40
        count_of_before = fileObj.getOnlyBeforeCount()
        metric_str_for_file = metric_str_for_file + str(count_of_before) + ","

        #Metric-41
        count_of_audit = fileObj.getOnlyAuditCount()
        metric_str_for_file = metric_str_for_file + str(count_of_audit) + ","

        meta_param_total_cnt = ( count_of_requi + count_of_notify  + count_of_alias + count_of_subsc +
                                 count_of_consume +  count_of_export +  count_of_sched +  count_of_stage +  count_of_tags +
                                 count_of_noop +   count_of_before +  count_of_audit
                                )
        metric_str_for_file = metric_str_for_file + str(meta_param_total_cnt) + ","

        #Metric-42
        count_of_inheri_usage = fileObj.getOnlyInheritanceUsageCount()
        metric_str_for_file = metric_str_for_file + str(count_of_inheri_usage) + ","

        #Metric-43
        count_of_sql_usage = fileObj.getOnlySQLUsageCount()
        metric_str_for_file = metric_str_for_file + str(count_of_sql_usage) + ","

        #Metric-44
        non_pp_count = fileObj.getNonPuppetUsageCount()
        metric_str_for_file = metric_str_for_file + str(non_pp_count) + ","

        #Metric-45
        mcx_count = fileObj.getMCXCount()
        metric_str_for_file = metric_str_for_file + str(mcx_count) + ","

        #Metric-46
        rsyslog_count = fileObj.getRSysLogCount()
        metric_str_for_file = metric_str_for_file + str(rsyslog_count) + ","

        #Metric-47
        valid_hash_count = fileObj.getValidateHashCount()
        metric_str_for_file = metric_str_for_file + str(valid_hash_count) + ","

        #Metric-48
        req_pack_count = fileObj.getRequirePackageCount()
        metric_str_for_file = metric_str_for_file + str(req_pack_count) + ","

        #Metric-49
        hiera_incl_count = fileObj.getHieraIncludeCount()
        metric_str_for_file = metric_str_for_file + str(hiera_incl_count) + ","

        #Metric-50
        incl_packs_count = fileObj.getIncludePacksCount()
        metric_str_for_file = metric_str_for_file + str(incl_packs_count) + ","

        #Metric-51
        ensure_packs_count = fileObj.getEnsurePacksCount()
        metric_str_for_file = metric_str_for_file + str(ensure_packs_count) + ","

        #Metric-52
        if_count = fileObj.getIfElseCount()
        metric_str_for_file = metric_str_for_file + str(if_count) + ","

        #Metric-53
        undef_count = fileObj.getUndefCount()
        metric_str_for_file = metric_str_for_file + str(undef_count) + ","


        clsParamStat  = fileObj.getClassParamCount()
        #Metric-54
        avg_param_cnt = clsParamStat[0]
        metric_str_for_file = metric_str_for_file + str(avg_param_cnt) + ","

        #Metric-55
        medi_param_cnt = clsParamStat[1]
        metric_str_for_file = metric_str_for_file + str(medi_param_cnt) + ","

        #Metric-56
        max_param_cnt = clsParamStat[2]
        metric_str_for_file = metric_str_for_file + str(max_param_cnt) + ","

        #Metric-57
        min_param_cnt = clsParamStat[3]
        metric_str_for_file = metric_str_for_file + str(min_param_cnt) + ","

        #Metric-58
        var_assign_cnt = fileObj.getVarAssiCount()
        metric_str_for_file = metric_str_for_file + str(var_assign_cnt) + ","
        '''
        ### Oct 16, 2016
        '''
        #Metric-59
        case_stmt_cnt = fileObj.getCaseStmtCount()
        metric_str_for_file = metric_str_for_file + str(case_stmt_cnt) + ","

        #Metric-60
        env_cnt = fileObj.getEnvCount()
        metric_str_for_file = metric_str_for_file + str(env_cnt) + ","
        #print "Env count:", env_cnt
        #Metric-61
        crone_cnt = fileObj.getCronCount()
        metric_str_for_file = metric_str_for_file + str(crone_cnt) + ","

        #Metric-62
        ## count of  '=>' 's
        reff_cnt = fileObj.getReffCount()
        metric_str_for_file = metric_str_for_file + str(reff_cnt) + ","

        '''
        ### Oct 17, 2016
        '''
        #Metric-63 : summation of resources,
        #cron is also a resource : reff: https://docs.puppet.com/puppet/latest/reference/type.html#about-resource-types
        total_reso_cnt_per_file = no_exec_dec_for_file + no_file_dec_for_file + no_pack_dec_for_file + no_serv_dec_for_file + crone_cnt
        metric_str_for_file = metric_str_for_file + str(total_reso_cnt_per_file) + ","


        #Metric-64 : summation of resources : ratio : per block
        cnt_blocks = no_class_dec_for_file + no_def_dec_for_file
        if cnt_blocks==0:
           cnt_blocks = cnt_blocks + 1
        total_reso_cnt_per_blocks = float(total_reso_cnt_per_file) / float(cnt_blocks)
        metric_str_for_file = metric_str_for_file + str(total_reso_cnt_per_blocks) + ","
        #print "resource per block:{}, count of block:{}, resource per file:{}".format(total_reso_cnt_per_blocks, cnt_blocks, total_reso_cnt_per_file)

        #Metric-65 : summation of resources : ratio : per lines withour comment

        total_reso_cnt_per_lines = float(total_reso_cnt_per_file) / float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(total_reso_cnt_per_lines) + ","
        #print "resource perlines:{},lines:{},resource:{}".format(total_reso_cnt_per_lines, no_lines_wo_comm_fil, total_reso_cnt_per_file)

        #Metric-66: count of services : ratio : per block
        svc_cnt_per_blocks = float(no_serv_dec_for_file) / float(cnt_blocks)
        metric_str_for_file = metric_str_for_file + str(svc_cnt_per_blocks) + ","
        #print "service per blocks:{},service:{}, blocks:{}".format(svc_cnt_per_blocks, no_serv_dec_for_file, cnt_blocks)

        #Metric-67: count of includes : ratio : per service
        if no_serv_dec_for_file==0:
           no_serv_dec_for_file = no_serv_dec_for_file + 0.50
        inc_per_svc_cnt = float(count_of_includes) / float(no_serv_dec_for_file)
        metric_str_for_file = metric_str_for_file + str(inc_per_svc_cnt) + ","
        #print "inc. per svc.:{},include:{}, service:{}".format(inc_per_svc_cnt, count_of_includes, no_serv_dec_for_file)

        #Metric-68: count of includes : ratio : per package
        if no_pack_dec_for_file==0:
           no_pack_dec_for_file = float(no_pack_dec_for_file) + 0.50
        inc_per_pkg_cnt = float(count_of_includes) / float(no_pack_dec_for_file)
        metric_str_for_file = metric_str_for_file + str(inc_per_pkg_cnt) + ","
        #print "inc. per pkg.:{},include:{}, package:{}".format(inc_per_pkg_cnt, count_of_includes, no_pack_dec_for_file)



        #Metric-69: count of includes : ratio : per file
        if no_file_dec_for_file==0:
           no_file_dec_for_file = float(no_file_dec_for_file) + 0.50
        inc_per_file_cnt = float(count_of_includes) / float(no_file_dec_for_file)
        metric_str_for_file = metric_str_for_file + str(inc_per_file_cnt) + ","
        #print "inc. per file.:{},include:{}, file:{}".format(inc_per_file_cnt, count_of_includes, no_file_dec_for_file)

        #Metric-70: count of includes : ratio : per resource
        if total_reso_cnt_per_file==0:
           total_reso_cnt_per_file = float(total_reso_cnt_per_file) + 0.50
        inc_per_tot_reso_cnt = float(count_of_includes) / float(total_reso_cnt_per_file)
        metric_str_for_file = metric_str_for_file + str(inc_per_tot_reso_cnt) + ","
        #print "inc. per total resource:{},include:{}, reso:{}".format(inc_per_tot_reso_cnt, count_of_includes, total_reso_cnt_per_file)

        #Metric-71: count of includes : ratio : per line
        inc_per_line = float(count_of_includes) / float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(inc_per_line) + ","
        #print "inc. per lines:{},include:{}, lines:{}".format(inc_per_line, count_of_includes, no_lines_wo_comm_fil)

        #Metric-72: count of crons : ratio : per line
        cron_per_line = float(crone_cnt) / float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(cron_per_line) + ","
        #print "cron per lines.:{},cron:{}, line:{}".format(cron_per_line, crone_cnt, no_lines_wo_comm_fil)

        #Metric-73: count of if statements : ratio : per blocks
        if_cnt_per_block = float(if_count) / float(cnt_blocks)
        metric_str_for_file = metric_str_for_file + str(if_cnt_per_block) + ","
        #print "if-count per blocks:{},if-count:{}, block:{}".format(if_cnt_per_block, if_count, cnt_blocks)

        #Metric-74: count of include declarations : ratio : per blocks
        incl_cnt_per_block = float(count_of_includes) / float(cnt_blocks)
        metric_str_for_file = metric_str_for_file + str(incl_cnt_per_block) + ","
        #print "include-count per blocks:{},include-count:{}, block:{}".format(incl_cnt_per_block, count_of_includes, cnt_blocks)

        #Metric-75: count of req_packs declarations : ratio : per blocks
        req_pack_cnt_per_block = float(req_pack_count) / float(cnt_blocks)
        metric_str_for_file = metric_str_for_file + str(req_pack_cnt_per_block) + ","
        #print "req_pack-count per blocks:{},req_pack-count:{}, block:{}".format(req_pack_cnt_per_block, req_pack_count, cnt_blocks)

        #Metric-76: count of package declarations : ratio : per blocks
        pack_decl_cnt_per_block = float(no_pack_dec_for_file) / float(cnt_blocks)
        metric_str_for_file = metric_str_for_file + str(pack_decl_cnt_per_block) + ","
        #print "pack. decl. count per blocks:{}, pack. decl. count{}, block:{}".format(pack_decl_cnt_per_block, no_pack_dec_for_file, cnt_blocks)

        '''
           count_of_requi refers to 'require =>'
           req_pack_count refers to 'require_package()'
        '''
        #Metric-77: count of req_packs  : ratio : per lines
        req_pack_cnt_per_lines = float(req_pack_count) / float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(req_pack_cnt_per_lines) + ","
        #print "req_pack-count per lines:{},req_pack-count:{}, lines:{}".format(req_pack_cnt_per_lines, req_pack_count, no_lines_wo_comm_fil)

        #Metric-78: count of requires  : ratio : per lines
        '''
           count_of_requi refers to 'require =>'
           req_pack_count refers to 'require_package()'
        '''
        require_per_lines = float(count_of_requi) / float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(require_per_lines) + ","
        #print "requires per lines:{},requires:{}, lines:{}".format(require_per_lines, count_of_requi, no_lines_wo_comm_fil)


        #Metric-79: count of variable assignments  : ratio : per lines
        '''
            var_assi_cnt refers to '$hagu = 'lol' type Puppet statements
        '''
        var_per_lines = float(var_assign_cnt) / float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(var_per_lines) + ","
        #print "var. assig. per lines:{},var. assi.:{}, lines:{}".format(var_per_lines, var_assign_cnt, no_lines_wo_comm_fil)

        #Metric-80: count of variable assignments  : ratio : ''=>''
        '''
            var_assi_cnt refers to '$hagu =  'lol' type Puppet statements
            reff_cnt            to 'path' => '/usr/bin/' type Puppet statements
        '''
        if reff_cnt==0:
           reff_cnt = float(reff_cnt) + 0.50
        var_to_reffs = float(var_assign_cnt) / float(reff_cnt)
        metric_str_for_file = metric_str_for_file + str(var_to_reffs) + ","
        #print "var. to reffs:{},var. assi.:{},reffs:{}".format(var_to_reffs, var_assign_cnt, reff_cnt)


        #Metric-81: count of reffs (''=>''): ratio : block (= class + define)
        reffs_per_block = float(reff_cnt) / float(cnt_blocks)
        metric_str_for_file = metric_str_for_file + str(reffs_per_block) + ","
        #print "reffs2blocks:{},reffs:{},blocks:{}".format(reffs_per_block, reff_cnt, cnt_blocks)

        #Metric-82: count of reffs (''=>''): ratio : per lines
        reff_cnt_per_lines = float(reff_cnt) / float(no_lines_wo_comm_fil)
        metric_str_for_file = metric_str_for_file + str(reff_cnt_per_lines) + ","
        #print "'=>' counts per lines:{},=>:{}, lines:{}".format(reff_cnt_per_lines, reff_cnt, no_lines_wo_comm_fil)

        #Metric-83: count of reffs (''=>''): ratio : total resources
        '''
           total_reso_cnt_per_file represents all resources used in the file
        '''
        if total_reso_cnt_per_file==0:
           total_reso_cnt_per_file = float(total_reso_cnt_per_file) + 0.50
        reff_cnt2total_reso = float(reff_cnt) / float(total_reso_cnt_per_file)
        metric_str_for_file = metric_str_for_file + str(reff_cnt2total_reso) + ","
        #print "'=>' counts per lines:{},=>:{}, tot-reso:{}".format(reff_cnt2total_reso, reff_cnt, total_reso_cnt_per_file)

        #Metric-84: count of reffs (''=>''): ratio : required package counts
        '''
           req_pack_count refers to 'require_package()'
        '''
        if req_pack_count==0:
           req_pack_count = float(req_pack_count) + 0.50
        reff_cnt2req_pack = float(reff_cnt) / float(req_pack_count)
        metric_str_for_file = metric_str_for_file + str(reff_cnt2req_pack) + ","
        #print "'=>' counts per require_package:{},=>:{}, req_pkg:{}".format(reff_cnt2req_pack, reff_cnt, req_pack_count)

        #Metric-85: count of reffs (''=>''): ratio : required include counts
        '''
           count_of_includes refers to 'include::' , not 'include_packages()'
        '''
        if count_of_includes==0:
           count_of_includes = float(count_of_includes) + 0.50
        reff_cnt2incl_cnt = float(reff_cnt) / float(count_of_includes)
        metric_str_for_file = metric_str_for_file + str(reff_cnt2incl_cnt) + ","
        #print "'=>'counts 2 include count:{},=>:{}, incl:{}".format(reff_cnt2incl_cnt, reff_cnt, count_of_includes)
        '''
           Append everyhting !!!
        '''
        str2ret = str2ret + metric_str_for_file
        '''
        reset values
        '''
        max_nest_depth_for_file = 0
        no_class_dec_for_file = 0
        no_def_dec_for_file = 0
        no_pack_dec_for_file = 0
        no_file_dec_for_file = 0
        no_serv_dec_for_file = 0
        no_exec_dec_for_file = 0
        lack_cohe_meth_file = 0
        body_txt_size_file = 0
        no_lines_w_comm_file = 0
        no_lines_wo_comm_fil = 0
        no_outerelem_for_file = 0
        no_file_res_for_file = 0
        no_ser_res_for_file = 0
        no_package_res_for_file = 0
        no_hard_coded_stmt = 0
        no_node_dec_for_file = 0
        no_parent_cls_for_file = 0
        density_class_dec = 0
        density_define_dec = 0
        density_pack_dec = 0
        density_file_dec = 0
        density_serv_dec = 0
        density_exec_dec = 0
        density_outerlem = 0
        density_hardcode = 0
        count_of_includes = 0
        count_of_git_usages = 0
        count_of_requi = 0
        count_of_notify = 0
        count_of_ensure = 0
        count_of_alias = 0
        count_of_subsc = 0
        count_of_consume = 0
        count_of_export = 0
        count_of_sched = 0
        count_of_stage = 0
        count_of_tags = 0
        count_of_noop = 0
        count_of_before = 0
        count_of_audit = 0
        meta_param_total_cnt = 0
        count_of_inheri_usage = 0
        count_of_sql_usage = 0
        non_pp_count = 0
        mcx_count = 0
        rsyslog_count = 0
        valid_hash_count = 0
        req_pack_count = 0
        hiera_incl_count = 0
        incl_packs_count = 0
        ensure_packs_count = 0
        if_count = 0
        undef_count = 0
        avg_param_cnt = 0
        medi_param_cnt = 0
        max_param_cnt = 0
        min_param_cnt = 0
        var_assign_cnt = 0
        case_stmt_cnt = 0
        env_cnt = 0
        crone_cnt = 0
        reff_cnt = 0
        total_reso_cnt_per_file = 0
        cron_per_line =  0
        inc_per_line = 0
        inc_per_tot_reso_cnt = 0
        inc_per_file_cnt = 0
        inc_per_pkg_cnt = 0
        inc_per_svc_cnt = 0
        svc_cnt_per_blocks = 0
        total_reso_cnt_per_lines = 0
        total_reso_cnt_per_blocks = 0

        return str2ret
def hogarbal():
  fileName='paikhana1.pp'
  fileObj = SourceModel.SM_File.SM_File(fileName)
  getMetricsForFile(fileName)
  print "="*50
  cnt_includes = fileObj.getOnlyIncludeClassesCount()
  # count_of_git_usages = fileObj.getNoOfGitUsages()
  # print "Git count:", count_of_git_usages
  count_of_requires = fileObj.getOnlyRequireCount()
  print "count fo requires:", count_of_requires
  # count_of_notifies = fileObj.getOnlyNotifyCount()
  # count_of_ensures  = fileObj.getOnlyEnsureCount()
  # count_of_aliases  = fileObj.getOnlyAliasCount()
  # count_of_subscri  = fileObj.getOnlySubscribeCount()
  # count_of_consume  = fileObj.getOnlyConsumeCount()
  # count_of_export   = fileObj.getOnlyExportCount()
  # count_of_schedu   = fileObj.getOnlyScheduleCount()
  # count_of_stages   = fileObj.getOnlyStageCount()
  # count_of_tags     = fileObj.getOnlyTagCount()
  # count_of_noop     = fileObj.getOnlyNoopCount()
  # count_of_before   = fileObj.getOnlyBeforeCount()
  # count_of_audit    = fileObj.getOnlyAuditCount()


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
  print "*"*50


def getQualGenratedMetricForFile(fully_qualaified_path_to_file):
        str2ret = ""
        metric_str_for_file=""
        fileObj = SourceModel.SM_File.SM_File(fully_qualaified_path_to_file)
        #metric_str_for_file = fileObj.fileName + ","
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


        '''
           Append everyhting !!!
        '''
        str2ret = str2ret + metric_str_for_file
        '''
        reset values
        '''
        max_nest_depth_for_file = 0
        no_class_dec_for_file = 0
        no_def_dec_for_file = 0


        return str2ret
