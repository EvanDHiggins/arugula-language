types = ['Int']

class Expression:
    def __init__(self, exprType, exprText):
        self.arugulaType = exprType
        self.text = exprText

    def type(self):
        return self.arugulaType
