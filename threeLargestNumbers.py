def threeLargestNumbers(array):
  threeLargest = [None, None, None]
  for num in array:
      updatelargest(threeLargest, num)
  return threeLargest

def updatelargest(threeLargest, num):
  if threeLargest[2] is None or num > threeLargest[2]:
    shiftAndUpdate(threeLargest, num, 2)
  elif threeLargest[1] is None or num > threeLargest[1]:
    shiftAndUpdate(threeLargest, num, 1)
  elif threeLargest[0] is None or num > threeLargest[0]:
    shiftAndUpdate(threeLargest, num, 0)
    
def shiftAndUpdate(array, num, idx):
  for i in range(idx + 1):
    if i == idx:
      array[i] = num
    else:
      array[i] = array[i+1]

a = [141,1,17,-7,-17,-27,18,541,8,7,7]

print(threeLargestNumbers(a))