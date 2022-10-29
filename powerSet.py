def powerSet(array):
  subsets = [[]]
  for element in array:
    for i in range(len(subsets)):
      currentSubset = subsets[i]
      subsets.append(currentSubset + [element])
  return subsets


a = [1,2,3]
print(powerSet(a))