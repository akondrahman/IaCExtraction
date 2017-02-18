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

        # Metric-4: local and remote location usgaes
        location_usg_for_file  = file_usg_for_file + url_usg_for_file
        metric_str_for_file    = metric_str_for_file + str(location_usg_for_file) + ","

        # Metric-5: SLOC
        lines_for_file  = sum(1 for line in open(fully_qualaified_path_to_file))
        metric_str_for_file = metric_str_for_file + str(lines_for_file) + ","

        # Metric-6: location reff per SLOC
        loca_per_sloc    = float(location_usg_for_file)/float(lines_for_file)
        loca_per_sloc    = round(loca_per_sloc, 5)
        metric_str_for_file = metric_str_for_file + str(loca_per_sloc) + ","

        # Metric-7: get include usages
        incl_usg_for_file      = fileObj.getOnlyIncludeClassesCount()
        metric_str_for_file = metric_str_for_file + str(incl_usg_for_file) + ","

        # Metric-8: get require usages
        req_usg_for_file      = fileObj.getOnlyRequireCount()
        metric_str_for_file = metric_str_for_file + str(req_usg_for_file) + ","

        # Metric-9: get ensure usages
        ens_usg_for_file      = fileObj.getOnlyEnsureCount()
        metric_str_for_file = metric_str_for_file + str(ens_usg_for_file) + ","

        # Metric-10: get unless usages
        unless_usg_for_file   = fileObj.getOnlyUnlessCount()
        metric_str_for_file = metric_str_for_file + str(unless_usg_for_file) + ","

        # Metric-11: get before usages
        before_usg_for_file   = fileObj.getOnlyBeforeCount()
        metric_str_for_file   = metric_str_for_file + str(before_usg_for_file) + ","

        # Metric-12: get dependencies
        dependency_for_file   = incl_usg_for_file + req_usg_for_file + ens_usg_for_file + unless_usg_for_file + before_usg_for_file
        metric_str_for_file   = metric_str_for_file + str(dependency_for_file) + ","

        # Metric-13: get dependencies per SLOC
        dependency_per_sloc   = float(dependency_for_file)/float(lines_for_file)
        metric_str_for_file   = metric_str_for_file + str(dependency_for_file) + ","

        '''
           Append everyhting !!!
        '''
        str2ret = str2ret + metric_str_for_file
        '''
        reset values
        '''
        pkg_usg_for_file, location_usg_for_file, file_usg_for_file, url_usg_for_file = 0, 0, 0, 0
        lines_for_file, loca_per_sloc, dependency_per_sloc = 0, 0, 0
        dependency_for_file, incl_usg_for_file, req_usg_for_file, ens_usg_for_file, unless_usg_for_file = 0, 0, 0, 0, 0
        before_usg_for_file = 0

        return str2ret
