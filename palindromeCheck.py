import string
from turtle import left


def isPalindromeRevString(s):
  reversedString = ""
  for i in reversed(range(len(s))):
    reversedString += s[i]
  return s == reversedString

def isPalindromRevChars(s):
  reversedChars = []
  for i in reversed(range(len(s))):
    reversedChars.append(s[i])
  return s == "".join(reversedChars)

def isPalindromeRecu(s, i = 0):
  j = len(s) - 1 - i
  return True if i >= j else s[i] == s[j] and isPalindromeRecu(s, i+1)

def isPalindromeRecuTail(s, i = 0):
  j = len(s) - 1 - i
  if i >= j:
    return True
  if s[i] != s[j]:
    return False
  return isPalindromeRecuTail(s, i + 1)

def isPalindromeTwoPointers(s):
  leftIdx = 0
  rightIdx = len(s) - 1
  while leftIdx < rightIdx:
    if s[leftIdx] != s[rightIdx]:
      return False
    leftIdx += 1
    rightIdx -= 1
  return True

if __name__ == "__main__":
  print("Reversed string")
  print(isPalindromeRevString("abcdcba"))
  print(isPalindromeRevString("madam")) 
  print(isPalindromeRevString("madman"))
  print("Reversed Chars")
  print(isPalindromRevChars("abcdcba"))
  print(isPalindromRevChars("madam")) 
  print(isPalindromRevChars("madman"))
  print("Recursive")
  print(isPalindromeRecu("abcdcba"))
  print(isPalindromeRecu("madam")) 
  print(isPalindromeRecu("madman"))
  print("Recursive tail")
  print(isPalindromeRecuTail("abcdcba"))
  print(isPalindromeRecuTail("madam")) 
  print(isPalindromeRecuTail("madman"))
  print("Two pointer")
  print(isPalindromeTwoPointers("abcdcba"))
  print(isPalindromeTwoPointers("madam")) 
  print(isPalindromeTwoPointers("madman"))