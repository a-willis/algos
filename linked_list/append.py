class Node:
  def __init__(self, data = 0, next = None): 
    self.data = data
    self.next = next

def arrayify(head):
  array = []
  ptr = head
  while ptr != None:
    array.append(ptr.value)
    ptr = ptr.next
  return array

#recursive
def append(self, target):
  if self.next is not None:
    self.next = Node(target)
  else:
    self.next.append(target)


# Test Cases
LL1 = Node(1, Node(4, Node(5)))
# print(arrayify(append(None, 1))) # [1]
print(arrayify(append(LL1, 7))) # [1, 4, 5, 7]
print(arrayify(append(Node(), 7))) # [0, 7]

