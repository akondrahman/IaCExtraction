import re

import SourceModel.SM_Element
from SmellDetector import Utilities


class SM_IncludeResource(SourceModel.SM_Element.SM_Element):
    def __init__(self, text, name=None):
        self.resourceText = text
        self.className = name
        #super().__init__(text)
        SourceModel.SM_Element.SM_Element.__init__(self, text)        

    def getUsedVariables(self):
        #return super().getUsedVariables()
        return SourceModel.SM_Element.SM_Element.getUsedVariables(self)

    def getPhysicalResourceDeclarationCount(self):
        compiledRE = re.compile(r'\'.+\'\W*:|\".+\":')
        tempVar = compiledRE.findall(self.resourceText)
        Utilities.myPrint("Found include declarations: " + str(tempVar))
        return len(tempVar)
