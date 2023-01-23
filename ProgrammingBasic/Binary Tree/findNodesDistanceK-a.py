class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space - where n is the number of nodes in the tree
def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)
    return breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)

def breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
    # We could use the `deque` object instead of a standard Python
    # list if we wanted to optimize our `.pop(0) operations.`
    queue = [(targetNode, 0)]
    seen = {targetNode.value}
    while len(queue) > 0:
        currentNode, distanceFromTarget = queue.pop(0)
        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue]
            nodesDistanceK.append(currentNode.value)
            return nodesDistanceK
        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue
            if node.value in seen:
                continue
            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))
    return []

def getNodeFromValue(value, tree, nodesToParents):
    if tree.value == value:
        return tree
    nodeParent = nodesToParents[value]
    if nodeParent.left is not None and nodeParent.left.value == value:
        return nodeParent.left
    return nodeParent.right

def populateNodesToParents(node, nodesToParents, parent=None):
    if node is not None:
        nodesToParents[node.value] = parent
        populateNodesToParents(node.left, nodesToParents, node)
        populateNodesToParents(node.right, nodesToParents, node)



tree = BinaryTree(1)

tree.left = BinaryTree(2)
tree.right = BinaryTree(3)

tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)

tree.right.right = BinaryTree(6)

tree.right.right.left = BinaryTree(7)
tree.right.right.right = BinaryTree(8)


findNodesDistanceK(tree,3,1)
