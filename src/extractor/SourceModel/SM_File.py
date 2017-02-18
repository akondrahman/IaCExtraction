import re

import SourceModel.SM_CaseStmt
import SourceModel.SM_Class
import SourceModel.SM_Constants as SMCONSTS
import SourceModel.SM_Define
#import SourceModel.SM_Define
import SourceModel.SM_Element
import SourceModel.SM_Exec
import SourceModel.SM_FileResource
import SourceModel.SM_IfStmt
import SourceModel.SM_IncludeResource
import SourceModel.SM_LCOM
import SourceModel.SM_Node
import SourceModel.SM_PackageResource
import SourceModel.SM_ServiceResource
import SourceModel.SM_User
from SmellDetector import Utilities


class SM_File:

    def __init__(self, file_=""):
        if file_ != "":
            #print "asi mama", file_
            #curFile = open(file_, 'rt', errors='ignore')
            curFile = open(file_, 'rt')
            self.fileText = curFile.read()
            self.resourceBodyText = self.fileText
            self.fileName = file_
            curFile.close()

    def setText(self, text):
        self.fileText = text

    def getNoOfClassDeclarations(self):
        ##Oct 17, 2016: needed extra code for removing commented stuff
        inv_class_count = self.countEntityDeclaration(SMCONSTS.INVALID_CLASS_REGEX, "invalid class")
        all_class_count = self.countEntityDeclaration(SMCONSTS.CLASS_REGEX, "class")
        cls_cnt_to_ret  = all_class_count - inv_class_count
        return cls_cnt_to_ret

    def getNoOfDefineDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.DEFINE_REGEX, "define")

    def getNoOfFileDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.FILE_REGEX, "file")

    def getNoOfPackageDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.PACKAGE_REGEX, "package")

    def getNoOfServiceDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.SERVICE_REGEX, "service")

    def getNoOfExecDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.EXEC_REGEX, "exec")


    ##Oct 14, 2016
    # def getNoOfGitUsages(self):
    #     return self.countEntityDeclaration(SMCONSTS.ONLY_GIT_REGEX, "git")

    def getLinesOfCode(self):
        counter = self.countEntityDeclaration(SMCONSTS.LOC_REGEX, "newLine")
        if counter > 0:
            return counter+1

        if (len(self.fileText) > 0):
            return 1
        return 0

    def getLinesOfCodeWithoutComments(self):
        totalLines = self.getLinesOfCode()
        totalCommentsLines = self.getLinesOfComments()
        return totalLines - totalCommentsLines

    def getLinesOfComments(self):
        counter = self.countEntityDeclaration(SMCONSTS.COMMENT_REGEX, "newLine")
        return counter

    def countEntityDeclaration(self, regEx, entityType):
        compiledRE = re.compile(regEx)
        # Utilities.myPrint("Identified " + entityType + " declarations: " + str(compiledRE.findall(self.fileText)) + \
        #                   " Size: " + str(len(compiledRE.findall(self.fileText))))
        matchedTxt = compiledRE.findall(self.fileText)
        #print "Identified: {}  declarations: {} Size: {}".format(entityType, str(matchedTxt), len(matchedTxt))
        return len(matchedTxt)

    def getFileResourceList(self):
        compiledRE = re.compile(SMCONSTS.FILE_REGEX)
        fileResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            fileResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted file declaration: " + fileResourceText)
            fileResourceObj = SourceModel.SM_FileResource.SM_FileResource(fileResourceText)
            fileResourceList.append(fileResourceObj)
        return fileResourceList

    def extractResourceText(self, initialString):
        index = self.fileText.find(initialString)
        if index < 0:
            return initialString

        compiledRE1 = re.compile(r'\{')
        compiledRE2 = re.compile(r'\}')
        curBracketCount = len(compiledRE1.findall(initialString)) - len(compiledRE2.findall(initialString))

        curIndex = index + len(initialString) + 1
        if curBracketCount == 0:
            #This is to find the first "{" since currently there is no { which may happen in case of multi-line def
            found = False
            while curIndex < len(self.fileText) and not found:
                if self.fileText[curIndex] == '{':
                    found = True
                    curBracketCount = 1
                curIndex += 1

        while curBracketCount > 0 and curIndex < len(self.fileText):
            if self.fileText[curIndex] == '}':
                curBracketCount -= 1
            if self.fileText[curIndex] == '{':
                curBracketCount += 1
            curIndex +=1

        return self.fileText[index:curIndex]

    def getServiceResourceList(self):
        compiledRE = re.compile(SMCONSTS.SERVICE_REGEX)
        serviceResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            serviceResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted service declaration: " + serviceResourceText)
            serviceResourceObj = SourceModel.SM_ServiceResource.SM_ServiceResource(serviceResourceText)
            serviceResourceList.append(serviceResourceObj)
        return serviceResourceList

    def getPackageResourceList(self):
        compiledRE = re.compile(SMCONSTS.PACKAGE_REGEX)
        packageResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            packageResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted package declaration: " + packageResourceText)
            packageResourceObj = SourceModel.SM_PackageResource.SM_PackageResource(packageResourceText)
            packageResourceList.append(packageResourceObj)
        return packageResourceList

    def getClassDeclarationList(self):
        compiledRE = re.compile(SMCONSTS.CLASS_REGEX)
        compiledClassNameRE = re.compile(SMCONSTS.CLASS_NAME_REGEX)
        classList = []
        for match in compiledRE.findall(self.fileText):
            className = compiledClassNameRE.findall(match)[0]
            #print("Class name: %s" % (className))
            classText = self.extractResourceText(match)
            Utilities.myPrint("Extracted class declaration: " + classText)
            classObj = SourceModel.SM_Class.SM_Class(classText, className)
            classList.append(classObj)
        return classList

    def getDefineDeclarationList(self):
        compiledRE = re.compile(SMCONSTS.DEFINE_REGEX)
        defineList = []
        for match in compiledRE.findall(self.fileText):
            defineText, s, e = self.extractElementText(match)
            Utilities.myPrint("Extracted define declaration: " + defineText)
            defineObj = SourceModel.SM_Define.SM_Define(defineText)
            defineList.append(defineObj)
        return defineList

    def getLCOM(self):
        return SourceModel.SM_LCOM.getLCOM(self.getOuterElementList())

    def getBodyTextSize(self):
        loc = self.getLinesOfCode()
        return loc, len(self.resourceBodyText)

    def getOuterClassList(self):
        outerElementList = self.getOuterElementList()
        classList = []
        for element in outerElementList:
            if type(element) is SourceModel.SM_Class.SM_Class:
                classList.append(element)
        return classList

    def getOuterDefineList(self):
        outerElementList = self.getOuterElementList()
        defineList = []
        for element in outerElementList:
            if type(element) is SourceModel.SM_Define.SM_Define:
                defineList.append(element)
        return defineList
        # exElementList = []
        # exElementList.extend(self.getElementList(SMCONSTS.DEFINE_REGEX))
        # filteredList = self.filterOutInnerElements(exElementList)
        # return filteredList

    def getOuterElementList(self):
        exElementList = []
        exElementList.extend(self.getElementList(SMCONSTS.CLASS_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.SERVICE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.CASE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.DEFINE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.EXEC_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.FILE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.IF_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.PACKAGE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.USER_REGEX))
        filteredList = self.filterOutInnerElements(exElementList)
        return filteredList

    def getElementList(self, regex):
        compiledRE = re.compile(regex)
        exElementList = []
        for str_ in (compiledRE.findall(self.fileText)):
            #print str_
            elementText, startIndex, endIndex = self.extractElementText(str_)
            #print "txt:{}, start:{}, end:{}".format(elementText, startIndex, endIndex)
            elementObj = self.getElementObject(elementText, regex)
            exElementList.append(ExElement(elementObj, startIndex, endIndex))

        return exElementList

# TODO: Handle variables
# Unwrap classes from list
    def getOnlyIncludeClasses(self):
        compiledIncludeRE = re.compile(SMCONSTS.DECLARE_INCLUDE_REGEX)
        compiledResourceRE = re.compile(SMCONSTS.DECLARE_RESOURCE_REGEX)
        declareClassList = []
        declareClassName = ""
        for match in (compiledIncludeRE.findall(self.fileText)):
            #print(match)
            declareClassText = match
            cleanInclude = re.sub(r'^\s*include \[?(.+)\]?\s*$', r'\1', declareClassText)
            #print("Clean include: %s" % cleanInclude)
            class_name = r'(?:Class\[)?\'?\:{0,2}([\w\d\:\-_\$]+)\'?\]?'
            classRE = re.compile(class_name)
            if ',' in cleanInclude:
              classes = cleanInclude.split(',')
              for c in classes:
                for m in classRE.findall(c):
                  # Find a variable value in text
                  if m.startswith('$'):
                    #print("Variable: %s" % m)
                    varRE = r'(?:^|\n)\s*\$[\w\d\-_]+\s?=\s?\'?\"?([\w\d\-_]+)\'?\"?\n'
                    compiledVarRE = re.compile(varRE)
                    for v in (compiledVarRE.findall(self.fileText)):
                      #print(v)
                      declareClassName = v
                      Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                      declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                      declareClassList.append(declareResourceObj)
                      break
                      #print("Variable %s value)
                  #print("Extracted class name: %s" % m)
                  else:
                    declareClassName = m
                    Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                    declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                    declareClassList.append(declareResourceObj)
            else:
              for c in classRE.findall(cleanInclude):
                #print("Extracted class name: %s" % c)
                declareClassName = c
            #print("%s" % includeClassText)
                Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                declareClassList.append(declareResourceObj)
        for match in (compiledResourceRE.findall(self.fileText)):
            #print(match)
            declareClassText = match
            declareClassName = declareClassText
            #print("%s" % includeClassText)
            Utilities.myPrint("Extracted resource class declaration: " + declareClassText)
            declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
            declareClassList.append(declareResourceObj)
        return declareClassList


    def extractElementText(self, initialString):
        compiledRE1 = re.compile(r'\{')
        compiledRE2 = re.compile(r'\}')
        #print initialString
        lol1=len(compiledRE1.findall(initialString))
        lol2=len(compiledRE2.findall(initialString))
        #####print"1:{}, 1:{}".format(lol1, lol2)
        curBracketCount = len(compiledRE1.findall(initialString)) - len(compiledRE2.findall(initialString))
        index = self.fileText.find(initialString)
        if index < 0:
            return initialString, 0, len(initialString)
        curIndex = index + len(initialString) + 1
        if curBracketCount == 0:
            #And now we need to find the corresponding ')' to avoid any errors where curly brackets are matched
            #in the parameters itself.
            found = False
            while curIndex < len(self.fileText) and not found:
                if self.fileText[curIndex] == ')':
                    found = True
                curIndex +=1

            #This is to find the first "{" since currently there is no { which may happen in case of multi-line class def
            found = False
            while curIndex < len(self.fileText) and not found:
                if self.fileText[curIndex] == '{':
                    found = True
                    curBracketCount = 1
                curIndex += 1

        while curBracketCount > 0 and curIndex < len(self.fileText):
            if self.fileText[curIndex] == '}':
                curBracketCount -= 1
            if self.fileText[curIndex] == '{':
                curBracketCount += 1
            curIndex +=1
        index2ret , curIndex2ret = index, curIndex
        index, curIndex = 0, 0
        return self.fileText[index2ret:curIndex2ret], index2ret, curIndex2ret

    def getElementObject(self, elementText, regex):
        if regex == SMCONSTS.CLASS_REGEX:
            return SourceModel.SM_Class.SM_Class(elementText)
        if regex == SMCONSTS.DEFINE_REGEX:
            return SourceModel.SM_Define.SM_Define(elementText)
        if regex == SMCONSTS.EXEC_REGEX:
            return SourceModel.SM_Exec.SM_Exec(elementText)
        if regex == SMCONSTS.FILE_REGEX:
            return SourceModel.SM_FileResource.SM_FileResource(elementText)
        if regex == SMCONSTS.PACKAGE_REGEX:
            return SourceModel.SM_PackageResource.SM_PackageResource(elementText)
        if regex == SMCONSTS.SERVICE_REGEX:
            return SourceModel.SM_ServiceResource.SM_ServiceResource(elementText)
        if regex == SMCONSTS.DECLARE_INCLUDE_REGEX or regex == SMCONSTS.DECLARE_RESOURCE_REGEX:
            return SourceModel.SM_IncludeResource.SM_IncludeResource(elementText)
        if regex == SMCONSTS.IF_REGEX:
            return SourceModel.SM_IfStmt.SM_IfStmt(elementText)
        if regex == SMCONSTS.CASE_REGEX:
            return SourceModel.SM_CaseStmt.SM_CaseStmt(elementText)
        if regex == SMCONSTS.USER_REGEX:
            return SourceModel.SM_User.SM_User(elementText)

    def sort(self, exClassElementList):
        result = []
        while len(exClassElementList) > 0:
            largest = self.findLargest(exClassElementList)
            result.append(largest)
            exClassElementList.remove(largest)
        return result

    def findLargest(self, exClassElementList):
        if len(exClassElementList) > 0:
            largest = exClassElementList[0]
            for item in exClassElementList:
                if (item.endIndex - item.startIndex) > (largest.endIndex - item.startIndex):
                    largest = item
            return largest

    def filterOutInnerElements(self, exClassElementList):
        filteredList = []
        exClassElementList = self.sort(exClassElementList)
        for element in exClassElementList:
            found = False
            for filteredItem in filteredList:
                if element.startIndex >= filteredItem.startIndex and element.endIndex <= filteredItem.endIndex:
                    found = True
                    break
            if found == False:
                filteredList.append(element)
        classElementList = []
        for item in filteredList:
            classElementList.append(item.elementObj)
        return classElementList

    def getMaxNestingDepth(self):
        maxNestingDepth = 0
        curIndex = 0
        curBracketCount = 0
        while curIndex < len(self.fileText):
            if self.fileText[curIndex] == '}':
                curBracketCount -= 1
            if self.fileText[curIndex] == '{':
                curBracketCount += 1
                if curBracketCount > maxNestingDepth:
                    maxNestingDepth = curBracketCount
            curIndex +=1

        return maxNestingDepth

    def getHardCodedStatments(self):
        compiledRE = re.compile(SMCONSTS.HARDCODED_VALUE_REGEX)
        hardCodedStmtList = compiledRE.findall(self.fileText)
        filteredList = []
        for item in hardCodedStmtList:
            #print(item)
            if not (item.__contains__("$") or item.__contains__("Package") or item.__contains__("Service") \
                    or item.__contains__("File")):
                filteredList.append(item)
        #print(filteredList)
        return filteredList

    def getClassHierarchyInfo(self):
        classDecls = self.getClassDeclarationList()
        classList = []
        parentClassList = []
        for aClass in classDecls:
            classes, pClasses = aClass.getClassHierarchyInfo()
            if len(classes) > 0:
                classList.append(classes)
            if len(pClasses) > 0:
                parentClassList.append(pClasses)
        return classList, parentClassList

    def getNodeDeclarations(self):
        compiledRE = re.compile(SMCONSTS.NODE_REGEX)
        nodeResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            nodeResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted node declaration: " + nodeResourceText)
            nodeResourceObj = SourceModel.SM_Node.SM_Node(nodeResourceText)
            nodeResourceList.append(nodeResourceObj)
        return nodeResourceList



#### Added on Oct 14, 2016
    def getOnlyIncludeClassesCount(self):
        cnt_of_includes = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_INCLUDE_REGEX)
        declareClassList = []
        for match in (compiledIncludeRE.findall(self.fileText)):
            cnt_of_includes = cnt_of_includes + 1
            #print match
            declareClassText = match
            cleanInclude = re.sub(r'^\s*include \[?(.+)\]?\s*$', r'\1', declareClassText)
            #print "Clean include: ", cleanInclude
            class_name = r'(?:Class\[)?\'?\:{0,2}([\w\d\:\-_\$]+)\'?\]?'
            classRE = re.compile(class_name)
            if ',' in cleanInclude:
              classes = cleanInclude.split(',')
              for c in classes:
                for m in classRE.findall(c):
                  # Find a variable value in text
                  if m.startswith('$'):
                    #print("Variable: %s" % m)
                    varRE = r'(?:^|\n)\s*\$[\w\d\-_]+\s?=\s?\'?\"?([\w\d\-_]+)\'?\"?\n'
                    compiledVarRE = re.compile(varRE)
                    for v in (compiledVarRE.findall(self.fileText)):
                      #print(v)
                      declareClassName = v
                      #Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                      declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                      declareClassList.append(declareResourceObj)
                      break
                      #print("Variable %s value)
                      #print "if block: Extracted class name:", m
                  else:
                    declareClassName = m
                    Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                    declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                    declareClassList.append(declareResourceObj)
            else:
              for c in classRE.findall(cleanInclude):
                #print "else block: Extracted class name: ", c
                declareClassName = c
                #print("%s" % includeClassText)
                #Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                declareClassList.append(declareResourceObj)
        #print "Declre class list contents in the end:", declareClassList
        #print "Total count of includes: ", cnt_of_includes
        return cnt_of_includes



    def getOnlyRequireCount(self):
        cnt_of_requires = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_REQUIRE_REGEX)
        declareClassList = []
        for match in (compiledIncludeRE.findall(self.fileText)):
            cnt_of_requires = cnt_of_requires + 1
            #print match
            declareClassText = match
            cleanInclude = re.sub(r'^\s*require \[?(.+)\]?\s*$', r'\1', declareClassText)
            class_name = r'(?:Class\[)?\'?\:{0,2}([\w\d\:\-_\$]+)\'?\]?'
            classRE = re.compile(class_name)
            if ',' in cleanInclude:
              classes = cleanInclude.split(',')
              for c in classes:
                for m in classRE.findall(c):
                  # Find a variable value in text
                  if m.startswith('$'):
                    #print("Variable: %s" % m)
                    varRE = r'(?:^|\n)\s*\$[\w\d\-_]+\s?=\s?\'?\"?([\w\d\-_]+)\'?\"?\n'
                    compiledVarRE = re.compile(varRE)
                    for v in (compiledVarRE.findall(self.fileText)):
                      #print(v)
                      declareClassName = v

                      declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                      declareClassList.append(declareResourceObj)
                      break
                  else:
                    declareClassName = m
                    Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                    declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                    declareClassList.append(declareResourceObj)
            else:
              for c in classRE.findall(cleanInclude):
                declareClassName = c

                declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                declareClassList.append(declareResourceObj)

        return cnt_of_requires
    def getOnlyNotifyCount(self):
        cnt_of_notifies = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_NOTIFY_REGEX)
        for match in (compiledIncludeRE.findall(self.fileText)):
            cnt_of_notifies = cnt_of_notifies + 1
        return cnt_of_notifies

    def getOnlyEnsureCount(self):
        cnt_of_ensures = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_ENSURE_REGEX)
        for match in (compiledIncludeRE.findall(self.fileText)):
            cnt_of_ensures = cnt_of_ensures + 1
        return cnt_of_ensures


    def getOnlyAliasCount(self):
        cnt_of_alias = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_ALIAS_REGEX)
        cnt_of_alias = len(compiledIncludeRE.findall(self.fileText))
        return cnt_of_alias
    def getOnlySubscribeCount(self):
        cnt_of_subs = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_SUBSCRIBE_REGEX)
        cnt_of_subs = len(compiledIncludeRE.findall(self.fileText))
        return cnt_of_subs
    def getOnlyConsumeCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_CONSUME_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyExportCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_EXPORT_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyScheduleCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_SCHEDULE_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyStageCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_STAGE_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyTagCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_TAG_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyNoopCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_NOOP_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyBeforeCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_BEFORE_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyAuditCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_AUDIT_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getOnlyInheritanceUsageCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.CLASS_INH_REGEX)
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #   print match
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_



    def getOnlySQLUsageCount(self):
        cnt_ = 0
        compiledIncludeRE1 = re.compile(SMCONSTS.ONLY_SQL_REGEX)
        cnt_1 = len(compiledIncludeRE1.findall(self.fileText))

        compiledIncludeRE2 = re.compile(SMCONSTS.POSTGRES_REGEX)
        cnt_2 = len(compiledIncludeRE2.findall(self.fileText))

        #for match in (compiledIncludeRE2.findall(self.fileText)):
        #   print match
        cnt_ = cnt_1 + cnt_2
        return cnt_

    def getNonPuppetUsageCount(self):
        cnt_ = 0
        usage_type1 = re.compile(SMCONSTS.ONLY_TYPEDEF_REGEX)
        cnt_1       = len(usage_type1.findall(self.fileText))
        #usage_type3 = re.compile(SMCONSTS.ONLY_CHAR_REGEX)
        #cnt_3       = len(usage_type3.findall(self.fileText))
        #usage_type4 = re.compile(SMCONSTS.ONLY_INT_REGEX)
        #cnt_4       = len(usage_type4.findall(self.fileText))
        usage_type5 = re.compile(SMCONSTS.ONLY_VOID_REGEX)
        cnt_5       = len(usage_type5.findall(self.fileText))
        usage_type6 = re.compile(SMCONSTS.ONLY_UNSIGN_REGEX)
        cnt_6       = len(usage_type6.findall(self.fileText))
        usage_type7 = re.compile(SMCONSTS.ONLY_CMODE_REGEX)
        cnt_7       = len(usage_type7.findall(self.fileText))

        #for match in (compiledIncludeRE.findall(self.fileText)):
        #   print match
        #cnt_ = cnt_1  + cnt_3 + cnt_4 + cnt_5 + cnt_6 + cnt_7
        cnt_ = cnt_1  + cnt_5 + cnt_6 + cnt_7
        ###print "1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}".format(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_6, cnt_7)
        return cnt_

    def getMCXCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_MCX_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #   print match
        return cnt_



    def getRSysLogCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_RSYSLOG_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #   print match
        return cnt_
    def getValidateHashCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.VALIDATE_HASH_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #   print match
        return cnt_

    def getRequirePackageCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.REQUIRE_PACK_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #   print match
        return cnt_

    def getHieraIncludeCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.HIERA_INCL_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #   print match
        return cnt_
    def getIncludePacksCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.INCL_PACK_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #  print match
        return cnt_
    def getEnsurePacksCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ENSU_PACK_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #  print match
        return cnt_

    def getClassParamCount(self):
        import numpy as np
        allClassParams = []
        compiledIncludeRE = re.compile(SMCONSTS.CLASS_PARAM_REGEX, re.DOTALL)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        for match in (compiledIncludeRE.findall(self.fileText)):
          str_ = match.strip('(')
          str_ = match.strip(')')
          str_ = match.strip('\n')
          splitted_str = match.split(',')
          splitted_str = [x_.strip('\n') for x_ in splitted_str]
          splitted_str = [x_ for x_ in splitted_str if '$' in x_]
          splitted_str = [x_ for x_ in splitted_str if '=>' not in x_]
          splitted_str = [x_ for x_ in splitted_str if 'if' not in x_]
          splitted_str = [x_ for x_ in splitted_str if 'file' not in x_]
          splitted_str = [x_ for x_ in splitted_str if '[' not in x_]
          splitted_str = [x_ for x_ in splitted_str if ']' not in x_]
          splitted_str = np.unique(splitted_str)
          #print splitted_str
          #print match
          #print"="*25
          paramCnt = len(splitted_str)
          allClassParams.append(paramCnt)
        if len(allClassParams) > 0:
          stats_ = (np.mean(allClassParams), np.median(allClassParams), max(allClassParams), min(allClassParams))
        else:
          stats_ = (float(0), float(0), float(0), float(0))
        return stats_
    def getIfElseCount(self):
        cnt_ = 0
        elemList = self.getElementList(SMCONSTS.IF_REGEX)
        cnt_ = len(elemList)
        return cnt_



    def getUndefCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_UNDEF_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getNoOfGitUsages(self):
        cnt_ = 0
        compiledIncludeRE1 = re.compile(SMCONSTS.ONLY_GIT_REGEX)
        cnt_1 = len(compiledIncludeRE1.findall(self.fileText))

        compiledIncludeRE2 = re.compile(SMCONSTS.INAVLID_GIT_REGEX)
        cnt_2 = len(compiledIncludeRE2.findall(self.fileText))

        if cnt_2 > cnt_1:
          cnt_ = 0
        else:
          cnt_ = cnt_1 - cnt_2
        return cnt_



    def getVarAssiCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.VAR_ASSIGN_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        #  print match
        return cnt_




    def getCaseStmtCount(self):
        cnt_ = 0
        elemList = self.getElementList(SMCONSTS.CASE_REGEX)
        cnt_ = len(elemList)
        return cnt_
    # def getColonizedReqCount(self):
    #     cnt_ = 0
    #     compiledIncludeRE = re.compile(SMCONSTS.COLON_REQI_REGEX)
    #     cnt_ = len(compiledIncludeRE.findall(self.fileText))
    #     return cnt_
    def getEnvCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_ENV_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getCronCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_CRON_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_
    def getReffCount(self):
        ### gives the count of '=>' s
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.ONLY_REFF_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        #for match in (compiledIncludeRE.findall(self.fileText)):
        # print match
        return cnt_

##Added Feb 17, 2017
    def getURLUsages(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.URL_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_

    def getOnlyUnlessCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.UNLESS_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_

    def getCondCount(self):
        cnt_ = 0

        compiledIncludeRE1 = re.compile(SMCONSTS.COND1_REGEX)
        cnt_1 = len(compiledIncludeRE1.findall(self.fileText))

        compiledIncludeRE2 = re.compile(SMCONSTS.COND2_REGEX)
        cnt_2 = len(compiledIncludeRE2.findall(self.fileText))

        compiledIncludeRE3 = re.compile(SMCONSTS.COND3_REGEX)
        cnt_3 = len(compiledIncludeRE3.findall(self.fileText))

        cnt_ = cnt_1 + cnt_2 + cnt_3
        return cnt_

    def getOnlyNamenodeCount(self):
        cnt_ = 0
        compiledIncludeRE = re.compile(SMCONSTS.NAMENODE_REGEX)
        cnt_ = len(compiledIncludeRE.findall(self.fileText))
        return cnt_

class ExElement(object):
    def __init__(self, elementObj, startIndex, endIndex):
            self.elementObj = elementObj
            self.startIndex = startIndex
            self.endIndex = endIndex
