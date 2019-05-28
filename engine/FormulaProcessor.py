import re
class FormulaProcessor:

    def __init__(self, formula):

        self.formula = formula
        yX = self.stringFilter(re.split(r'\~+', self.formula))
        
        if len(yX) != 2:
            raise Exception(f"{formula} does not have $a~b$ format")

        self.fieldY = yX[0]
        self.formulaX = yX[1]
        self.fieldsX = self.stringFilter(re.split(r'\++', self.formulaX))

        pass
    

    def stringFilter(self, strings):

        filtered = []

        for s in strings:
            s = s.strip()
            if len(s) > 0:
                filtered.append(s)
        
        return filtered
    

    def getData(self, formula)