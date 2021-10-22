class Node:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next

def sorted(head):
  if head is None or head.next is None:
    return True



listA = sorted(Node(1, Node(1, Node(1, Node(1, Node(1)))))) #T
# print(listA)
listB = sorted(Node(1, Node(2, Node(3, Node(4))))) #T
listC = sorted(Node(1, Node(2, Node(3, Node(2, Node(6, Node(7))))))) #F
listD = sorted(Node(11, Node(2, Node(3, Node(4, Node(6, Node(7))))))) #F
listE = sorted(Node(1)) #T
listF = sorted(Node(2, Node(4, Node(6, Node(0))))) #F


# // Check first two nodes and recursively call for next node.
#     return ((head->data > head->next->data) && isSorted(head->next)); 