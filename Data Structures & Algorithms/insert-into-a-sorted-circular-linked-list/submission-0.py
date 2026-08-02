# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            return Node(insertVal,head)
        curr=head
        prev=None
        while curr.next:
            prev=curr
            
            if curr.val<insertVal and curr.next.val>insertVal:
                break
            curr=curr.next
        nextRef=curr.next
        prev.next=Node(insertVal,nextRef)
        #curr.next.next=nextRef
        return head