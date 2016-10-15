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



        #More metrics to go ... Oct 14, 2016
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

        #Metric-48
        hiera_incl_count = fileObj.getHieraIncludeCount()
        metric_str_for_file = metric_str_for_file + str(hiera_incl_count) + "," 

        #Metric-49
        incl_packs_count = fileObj.getIncludePacksCount()
        metric_str_for_file = metric_str_for_file + str(incl_packs_count) + "," 

        #Metric-50
        ensure_packs_count = fileObj.getEnsurePacksCount()
        metric_str_for_file = metric_str_for_file + str(ensure_packs_count) + "," 

        #Metric-51
        if_count = fileObj.getIfElseCount()
        metric_str_for_file = metric_str_for_file + str(if_count) + ","  

        #Metric-52
        undef_count = fileObj.getUndefCount()
        metric_str_for_file = metric_str_for_file + str(undef_count) + ","                                  

        str2ret = str2ret + metric_str_for_file   
        return str2ret





def hogarbal():
  fileObj = SourceModel.SM_File.SM_File('paikhana1.pp')
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

  # print "Include count:", cnt_includes  
  # print "Require count",  count_of_requires
  # print "Notify count:",  count_of_notifies        
  # print "Ensure count",   count_of_ensures   
  # print "Alias count:",   count_of_aliases 
  # print "Subsc count:",   count_of_subscri  
  # print "Consume count:", count_of_consume  
  # print "Export count:",  count_of_export  
  # print "Schedule cnt:",  count_of_schedu               
  # print "Stages cnt:",    count_of_stages      
  # print "Tags count:",    count_of_tags
  # print "No-op count:",   count_of_noop  
  # print "Before count:",  count_of_before 
  # print "Audit count:",   count_of_audit 

  # meta_param_total_cnt = (     count_of_requires + count_of_notifies  + count_of_aliases + count_of_subscri + 
  #                              count_of_consume +  count_of_export +  count_of_schedu +  count_of_stages +  count_of_tags +
  #                              count_of_noop +   count_of_before +  count_of_audit  
  #                        ) 
  # print "*"*100 
  # print "Total meta usages: ", meta_param_total_cnt
  #count_of_inher    = fileObj.getOnlyInheritanceUsageCount()
  #print "Inheritance use count:", count_of_inher             
  #count_of_sql_ref    = fileObj.getOnlySQLUsageCount()
  #print "SQL use count:", count_of_sql_ref        
  #non_pp_count = fileObj.getNonPuppetUsageCount()
  #rint "Non puppet usage count:", non_pp_count    
  #mcx_cnt = fileObj.getMCXCount()
  #print "MCX Count:", mcx_cnt  
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