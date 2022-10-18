def getNthFibRecu(n):
  if n == 2:
    return 1
  elif n == 1:
    return 0
  else:
    return getNthFibRecu(n-1) + getNthFibRecu(n-2)
  
def getNthFibMemo(n, memoize = {1: 0, 2: 1}):
  if n in memoize:
    return memoize[n]
  else:
    memoize[n] = getNthFibMemo(n-1, memoize) + getNthFibMemo(n-2, memoize)
    return memoize[n]
  
def getNthFibIter(n):
  lastTwo = [0, 1]
  counter = 3
  while counter <= n:
    nextFib = lastTwo[0] + lastTwo[1]
    lastTwo[0] = lastTwo[1]
    lastTwo[1] = nextFib
    counter += 1
  return lastTwo[1] if n > 1 else lastTwo[0]

print(getNthFibRecu(6))
print(getNthFibMemo(6))
print(getNthFibIter(6))