def twoNumberSumA(array, targetSum):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[i] + array[j] == targetSum:
        return [array[i], array[j]]
  return []


def twoNumberSumB(array, targetSum):
  array.sort()
  left = 0
  right = len(array) - 1
  while left < right:
    currentSum = array[left] + array[right]
    if currentSum == targetSum:
      return [array[left], array[right]]
    elif currentSum < targetSum:
      left += 1
    else:
      right -= 1
  return []

def twoNUmberSumC(array, targetSum):
  nums = {}
  for num in array:
    potentialMatch = targetSum - num
    if potentialMatch in nums:
      return [potentialMatch, num]
    else:
      nums[num] = True
  return []

print(twoNumberSumB([3, 5, -4, 8, 11, 1, -1, 6], 10))

print(twoNumberSumA([3, 5, -4, 8, 11, 1, -1, 6], 10))

print(twoNUmberSumC([3, 5, -4, 8, 11, 1, -1, 6], 10))

