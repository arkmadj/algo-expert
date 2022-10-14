class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
  def insert(self, value):
    currentNode = self
    while True:
      if value < currentNode.value:
        if currentNode.left is None:
          currentNode.left = BST(value)
          break
        else:
          currentNode = currentNode.left
      else:
        if currentNode.right is None:
          currentNode.right = BST(value)
          break
        else:
          currentNode = currentNode.right
    return self
  
  def contains(self, value):
    currentNode = self
    while currentNode is not None:
      if value < currentNode.value:
        currentNode = currentNode.left
      elif value > currentNode.value:
        currentNode = currentNode.right
      else:
        return True
    return False
  
  def remove(self, value, parentNode = None):
    currentNode = self
    while currentNode is not None:
      if value < currentNode.value:
        parentNode = currentNode
        currentNode = currentNode.left
      elif value > currentNode.value:
        parentNode = currentNode
        currentNode = currentNode.right
      else:
        if currentNode.left is not None and currentNode.right is not None:
          currentNode.value = currentNode.right.getMinValue()
          currentNode.right.remove(currentNode.value, currentNode)
        elif parentNode is None:
          if currentNode.left is not None:
            currentNode.value = currentNode.left.value
            currentNode.right = currentNode.left.right
            currentNode.left = currentNode.left.left
          elif currentNode.right is not None:
            currentNode.value = currentNode.right.value
            currentNode.left = currentNode.right.left
            currentNode.right = currentNode.right.right
          else:
            currentNode.value = None
        elif parentNode.left == currentNode:
          parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
        elif parentNode.right == currentNode:
          parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
        break
    return self
  
  def getMinValue(self):
    currentNode = self
    while currentNode.left is not None:
      currentNode = currentNode.left
    return currentNode.value\
      
  def findClosestValueInBSTRecursive(self, target):
    currentNode = self
    return self.findClosestValueInBSTHelperRecursive(currentNode, target, float("inf"))
  
  def findClosestValueInBSTHelperRecursive(self, tree, target, closest):
    if tree is None:
      return closest
    if abs(target - closest) > abs(target - tree.value):
      closest = tree.value
    if target < tree.value:
      return self.findClosestValueInBSTHelperRecursive(tree.left, target, closest)
    elif target > tree.value:
      return self.findClosestValueInBSTHelperRecursive(tree.right, target, closest)
    else:
      return closest
    
  def findClosestValueInBSTIterative(self, target):
    currentNode = self
    return self.findClosestValueInBSTHelperIterative(currentNode, target, float("inf"))
  
  def findClosestValueInBSTHelperIterative(self, tree, target, closest):
    currentNode = tree
    while currentNode is not None:
      if abs(target - closest) > abs(target - currentNode.value):
        closest = currentNode.value
      if target < currentNode.value:
        currentNode = currentNode.left
      elif target > currentNode.value:
        currentNode = currentNode.right
      else:
        break
    return closest
  
  def inOrderTraversal(self):
    currentNode = self
    return self.inOrderTraversalHelper(currentNode, array=[])
  
  def inOrderTraversalHelper(self, tree, array):
    if tree is not None:
      self.inOrderTraversalHelper(tree.left, array)
      array.append(tree.value)
      self.inOrderTraversalHelper(tree.right, array)
    return array
  
  def preOrderTraversal(self):
    currentNode = self
    return self.preOrderTraversalHelper(currentNode, array=[])
  
  def preOrderTraversalHelper(self, tree, array):
    if tree is not None:
      array.append(tree.value)
      self.preOrderTraversalHelper(tree.left, array)
      self.preOrderTraversalHelper(tree.right, array)
    return array
  
  def postOrderTraversal(self):
    currentNode = self
    return self.postOrderTraversalHelper(currentNode, array=[])
  
  def postOrderTraversalHelper(self, tree, array):
    if tree is not None:
      self.postOrderTraversalHelper(tree.left, array)
      self.postOrderTraversalHelper(tree.right, array)
      array.append(tree.value)
    return array
  
  def flattenBinaryTreeInOrder(self):
    inOrderNodes = self.flattenBinaryTreeInOrderHelper(self, [])
    for i in range(0, len(inOrderNodes) - 1):
      leftNode = inOrderNodes[i]
      rightNode = inOrderNodes[i+1]
      leftNode.right = rightNode
      rightNode.left = leftNode
    return inOrderNodes[0]
  
  def flattenBinaryTreeInOrderHelper(self, tree, array):
    if tree is not None:
      self.flattenBinaryTreeInOrderHelper(tree.left, array)
      array.append(tree)
      self.flattenBinaryTreeInOrderHelper(tree.right, array)
    return array
      
  def flattenBinaryTree(self):
    currentNode = self
    if currentNode is None:
      return
    leftMost, _ = self.flattenTree(currentNode)
    return leftMost
  
  def flattenTree(self, node):
    if node is None:
      return [None, None]
    
    # if node.left is None:
    #   leftMost = node
    #   print("I am none")
    if node.left is None:
      leftMost = node
    else:
      leftSubtreeLeftMost, leftSubtreeRightMost = self.flattenTree(node.left)
      self.connectNodes(leftSubtreeRightMost, node)
      leftMost = leftSubtreeLeftMost
    
    if node.right is None:
      rightMost = node
    else:
      rightSubtreeLeftMost, rightSubtreeRightMost = self.flattenTree(node.right)
      self.connectNodes(node, rightSubtreeLeftMost)
      rightMost = rightSubtreeRightMost
      
    return [leftMost, rightMost]
  
  def connectNodes(self, left, right):
    left.right = right
    right.left = left
    
  def branchSums(self):
    sums = []
    self.calculateBranchSums(self, 0, sums)
    return sums
    
  def calculateBranchSums(self, node, runningSum, sums):
    if node is None:
      return
    
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
      sums.append(newRunningSum)
      return
    
    self.calculateBranchSums(node.left, newRunningSum, sums)
    self.calculateBranchSums(node.right, newRunningSum, sums)
    
  def nodeDepthsItrerative(self):
    sumOfDepths = 0
    stack = [{"node": self, "depth": 0}]
    while len(stack) > 0:
      nodeInfo = stack.pop()
      node, depth  = nodeInfo["node"], nodeInfo["depth"]
      if node is None:
        continue
      sumOfDepths += depth
      stack.append({"node": node.left, "depth": depth+1})
      stack.append({"node": node.right, "depth": depth+1})
    return sumOfDepths
  
  def nodeDepthsRecursive(self):
    return self.nodeDepthsRecursiveHelper(self,0)
  
  def nodeDepthsRecursiveHelper(self, node, depth=0):
    if node is None:
      return 0
    return depth + self.nodeDepthsRecursiveHelper(node.left, depth+1) + self.nodeDepthsRecursiveHelper(node.right, depth+1)
  
  def depthFirstSearch(self):
    return self.depthFirstSearchHelper(self, [])
    
  def depthFirstSearchHelper(self, node, array):
    array.append(node.value)
    if node.left is not None:
      self.depthFirstSearchHelper(node.left, array)
    if node.right is not None:
      self.depthFirstSearchHelper(node.right, array)
    return array
  
  def breadthFirstSearch(self):
    array = []
    queue = [self]
    
    while len(queue) > 0:
      current = queue.pop(0)
      array.append(current.value)
      if current.left is not None:
        queue.append(current.left)
        
      if current.right is not None:
        queue.append(current.right)
        
    return array
  
  def allKindsOfnodeDepthsIterative(self):
    sumofAllDepths = 0
    stack = [self]
    while len(stack) > 0:
      node = stack.pop()
      if node is None:
        continue
      sumofAllDepths += self.nodeDepthsRecursiveHelper(node)
      stack.append(node.left)
      stack.append(node.right)
    return sumofAllDepths
  
  def allKindsOfNodeDepthsRecursive(self):
    return self.nodeDepthsRecursiveHelper(self, 0)
  
  def allKindsOfNodeDepthRecursiveHelper(self, node):
    if node is None:
      return 0
    return self.allKindsOfNodeDepthRecursiveHelper(node.left) + self.allKindsOfNodeDepthRecursiveHelper(node.right) + self.nodeDepthsRecursiveHelper(node)
      
a = BST(10)
a.insert(5)
a.insert(2)
a.insert(13)
a.insert(14)
a.insert(22)
a.insert(5)
a.insert(15)
# print(a.findClosestValueInBSTRecursive(12))
# print(a.findClosestValueInBSTIterative(12))
# print(a.inOrderTraversal())
# print(a.preOrderTraversal())
# print(a.postOrderTraversal())
# print(a.flattenBinaryTreeInOrder())
# print(a.flattenBinaryTree())
# print(a.branchSums())
print(a.nodeDepthsItrerative())
print(a.nodeDepthsRecursive())
print(a.depthFirstSearch())
print(a.breadthFirstSearch())
print(a.allKindsOfnodeDepthsIterative())
# print(a.allKindsOfNodeDepthsRecursive())


# print(a)