def powerSet(array):
  subsets = [[]]
  for element in array:
    for i in range(len(subsets)):
      currentSubset = subsets[i]
      subsets.append(currentSubset + [element])
  return subsets


def powerSetRecu(array, idx = None):
  if idx is None:
    idx = len(array) - 1
  elif idx < 0:
    return [[]]
  element = array[idx]
  subsets = powerSetRecu(array, idx - 1)
  for i in range(len(subsets)):
    currentSubset = subsets[i]
    subsets.append(currentSubset + [element])
  return subsets


a = [1,2,3]
print(powerSet(a))
print(powerSetRecu(a))