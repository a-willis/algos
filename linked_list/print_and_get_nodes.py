class Node:
  def __init__(self, data = 0, next_node=None):
    self.data = data
    self.next = next_node

	# make string represention of a node , return string
  def __repr__(self):
    return str(self.data)


class LinkedList:
  def __init__(self, start):
    self.start = start

  def __repr__(self):
    string = ""
    node = self.start                   # reference start node , keep track of position
    while True:
      string += str(node) + " "         # Append the string representation of the node to a string
      if node.next is None:
        break
      node = node.next                  # moving pointer one node up and repeat process of appending node to string
    return string

  def __len__(self):
    length = 0
    node = self.start                   
    while True:
      length += 1        
      if node.next is None:
        break
      node = node.next                  
    return length

  # grab particular element 
  def get(self, index):
    node = self.start
    for i in range(index):
      node = node.next
    return node.data



linked_list = LinkedList(Node(5, Node(10, Node(15, Node(20, Node(25))))))
print(linked_list)
print(len(linked_list))




# add new node to beginning
# linked_list.start = Node(0, next_node=linked_list.start)
# print(linked_list)
# print(linked_list.get(3))
# linked_list.start = Node(0, next_node = linked_list.start)
# print(linked_list.start)