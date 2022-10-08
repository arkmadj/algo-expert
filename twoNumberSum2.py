def twoNumberSum(array, targetSum):
  for i in range(len(array) - 1):
    firstNum = array[i]
    for j in range(i+1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]
  return []

a = [1,2,3,4,5,6,7,8,9]
t= 10


def twoNumberSumSpace(array, targetSum):
  nums = {}
  for num in array:
    potentialMatch = targetSum - num
    if potentialMatch in nums:
      return [potentialMatch, num]
    else:
      nums[num] = True
  return []

def twoNumberSumSort(array, targetSum):
  array.sort()
  left = 0
  right = len(array) - 1
  while left < right:
    currentSum = array[left] + array[right]
    print(currentSum)
    if currentSum == targetSum:
      return [array[left], array[right]]
    elif currentSum < targetSum:
      left += 1
    else:
      right -= 1
  return []


print(twoNumberSum(a,t))
print(twoNumberSumSpace(a,t))
print(twoNumberSumSort(a,t))