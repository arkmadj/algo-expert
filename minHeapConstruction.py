class MinHeap:
  def __init__(self):
    self.heap = self.buildHeap(array)

  def buildHeap(self, array):
    pass
  
  def siftDown(self, currentIdx, endIdx, heap):
    pass
  
  def siftUp(self, currentIdx, heap):
    pass
  
  def peek(self):
    return self.heap[0]
  
  def remove(self):
    self.swap(0, len(self.heap) - 1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(o, len(self.heap) - 1, self.heap)
    return valueToRemove
  
  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)
  
  def swap(self, i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]

if __name__ == "__main__":
  #  a = [30,102,23,17,18,9,44,12,31]
