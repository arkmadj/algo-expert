from operator import truediv


def isMonotonic(array):
  if len(array) < 2:
    return True
  
  direction = array[1] - array[0]
  for i in range(2, len(array)):
    if direction == 0:
      direction = array[i] - array[i-1]
      continue
    if breaksDirection(direction, array[i- 1], array[i]):
      return False
    
  return True

def breaksDirection(direction, previousInt, currentInt):
  difference = currentInt - previousInt
  if direction > 0:
    return difference < 0
  return difference > 0

def isMonotonicTwo(array):
  isNonDecreasing = True
  isNonIncreasing = True
  
  for i in range(1, len(array)):
    if array[i] < array[i-1]:
      isNonDecreasing = False
    if array[i] > array[i-1]:
      isNonIncreasing = False
      
  return isNonDecreasing or isNonIncreasing

a = [-1,-5,-10,-1100,-1100,-1100,-1101,-1102,-9001]
b = [1,1,1,2,3,4,3,4,5]

print(isMonotonic(a))
print(isMonotonic(b))
print(isMonotonicTwo(a))
print(isMonotonicTwo(b))