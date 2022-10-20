from re import L
from turtle import right


def binarySearchRecu(array, target):
  return binarySearchRecuHelper(array, target, 0, len(array) - 1)

def binarySearchRecuHelper(array, target, left, right):
  if left > right:
    return -1
  middle = (left + right) // 2
  potenetialMatch = array[middle]
  if potenetialMatch == target:
    return middle
  elif target < potenetialMatch:
    return binarySearchRecuHelper(array, target, left, middle - 1)
  else:
    return binarySearchRecuHelper(array, target, middle + 1, right)
  
def binarySearchIter(array, target):
  left = 0
  right = len(array) - 1
  while left <= right:
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if potentialMatch == target:
      return middle
    elif target < potentialMatch:
      right = middle - 1
    else:
      left = middle + 1
  return -1


print(binarySearchRecu([0,1,21,33,45,45,61,71,72,73],33))
print(binarySearchRecu([0,1,21,33,45,45,61,71,72,73],83))
print(binarySearchIter([0,1,21,33,45,45,61,71,72,73],33))
print(binarySearchIter([0,1,21,33,45,45,61,71,72,73],83))