class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def branchSums(root):
  sums = []
  branchSumsHelper(root, 0, sums)
  return sums

def branchSumsHelper(node, runningSum, sums):
  if node is None:
    return
  newRunningSum = runningSum + node.value
  if node.left is None and node.right is None:
    sums.append(newRunningSum)
  branchSumsHelper(node.left, newRunningSum, sums)
  branchSumsHelper(node.right, newRunningSum, sums) 