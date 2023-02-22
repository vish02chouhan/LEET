def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numImportantReports)

class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

# This is the input class.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
        
# Create the nodes.
a = OrgChart("A")
b = OrgChart("B")
c = OrgChart("C")
d = OrgChart("D")
e = OrgChart("E")
f = OrgChart("F")
g = OrgChart("G")
h = OrgChart("H")
i = OrgChart("I")
j = OrgChart("J")

# Set the relationships between the nodes.
a.directReports = [b, c]
b.directReports = [d, e]
c.directReports = [f, g]
d.directReports = [h, i]
e.directReports = [j]

# Set the variables for the input of getLowestCommonManager.
topManager = a
reportOne = e
reportTwo = i


outpot = getLowestCommonManager(a,e,j)


abab = 9