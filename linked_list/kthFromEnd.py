class ListNode:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next

def kthFromLast(head,k):
  fast, slow = head, head
  





# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(kthFromLast(LL1, 0)) # 10
print(kthFromLast(LL1, 2)) # 3
print(kthFromLast(LL1, 5)) # 13