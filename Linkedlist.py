# العقدة الأساسية للقائمة المرتبطة
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# كلاس القائمة المرتبطة
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # الإضافة
  def append(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # طباعة العناصر
  def print(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# القائمة المرتبطة
LL = LinkedList()
LL.append(3)
LL.append(4)
LL.append(5)
LL.print()

