class TreeInfo:
    def __init__(self, node = None, distance = 0):
        self.node = node
        self.distance = distance


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    
    treeInfo = findNodeDistanceWithTarget(tree.left,target,0)
    if not treeInfo:
        treeInfo = findNodeDistanceWithTarget(tree.right,target,0)

    result = []
    findNodesWithDistance(treeInfo.node,k, result, 0)


    print(result)


        

def findNodesWithDistance(node, k, result, distance):
    if node is None:
        return result
    
    if distance == k:
        result.append(node.value)
        return result

    distance += 1

    findNodesWithDistance(node.left, k, result, distance)

    findNodesWithDistance(node.right, k, result, distance)

    return result
    


def findNodeDistanceWithTarget(tree, target, distance):
    if tree is None:
        return None
    
    if tree.value == target:
        return TreeInfo(tree, distance)

    distance += 1

    treeInfo = findNodeDistanceWithTarget(tree.left, target, distance)
    if not treeInfo:
         treeInfo = findNodeDistanceWithTarget(tree.right, target, distance)

    if treeInfo:
        return treeInfo

    
    return None
    




tree = BinaryTree(1)

tree.left = BinaryTree(2)
tree.right = BinaryTree(3)

tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)

tree.right.right = BinaryTree(6)

tree.right.right.left = BinaryTree(7)
tree.right.right.right = BinaryTree(8)


findNodesDistanceK(tree,3,1)