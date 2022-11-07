def fourNumberSum(array, targetSum):
  allPairSums = {}
  quadruplets = []
  for i in range(1, len(array) - 1):
    for j in range(i + 1, len(array)):
      currentSum = array[i] + array[j]
      differnce = targetSum - currentSum
      if differnce in allPairSums:
        for pair in allPairSums[differnce]:
          quadruplets.append(pair + [array[i], array[j]])
    for k in range(0, i):
      currentSum = array[i] + array[k]
      if currentSum not in allPairSums:
        allPairSums[currentSum] = [[array[k], array[i]]]
      else:
        allPairSums[currentSum].append([array[k], array[i]])
  return quadruplets

a = [7, 6, 4, -1, 1, 2]
print(fourNumberSum(a, 16))