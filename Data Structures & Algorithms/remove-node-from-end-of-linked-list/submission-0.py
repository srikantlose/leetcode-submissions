# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=dummy
        count=0
        while curr:
            curr=curr.next
            count+=1
        tbd=count-n-1
        count=0
        curr=dummy
        while curr:
            if(count!=tbd):
                count+=1
            else:
                break
            curr=curr.next
        curr.next=curr.next.next
        return dummy.next