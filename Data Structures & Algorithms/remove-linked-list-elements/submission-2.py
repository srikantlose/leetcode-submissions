# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head
        if head.val==val:
            while head.val==val and head.next:
                head=head.next
        if head.val==val:
            head=None
            return head
        curr=head
        prev=None
        while curr.next:
            prev=curr
            curr=curr.next
            if curr.val==val:
                
                prev.next=curr.next 
        if curr.val==val:
            prev.next=None
            
        
        return head