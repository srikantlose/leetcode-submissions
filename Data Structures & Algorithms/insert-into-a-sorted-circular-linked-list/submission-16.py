# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        dummy=Node(0,head)
        curr=dummy
        prev=None
        count=1
        if not head:
            new= Node(insertVal,head)
            new.next=new
            return new
        if head.next==head: 
            head.next=Node(insertVal,head)
            return head
        while curr:
            prev=curr
            curr=curr.next
            if(curr.val<=insertVal and curr.next.val>insertVal):
                curr.next=Node(insertVal,curr.next)
                break
            
            if curr==head:
                count+=1
                break
            
        
        
        if count>1:
            nextRef=head.next
            head.next=Node(insertVal,head.next)
        return dummy.next