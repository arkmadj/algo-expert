from unittest import result


def groupedAnagrams(words):
  if len(words) == 0:
    return []

  sortedWords = ["".join(sorted(w)) for w in words]
  indices = [i for i in range(len(words))]
  indices.sort(key=lambda x: sortedWords[x])

  result = []
  currentAnagramGroup = []
  currentAnagram = sortedWords[indices[0]]
  for index in indices:
    word = words[index]
    sortedWord = sortedWords[index]
    
    if sortedWord == currentAnagram:
      currentAnagramGroup.append(word)
      continue
    
    result.append(currentAnagramGroup)
    currentAnagramGroup = [word]
    currentAnagram = sortedWord
    
  result.append(currentAnagramGroup)

  return result

def groupedAnagramsSimplier(words):
  anagrams = {}
  for word in words:
    sortedWord = "".join(sorted(word))
    if sortedWord in anagrams:
      anagrams[sortedWord].append(word)
    else:
      anagrams[sortedWord] = [word]
  return list(anagrams.values())


a = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
print(groupedAnagrams(a))
print(groupedAnagramsSimplier(a))