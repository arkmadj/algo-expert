class MinMaxStaxk:
  def __init__(self):
    self.minMaxStack = []
    self.stack = []
  
  def peek(self):
    return self.stack[len(self.stack) - 1]
  
  def pop(self):
    self.minMaxStack.pop()
    return self.stack.pop()
  
  def push(self, number):
    newMinMax = {"min": number, "max": number}
    if len(self.minMaxStack):
      lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
      newMinMax["min"] = min(lastMinMax["min"], number)
      newMinMax["max"] = max(lastMinMax["max"], number)
    self.minMaxStack.append(newMinMax)
    self.stack.append(number)
  
  def getMin(self):
    return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
  
  def getMax(self):
    return self.minMaxStack[len(self.minMaxStack) - 1]["max"]
  
if __name__ == "__main__":
  a = MinMaxStaxk()
  a.push(5)
  print("Min: ", a.getMin())
  print("Max: ", a.getMax())
  print("Peek: ", a.peek())
  a.push(7)
  print("Min: ", a.getMin())
  print("Max: ", a.getMax())
  print("Peek: ", a.peek())
  a.push(2)
  print("Min: ", a.getMin())
  print("Max: ", a.getMax())
  print("Peek: ", a.peek())