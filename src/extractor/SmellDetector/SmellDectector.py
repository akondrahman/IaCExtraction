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

        # Metric-14: get define usages
        define_usg_for_file   = fileObj.getNoOfDefineDeclarations()
        metric_str_for_file   = metric_str_for_file + str(define_usg_for_file) + ","

        # Metric-15: get reff aka '=>' usages
        reff_usg_for_file   = fileObj.getReffCount()
        metric_str_for_file = metric_str_for_file + str(reff_usg_for_file) + ","

        # Metric-16: get compar aka '>=, ==, <=' usages
        cond_usg_for_file   = fileObj.getCondCount()
        metric_str_for_file = metric_str_for_file + str(cond_usg_for_file) + ","

        # Metric-17: get namenode_hosts usages
        namenode_usg_for_file   = fileObj.getOnlyNamenodeCount()
        metric_str_for_file     = metric_str_for_file + str(namenode_usg_for_file) + ","

        # Metric-18: get cron usages
        cron_usg_for_file       = fileObj.getCronCount()
        metric_str_for_file     = metric_str_for_file + str(cron_usg_for_file) + ","

        # Metric-19: get parameter usages
        param_usg_for_file       = fileObj.getClassParamCount() ## give a tuple of 4 vlaues
        param_usg_for_file       = param_usg_for_file[0] ## taking the median
        metric_str_for_file      = metric_str_for_file + str(param_usg_for_file) + ","

        # Metric-20: get hard coded strings
        hard_code_for_file       = len(fileObj.getHardCodedStatments())
        metric_str_for_file      = metric_str_for_file + str(hard_code_for_file) + ","

        # Metric-21: get hard coded strings
        hard_code_per_sloc       = float(hard_code_for_file)/float(lines_for_file)
        hard_code_per_sloc       = round(hard_code_per_sloc, 5)
        metric_str_for_file      = metric_str_for_file + str(hard_code_per_sloc) + ","

        # Metric-22: get comment counts
        comm_count_for_file      = fileObj.getLinesOfComments()
        metric_str_for_file      = metric_str_for_file + str(comm_count_for_file) + ","

        # Metric-23: get comment counts per LOC
        comm_count_per_SLOC      = float(comm_count_for_file)/float(lines_for_file)
        comm_count_per_SLOC      = round(comm_count_per_SLOC, 5)
        metric_str_for_file      = metric_str_for_file + str(comm_count_per_SLOC) + ","

        # Metric-24: get runinterval counts
        run_int_for_file         = fileObj.getRunIntervalCount()
        metric_str_for_file      = metric_str_for_file + str(run_int_for_file) + ","

        # Metric-25: get command counts
        command_count_for_file      = fileObj.getCommandCount()
        metric_str_for_file         = metric_str_for_file + str(command_count_for_file) + ","

        # Metric-26: get path counts
        path_count_for_file      = fileObj.getPathCount()
        metric_str_for_file      = metric_str_for_file + str(path_count_for_file) + ","

        # Metric-27: get ssh auth counts
        ssh_auth_count_for_file      = fileObj.getSSHAuthCount()
        metric_str_for_file          = metric_str_for_file + str(ssh_auth_count_for_file) + ","

        # Metric-28: get file mode counts
        file_mode_count_for_file      = fileObj.getFileModeCount()
        metric_str_for_file           = metric_str_for_file + str(file_mode_count_for_file) + ","


        # Metric-29: get role counts
        role_count_for_file           = fileObj.getRoleCount()
        metric_str_for_file           = metric_str_for_file + str(role_count_for_file) + ","

        # Metric-30: get secuirty issue
        secu_count_for_file           = ssh_auth_count_for_file + file_mode_count_for_file + role_count_for_file
        metric_str_for_file           = metric_str_for_file + str(secu_count_for_file) + ","

        # Metric-31: get secuirty  counts per LOC
        secu_count_per_SLOC      = float(secu_count_for_file)/float(lines_for_file)
        secu_count_per_SLOC      = round(secu_count_per_SLOC, 5)
        metric_str_for_file      = metric_str_for_file + str(secu_count_per_SLOC) + ","



        '''
           Append everyhting !!!
        '''
        str2ret = str2ret + metric_str_for_file
        '''
        reset values
        '''
        pkg_usg_for_file, location_usg_for_file, file_usg_for_file, url_usg_for_file = 0, 0, 0, 0
        lines_for_file, loca_per_sloc, dependency_per_sloc, hard_code_per_sloc, comm_count_per_SLOC = 0, 0, 0, 0, 0
        dependency_for_file, incl_usg_for_file, req_usg_for_file, ens_usg_for_file, unless_usg_for_file = 0, 0, 0, 0, 0
        before_usg_for_file, define_usg_for_file, reff_usg_for_file, cond_usg_for_file, namenode_usg_for_file = 0, 0, 0, 0, 0
        cron_usg_for_file, param_usg_for_file, hard_code_for_file = 0, 0, 0
        comm_count_for_file, run_int_for_file, command_count_for_file, path_count_for_file  = 0, 0, 0, 0
        secu_count_per_SLOC, secu_count_for_file = 0, 0
        return str2ret
