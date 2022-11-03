class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):

        decendantOneArray = []
        decendantTwoArray = []

        decendantOneCurrent = descendantOne
        while decendantOneCurrent is not None:
             decendantOneArray.append(decendantOneCurrent)
             decendantOneCurrent = decendantOneCurrent.ancestor

        decendantTwoCurrent = descendantTwo
        while decendantTwoCurrent is not None:
             decendantTwoArray.append(decendantTwoCurrent)
             decendantTwoCurrent = decendantTwoCurrent.ancestor
            
        commonAncestor = None
    
        while decendantOneArray and  decendantTwoArray:
              d1Pop = decendantOneArray.pop()
              d2Pop = decendantTwoArray.pop()

              if d1Pop.name == d2Pop.name:
                commonAncestor = d1Pop
                if d1Pop.name in (descendantOne.name, descendantTwo.name) :
                    break
              else:
                if descendantOne.name in (d1Pop.name,d2Pop.name) or descendantTwo.name in (d1Pop.name,d2Pop.name):
                    break

        return commonAncestor




aD = AncestralTree('D')

aH = AncestralTree('H')
aI = AncestralTree('I')

aH.ancestor = aD
aI.ancestor = aD

aB = AncestralTree('B')
aA = AncestralTree('A')
aE = AncestralTree('E')

aC = AncestralTree('C')

aD.ancestor = aB
aE.ancestor = aB

aB.ancestor = aA
aC.ancestor = aA



print(getYoungestCommonAncestor(aA, aE, aI))

