import SourceModel.SM_Element

class SM_Exec(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        #super().__init__(text)
        SourceModel.SM_Element.SM_Element.__init__(self, text)        

    def getUsedVariables(self):
        #return super().getUsedVariables()
        return SourceModel.SM_Element.SM_Element.getUsedVariables(self)