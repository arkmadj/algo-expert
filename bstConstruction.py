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
  
a = BST(10)
a.insert(5)
a.insert(2)
a.insert(13)
a.insert(14)
a.insert(22)
a.insert(5)
a.insert(15)
print(a.findClosestValueInBSTRecursive(12))
print(a.findClosestValueInBSTIterative(12))

print(a)