class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head or not head.next:
        #     return
        
        
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        
        # prev, cur = None, slow.next
        # slow.next = None # Split the list into two halves
        # while cur:
        #     nextRef = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nextRef
        
        # first, second = head, prev
        # while second:
        #     tmp1, tmp2 = first.next, second.next
        #     first.next = second
        #     second.next = tmp1
        #     first = tmp1
        #     second = tmp2

        slow=fast=head
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        
        prev,cur=None,slow.next
        while(cur):
            nextRef=cur.next
            cur.next=prev
            prev=cur
            cur=nextRef
        first,second=head,prev
        while second:
            temp1, temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2

