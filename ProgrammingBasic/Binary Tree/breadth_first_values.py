class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def breadth_first_values(root):
    traverseStack = [root]
    visitedNodes = []
    while traverseStack:
      current = traverseStack.pop()
      if not current:
        continue
        
      visitedNodes.append(current.val)
    
      traverseStack.append(current.left)
      traverseStack.append(current.right)
    
    return visitedNodes
      
      
print(breadth_first_values(a))