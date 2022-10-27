def maxSubsetSumNoAdjacent(array):
  if not len(array):
    return
  elif len(array) == 1:
    return array[0]
  maxSums = array[:]
  maxSums[1] = max(array[0], array[1])
  for i in range(2, len(array)):
    maxSums[i] = max(maxSums[i-1], maxSums[i-2]+array[i])
  return maxSums[-1]

def maxSubsetSumNoAdjacentOptimize(array):
  if not len(array):
    return
  elif len(array) == 1:
    return array[0]
  second = array[0]
  first = max(array[0], array[1])
  for i in range(2, len(array)):
    current = max(first, second + array[i])
    second = first
    first = current
  return first


if __name__ == "__main__":
  a = [7,10,12,7,9,14]
  print(maxSubsetSumNoAdjacent(a))
  print(maxSubsetSumNoAdjacentOptimize(a))