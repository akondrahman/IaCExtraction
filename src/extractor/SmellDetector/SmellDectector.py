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


        # Metric-22
        density_serv_dec = float(no_serv_dec_for_file)/float(no_lines_wo_comm_fil) 
        metric_str_for_file = metric_str_for_file + str(density_serv_dec) + ","             
        str2ret = str2ret + metric_str_for_file   
        return str2ret