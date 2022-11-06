class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self) -> None:
    self.head = None
    
  def insertAtEnd(self, new_data):
    new_node = Node(new_data)
    
    if self.head is None:
      self.head = new_node
      return
    
    last = self.head
    while(last.next):
      last = last.next
      
    last.next = new_node
      
  def removeNthNodeFromTheEnd(self, n):
    counter = 1
    first = self.head
    second = self.head
    while counter <= n:
      second = second.next
      counter += 1
    if second is None:
      self.head.value = self.head.next.value
      self.head.next = self.head.next.next
      return
    while second.next is not None:
      second = second.next
      first = first.next
    first.next = first.next.next
    
  def printList(self):
    temp = self.head
    while(temp):
      print(str(temp.data) + "->", end="")
      temp = temp.next
  

if __name__ == "__main__":
  a = LinkedList()
  for i in range(10):
    a.insertAtEnd(i)
  a.printList()
  a.removeNthNodeFromTheEnd(4)
  print("\n")
  a.printList()