def maxSubsetSumNoAdjacent(array):
  if not len(array):
    return
  elif len(array) == 1:
    return array[0]
  maxSums = array[:]
  maxSums[1] = max(array[0], array[1])
  for i in range(2, len(array)):
    maxSums[i] = max(array[i-1], array[1-2]+array[i])
  return maxSums[-1]


if __name__ == "__main__":
  a = [7,10,12,7,9,14]
  print(maxSubsetSumNoAdjacent(a))