class Result:
    def __init__(self,fulldata,genderData,relationshipData):
        self.fulldata=fulldata
        self.genderData=genderData
        self.relationshipData=relationshipData
    def getFullData(self):
        return self.fulldata

    def getGenferData(self):
        return self.genderData
    def getRelationshipData(self):
        return self.relationshipData