class Node:
  def __init__(self, item) -> None:
    self.item = item
    self.next = None
class LinkedList:
  def __init__(self) -> None:
    self.head = None

def removeNthNodeFromTheEnd(head, n):
  counter = 1
  first = head
  second = head
  while counter <= n:
    second = second.next
    counter += 1
  if second is None:
    head.value = head.next.value
    head.next = head.next.next
    return
  while second.next is not None:
    second = second.next
    first = first.next
  first.next = first.next.next
  

if __name__ == "__main__":
  pass