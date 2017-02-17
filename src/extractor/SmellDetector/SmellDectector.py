from SmellDetector import AbsSmellDectector, ModSmellDectector, HieSmellDectector, DepSmellDectector, EncSmellDectector
from SmellDetector import Utilities
import os
import SourceModel.SM_File

# def detectSmells(folder, outputFile):
#     AbsSmellDectector.detectSmells(folder, outputFile)
#     EncSmellDectector.detectSmells(folder, outputFile)
#     ModSmellDectector.detectSmells(folder, outputFile)
#     DepSmellDectector.detectSmells(folder, outputFile)
#     HieSmellDectector.detectSmells(folder, outputFile)
#     ### get Graph data
#     graph_for_this_folder = ModSmellDectector.getGraph(folder)
#     #graph_for_this_folder.printGraph()
#     avg_degre = graph_for_this_folder.getAverageDegree()
#     str_avg_degree =  "Average degree of {} graph={}".format(folder, avg_degre) + "\n"
#     str_avg_degree =  str_avg_degree + "#######################" + "\n"
#     node_count = graph_for_this_folder.getNodeCount()
#     edge_count = graph_for_this_folder.getEdgeCount()
#     graph_details_as_str = graph_for_this_folder.printGraph()
#     nodes_edges_str = "Nodes in this graph:{}, edges in this graph:{}".format(node_count, edge_count) + "\n"
#     nodes_edges_str = nodes_edges_str +  "#######################" + "\n"
#     graph_file_to_save = folder + "/full_graph.txt"
#     str_graph = graph_details_as_str + str_avg_degree + nodes_edges_str
#     #print str_graph
#     dump_status = Utilities.dumpStrToFile(graph_file_to_save, str_graph)
#     print "Dumped a file of {} bytes".format(dump_status)


def getQualGenratedMetricForFile(fully_qualaified_path_to_file):
        str2ret = ""
        metric_str_for_file=""
        fileObj = SourceModel.SM_File.SM_File(fully_qualaified_path_to_file)
        #metric_str_for_file = fileObj.fileName + ","
        # direct metrics

        # Metric-1: package usages
        pkg_usg_for_file  = fileObj.getNoOfPackageDeclarations()
        metric_str_for_file = metric_str_for_file + str(pkg_usg_for_file) + ","


        # Metric-2: url usages
        url_usg_for_file    = fileObj.getURLUsages()
        metric_str_for_file = metric_str_for_file + str(url_usg_for_file) + ","

        # Metric-3: get file usages
        file_usg_for_file      = fileObj.getNoOfFileDeclarations()
        metric_str_for_file = metric_str_for_file + str(file_usg_for_file) + ","


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
