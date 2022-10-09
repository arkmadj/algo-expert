def validateSubsequenceWhile(array, sequence):
  arrIdx = 0
  seqIdx = 0
  while arrIdx < len(array) and seqIdx < len(sequence):
    if array[arrIdx] == sequence[seqIdx]:
      seqIdx += 1
    arrIdx += 1
  return seqIdx == len(sequence)
  
def validateSubsequenceFor(array, sequence):
  seqIdx = 0
  for num in array:
    if seqIdx == len(sequence):
      break
    if num == sequence[seqIdx]:
      seqIdx += 1
  return seqIdx == len(sequence)

a = [5,1,22,25,6,-1,8,10]
b = [1,6,-1,10]

print(validateSubsequenceWhile(a, b))
print(validateSubsequenceFor(a, b))