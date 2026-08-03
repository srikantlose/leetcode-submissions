# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        curr=head
        prev=None
        if not head: return Node(insertVal,head)
        if head.next==head: 
            head.next=Node(insertVal,head)
            return head
        while curr:
            prev=curr
            if(curr.val<=insertVal and curr.next.val>insertVal):
                break
            curr=curr.next
        
        prev.next=Node(insertVal,curr.next)
        return head