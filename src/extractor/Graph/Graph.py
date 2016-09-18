
class Graph:
    def __init__(self):
        self.dict = dict()

    def addNode(self, node):
        if not self.dict.__contains__(node):
            self.dict[node] = []

    def getNodeCount(self):
        return len(self.dict)

    def addEdge(self, node1, node2):
        if self.dict.__contains__(node1) and self.dict.__contains__(node2):
            if not self.dict[node1].__contains__(node2):
                self.dict[node1].append(node2)

    def getEdgeCount(self):
        counter = 0
        for item in self.dict:
            if self.dict[item]:
                counter += len(self.dict[item])
        return counter

    def printGraph(self):
        strToRet = ""        
        str1 = "***** Printing the Graph Started *****" + "\n"
        str2=""
        for item in self.dict.keys():
          #print ("key: " + str(item) + " value: " + str(self.dict[item]))
          nodeX  =  item.getId()
          nodesY =  self.dict[item] 
          for elem in nodesY: 
            nodeY = elem.getId()    
            str2 = str2 + "NodeX:{} -----> NodeY:{}".format(nodeX, nodeY) + "\n"
            str2 = str2 + "------------------------------" + "\n"
            str2 = str2 + "NodeX.dependency---> internal:{}, external:{}".format(item.internalDep, item.externalDep) + "\n"
            str2 = str2 + "------------------------------" + "\n"
            str2 = str2 + "NodeY.dependency---> internal:{}, external:{}".format(elem.internalDep, elem.externalDep) + "\n"
            str2 = str2 + "------------------------------" + "\n"
            reso_node_x = item.getResources()
            reso_node_y = elem.getResources()
            for reso_x in reso_node_x:
              str2 = str2 + "Resource for NodeX=name:{},type:{}".format(reso_x.name, reso_x.type) + "\n"
            str2 = str2 + "------------------------------" + "\n"
            for reso_y in reso_node_y:
              str2 = str2 + "Resource for NodeY=name:{},type:{}".format(reso_y.name, reso_y.type)    + "\n"          
            str2 = str2 + "------------------------------"              + "\n"
        str3 = str2 +  "***** Printing the Graph Ended *****" + "\n"
        strToRet = str1 + str2 +str3 
        str2 = ""
        return strToRet
        
    def getNodeWithId(self, id):
        for node in self.dict.keys():
            if node.id == id:
                return node

    def getNodes(self):
        return self.dict.keys()

    def getAverageDegree(self):
        totalEdges = self.getEdgeCount()
        totalNodes = len(self.dict.keys())
        if totalNodes == 0:
            return float(0)
        else:
            return float(totalEdges * 2)/float(totalNodes)
