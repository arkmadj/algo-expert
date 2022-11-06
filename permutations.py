def getPermutationsOne(array):
  permutations = []
  permutationsHelper(array, [], permutations)
  return permutations

def permutationsHelper(array, currentPermutation, permutations):
  if not len(array) and len(currentPermutation):
    permutations.append(currentPermutation)
  else:
    for i in range(len(array)):
      newArray = array[:i] + array[i+1:]
      newPermutation = currentPermutation + [array[i]]
      permutationsHelper(newArray, newPermutation, permutations)
      
def getPermutationsTwo(array):
  permutations = []
  permutationsHelperTwo(0, array, permutations)
  return permutations

def permutationsHelperTwo(i, array, permutations):
  if i == len(array) - 1:
    permutations.append(array[:])
  else:
    for j in range(i, len(array)):
      swap(array, i , j)
      permutationsHelperTwo(i + 1, array, permutations)
      swap(array, i, j)

def swap(array, i, j):
  array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
  a = [1,2,3]
  b = [1,2,3, 4,5]
  print(getPermutationsOne(a))
  print(getPermutationsTwo(a))
  print(getPermutationsOne(b))
  print(getPermutationsTwo(b))