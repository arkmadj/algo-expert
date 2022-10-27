def invertBinaryTree(tree):
  queue = [tree]
  while len(queue):
    current = queue.pop(0)
    if current is None:
      continue
    swapLeftAndRight(current)
    queue.append(current.left)
    queue.append(current.right)

def swapLeftAndRight(tree):
  tree.left, tree.right = tree.right, tree.left
  
def invertBinaryTreeRecu(tree):
  if tree is None:
    return
  swapLeftAndRight(tree)
  invertBinaryTreeRecu(tree.left)
  invertBinaryTreeRecu(tree.right)
  

if __name__ == "__main__":
  # Fix this with import BST
  pass